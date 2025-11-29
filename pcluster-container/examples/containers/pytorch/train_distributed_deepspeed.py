"""
Multi-node Distributed Training Script for AWS ParallelCluster
Uses /scratch for HuggingFace caching to avoid permission issues
"""

import os
import socket
import torch
import torch.distributed as dist
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_from_disk
from datetime import datetime
import logging

# ============================================
# 캐시 디렉토리 설정
# ============================================
def setup_cache_dirs():
    """Set up cache directories, preferring /scratch over /tmp"""
    # /scratch가 있으면 사용, 없으면 /tmp 사용
    if os.path.exists("/scratch"):
        CACHE_BASE = "/scratch"
        print("✓ Using /scratch for caching (NVMe - Fast!)")
    else:
        CACHE_BASE = "/tmp"
        print("⚠ /scratch not found, using /tmp for caching")
    
    # 사용자별 캐시 디렉토리
    uid = os.getuid()
    HF_CACHE = f"{CACHE_BASE}/hf_cache_{uid}"
    TRANSFORMERS_CACHE = f"{CACHE_BASE}/transformers_cache_{uid}"
    TRITON_CACHE = f"{CACHE_BASE}/triton_cache_{uid}"
    
    # 디렉토리 생성
    os.makedirs(HF_CACHE, exist_ok=True)
    os.makedirs(TRANSFORMERS_CACHE, exist_ok=True)
    os.makedirs(TRITON_CACHE, exist_ok=True)
    
    # 환경 변수 설정
    os.environ['HF_DATASETS_CACHE'] = HF_CACHE
    os.environ['TRANSFORMERS_CACHE'] = TRANSFORMERS_CACHE
    os.environ['TRITON_CACHE_DIR'] = TRITON_CACHE
    os.environ['HF_HOME'] = HF_CACHE
    
    print(f"📦 Cache directories:")
    print(f"   HF_DATASETS_CACHE: {HF_CACHE}")
    print(f"   TRANSFORMERS_CACHE: {TRANSFORMERS_CACHE}")
    print(f"   TRITON_CACHE_DIR: {TRITON_CACHE}")
    
    return HF_CACHE, TRANSFORMERS_CACHE

# ============================================
# 데이터셋 전처리 함수
# ============================================
def prepare_dataset(examples, tokenizer, max_length=512):
    """Tokenize text data"""
    tokenized = tokenizer(
        examples["text"],
        truncation=True,
        max_length=max_length,
        padding="max_length",
        return_tensors=None
    )
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

# ============================================
# 메인 학습 함수
# ============================================
def main():
    # 로깅 설정
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [Rank %(rank)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # ============================================
    # 1. 캐시 디렉토리 설정 (가장 먼저!)
    # ============================================
    HF_CACHE, TRANSFORMERS_CACHE = setup_cache_dirs()
    
    # ============================================
    # 2. 분산 환경 초기화
    # ============================================
    local_rank = int(os.environ.get('LOCAL_RANK', 0))
    world_size = int(os.environ.get('WORLD_SIZE', 1))
    rank = int(os.environ.get('RANK', 0))
    
    # PyTorch 분산 초기화
    if not dist.is_initialized():
        dist.init_process_group(backend='nccl')
        torch.cuda.set_device(local_rank)
    
    # 노드 정보
    node_name = socket.gethostname()
    
    # 로깅에 rank 추가
    logging.LoggerAdapter(logging.getLogger(), {'rank': rank})
    
    # ============================================
    # 3. 경로 설정
    # ============================================
    lustre_base = os.environ.get('LUSTRE_BASE', '/lustre')
    experiment_name = os.environ.get(
        'EXPERIMENT_NAME', 
        f'qwen-wikitext-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
    )
    
    # 데이터 경로
    data_path = f"{lustre_base}/data/wikitext-2"
    
    # 출력 경로
    checkpoint_path = f"{lustre_base}/checkpoints/{experiment_name}"
    log_path = f"{lustre_base}/logs/{experiment_name}"
    result_path = f"{lustre_base}/results/{experiment_name}"
    
    print("\n" + "="*70)
    print(f"🚀 Distributed Training Starting")
    print("="*70)
    print(f"📍 Node: {node_name}")
    print(f"🎯 Rank: {rank}/{world_size} (Local Rank: {local_rank})")
    print(f"📂 Dataset: {data_path}")
    print(f"💾 Checkpoints: {checkpoint_path}")
    print(f"📊 Logs: {log_path}")
    print(f"🎯 Results: {result_path}")
    print(f"🔧 Experiment: {experiment_name}")
    print("="*70 + "\n")
    
    # ============================================
    # 4. 디렉토리 생성 (Rank 0만)
    # ============================================
    if rank == 0:
        print(f"[Rank 0] Creating output directories...")
        try:
            os.makedirs(checkpoint_path, exist_ok=True)
            os.makedirs(log_path, exist_ok=True)
            os.makedirs(result_path, exist_ok=True)
            
            # 쓰기 테스트
            test_file = os.path.join(checkpoint_path, ".write_test")
            with open(test_file, "w") as f:
                f.write("test")
            os.remove(test_file)
            print(f"✓ [Rank 0] Output directories created and writable")
            
        except Exception as e:
            print(f"✗ [Rank 0] Error creating directories: {e}")
            raise
    
    # 모든 rank가 디렉토리 생성 대기
    dist.barrier()
    print(f"[Rank {rank}] Synchronized, proceeding...")
    
    # ============================================
    # 5. 모델 및 토크나이저 로드
    # ============================================
    print(f"[Rank {rank}] Loading Qwen2.5-0.5B model...")
    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2.5-0.5B",
        attn_implementation="flash_attention_2",
        torch_dtype=torch.bfloat16,
        cache_dir=TRANSFORMERS_CACHE,
    )
    
    print(f"[Rank {rank}] Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(
        "Qwen/Qwen2.5-0.5B",
        cache_dir=TRANSFORMERS_CACHE,
    )
    tokenizer.pad_token = tokenizer.eos_token
    
    # ============================================
    # 6. 데이터셋 로드 및 전처리
    # ============================================
    print(f"[Rank {rank}] Loading WikiText-2 dataset from {data_path}...")
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"Dataset not found at {data_path}. "
            f"Please ensure FSx Lustre is mounted and synced."
        )
    
    dataset = load_from_disk(data_path)
    train_dataset = dataset["train"]
    
    print(f"[Rank {rank}] Original dataset size: {len(train_dataset)}")
    
    # 빈 텍스트 필터링 (캐시를 로컬에 저장)
    print(f"[Rank {rank}] Filtering empty texts...")
    cache_file_filter = f"{HF_CACHE}/filtered_train_rank{rank}.arrow"
    
    train_dataset = train_dataset.filter(
        lambda x: len(x["text"]) > 0 and not x["text"].isspace(),
        cache_file_name=cache_file_filter,
        desc=f"Filtering (Rank {rank})"
    )
    
    print(f"[Rank {rank}] Filtered dataset size: {len(train_dataset)}")
    
    # 토큰화 (캐시를 로컬에 저장)
    print(f"[Rank {rank}] Tokenizing dataset...")
    cache_file_tokenize = f"{HF_CACHE}/tokenized_train_rank{rank}.arrow"
    
    tokenized_dataset = train_dataset.map(
        lambda x: prepare_dataset(x, tokenizer),
        batched=True,
        remove_columns=train_dataset.column_names,
        desc=f"Tokenizing (Rank {rank})",
        num_proc=4,
        cache_file_name=cache_file_tokenize,
    )
    
    print(f"[Rank {rank}] Tokenization complete. Dataset size: {len(tokenized_dataset)}")
    
    # ============================================
    # 7. 학습 설정
    # ============================================
    print(f"[Rank {rank}] Setting up training configuration...")
    
    training_args = TrainingArguments(
        # 출력 경로
        output_dir=checkpoint_path,
        logging_dir=log_path,
        
        # 학습 설정
        num_train_epochs=2,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=2,
        
        # 옵티마이저
        learning_rate=2e-5,
        warmup_steps=100,
        weight_decay=0.01,
        
        # 로깅
        logging_steps=10,
        logging_first_step=True,
        report_to="tensorboard",
        
        # 체크포인트
        save_strategy="epoch",
        save_total_limit=2,
        
        # 분산 학습
        ddp_backend="nccl",
        local_rank=local_rank,
        
        # 혼합 정밀도
        bf16=True,
        
        # 기타
        dataloader_num_workers=4,
        dataloader_pin_memory=True,
    )
    
    # Trainer 초기화
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )
    
    # ============================================
    # 8. 학습 시작
    # ============================================
    print("\n" + "="*70)
    print(f"🏋️  [Rank {rank}] Starting Distributed Training")
    print("="*70)
    print(f"📊 Total Samples: {len(tokenized_dataset)}")
    print(f"🔢 Batch Size per Device: {training_args.per_device_train_batch_size}")
    print(f"🔄 Gradient Accumulation Steps: {training_args.gradient_accumulation_steps}")
    print(f"🌐 World Size: {world_size}")
    print(f"📈 Effective Batch Size: {training_args.per_device_train_batch_size * training_args.gradient_accumulation_steps * world_size}")
    print(f"📝 Logs: tensorboard --logdir={log_path}")
    print("="*70 + "\n")
    
    # 학습 실행
    trainer.train()
    
    # ============================================
    # 9. 학습 완료 및 저장 (Rank 0만)
    # ============================================
    if rank == 0:
        print("\n" + "="*70)
        print("✅ Training Completed Successfully!")
        print("="*70)
        
        # 최종 모델 저장
        print(f"💾 Saving final model to {result_path}...")
        trainer.save_model(result_path)
        tokenizer.save_pretrained(result_path)
        
        # 학습 정보 저장
        info_file = os.path.join(result_path, "training_info.txt")
        with open(info_file, "w") as f:
            f.write(f"Experiment Name: {experiment_name}\n")
            f.write(f"Dataset: WikiText-2\n")
            f.write(f"Model: Qwen2.5-0.5B\n")
            f.write(f"Nodes: {world_size}\n")
            f.write(f"Total Samples: {len(tokenized_dataset)}\n")
            f.write(f"Epochs: {training_args.num_train_epochs}\n")
            f.write(f"Batch Size (per device): {training_args.per_device_train_batch_size}\n")
            f.write(f"Gradient Accumulation: {training_args.gradient_accumulation_steps}\n")
            f.write(f"Learning Rate: {training_args.learning_rate}\n")
            f.write(f"Completed: {datetime.now().isoformat()}\n")
        
        print(f"✓ Model saved to: {result_path}")
        print(f"✓ Training info saved to: {info_file}")
        print(f"📊 View logs: tensorboard --logdir={log_path}")
        print(f"📤 Results will sync to S3 (if configured)")
        print("="*70 + "\n")
    
    # 최종 동기화
    dist.barrier()
    
    print(f"[Rank {rank}] Training job finished successfully! 🎉")

if __name__ == "__main__":
    main()