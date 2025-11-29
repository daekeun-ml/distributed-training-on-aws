import os
import socket
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_from_disk
from datetime import datetime

os.makedirs("/root/.triton/autotune", exist_ok=True)

def prepare_dataset(examples, tokenizer, max_length=512):
    """텍스트를 토큰화"""
    tokenized = tokenizer(
        examples["text"],
        truncation=True,
        max_length=max_length,
        padding="max_length",
        return_tensors=None
    )
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized

def main():
    # 분산 환경 정보
    local_rank = int(os.environ.get('LOCAL_RANK', 0))
    world_size = int(os.environ.get('WORLD_SIZE', 1))
    rank = int(os.environ.get('RANK', 0))
    
    # 환경변수에서 노드 정보 가져오기
    node_name = os.environ.get('NODE_NAME', socket.gethostname())
    
    # FSx Lustre 경로 설정
    lustre_base = os.environ.get('LUSTRE_BASE', '/lustre')
    experiment_name = os.environ.get('EXPERIMENT_NAME', f'qwen-wikitext-{datetime.now().strftime("%Y%m%d-%H%M%S")}')
    
    # 경로 정의
    data_path = f"{lustre_base}/data/wikitext-2"
    checkpoint_path = f"{lustre_base}/checkpoints/{experiment_name}"
    log_path = f"{lustre_base}/logs/{experiment_name}"
    result_path = f"{lustre_base}/results/{experiment_name}"
    
    print(f"🚀 [Rank {rank}/{world_size}] {node_name} GPU {local_rank} - Starting...")
    print(f"📂 [Rank {rank}] Dataset: {data_path}")
    print(f"💾 [Rank {rank}] Checkpoints: {checkpoint_path}")
    print(f"📊 [Rank {rank}] Logs: {log_path}")
    print(f"🎯 [Rank {rank}] Results: {result_path}")
    
    # 디렉토리 생성 (rank 0만)
    if rank == 0:
        os.makedirs(checkpoint_path, exist_ok=True)
        os.makedirs(log_path, exist_ok=True)
        os.makedirs(result_path, exist_ok=True)
    
    # 모델 및 토크나이저 로드
    print(f"[Rank {rank}] Loading Qwen 0.5B...")
    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2.5-0.5B",
        attn_implementation="flash_attention_2",
        torch_dtype=torch.bfloat16,
    )
    
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")
    tokenizer.pad_token = tokenizer.eos_token
    
    # FSx Lustre에서 WikiText-2 로드
    print(f"[Rank {rank}] Loading WikiText-2 from FSx Lustre...")
    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"Dataset not found at {data_path}. "
            f"Please ensure FSx Lustre is synced with S3."
        )
    
    dataset = load_from_disk(data_path)
    train_dataset = dataset["train"]
    
    # 빈 텍스트 제거
    print(f"[Rank {rank}] Filtering empty texts...")
    train_dataset = train_dataset.filter(
        lambda x: len(x["text"]) > 0 and not x["text"].isspace()
    )
    
    print(f"[Rank {rank}] Tokenizing dataset... (Total samples: {len(train_dataset)})")
    tokenized_dataset = train_dataset.map(
        lambda x: prepare_dataset(x, tokenizer),
        batched=True,
        remove_columns=train_dataset.column_names,
        desc="Tokenizing",
        num_proc=4
    )
    
    print(f"[Rank {rank}] Setting up DeepSpeed training...")
    
    training_args = TrainingArguments(
        output_dir=checkpoint_path,
        logging_dir=log_path,
        num_train_epochs=2,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=2,
        logging_steps=10,
        bf16=True,
        learning_rate=2e-5,
        warmup_steps=10,
        save_strategy="epoch",
        save_total_limit=2,
        report_to="tensorboard",
        logging_first_step=True,
        deepspeed="ds_config.json",
        ddp_backend="nccl",
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )
    
    print(f"🏋️  [Rank {rank}] Starting distributed training on WikiText-2...")
    print(f"📈 [Rank {rank}] TensorBoard logs: {log_path}")
    
    trainer.train()
    
    if rank == 0:
        print("\n" + "="*60)
        print("✅ Multi-node DeepSpeed training completed!")
        print("🎉 WikiText-2 training successful!")
        print("="*60)
        
        # 최종 모델 저장
        print(f"💾 Saving final model to {result_path}...")
        trainer.save_model(result_path)
        tokenizer.save_pretrained(result_path)
        
        # 학습 정보 저장
        with open(f"{result_path}/training_info.txt", "w") as f:
            f.write(f"Experiment: {experiment_name}\n")
            f.write(f"Dataset: WikiText-2\n")
            f.write(f"Nodes: {world_size}\n")
            f.write(f"Total samples: {len(train_dataset)}\n")
            f.write(f"Epochs: 2\n")
            f.write(f"Completed: {datetime.now()}\n")
        
        print(f"✅ Final model saved to: {result_path}")
        print(f"📤 Results will sync to S3: s3://your-bucket/results/{experiment_name}/")
        print(f"📊 View logs: tensorboard --logdir={log_path}")

if __name__ == "__main__":
    main()