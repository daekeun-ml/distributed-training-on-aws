# 3. 분산 학습 실행

> 💡 **목표:** 컨테이너 기반 분산 학습 작업을 Slurm으로 실행합니다.

⏱️ **예상 소요 시간:** 40-60분

## 목차

- [개요](#개요)
- [스토리지 전략 이해](#스토리지-전략-이해)
- [3.1 컨테이너 이미지 준비](#31-컨테이너-이미지-준비)
  - [3.1.1 ECR 로그인](#311-ecr-로그인)
  - [3.1.2 Docker 이미지 Pull](#312-docker-이미지-pull)
  - [3.1.3 Enroot SQSH 포맷 변환](#313-enroot-sqsh-포맷-변환)
- [3.2 분산 학습 작업 제출](#32-분산-학습-작업-제출)
  - [3.2.1 Sbatch 스크립트 작성](#321-sbatch-스크립트-작성)
  - [3.2.2 작업 제출](#322-작업-제출)
  - [3.2.3 작업 모니터링](#323-작업-모니터링)
- [3.3 학습 결과 확인](#33-학습-결과-확인)
  - [3.3.1 로컬 결과 확인](#331-로컬-결과-확인)
  - [3.3.2 S3 동기화 확인](#332-s3-동기화-확인)
- [다음 단계](#다음-단계)

---

## 개요

이 문서에서는 다음 작업을 수행합니다:

- ✅ ECR에서 커스텀 DLC 이미지를 Enroot SQSH 포맷으로 변환
- ✅ DeepSpeed를 사용한 분산 학습 스크립트 작성
- ✅ Slurm + Pyxis로 멀티 노드 학습 실행
- ✅ 학습 결과 및 S3 동기화 확인

---

## 3.1 컨테이너 이미지 준비

Head Node에서 ECR의 커스텀 DLC 이미지를 Enroot SQSH 포맷으로 변환합니다.

> 💡 **왜 SQSH 포맷인가요?**
> - Enroot는 squashfs 압축 포맷 사용
> - 읽기 전용, 고속, 공유 가능
> - 여러 노드가 동시에 안전하게 읽을 수 있음

### 3.1.1 ECR 로그인

Head Node에서 ECR에 로그인합니다:

```bash
# 환경 변수 로드
source ~/pcluster-env.sh

# ECR 로그인
aws ecr get-login-password --region ${AWS_REGION} | \
  docker login --username AWS --password-stdin ${ECR_REPO_URI}
```

**예상 출력:**
```
WARNING! Your password will be stored unencrypted in /home/ubuntu/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

---

### 3.1.2 Docker 이미지 Pull

HeadNode에 접속해 ECR에서 커스텀 DLC 이미지를 가져옵니다:
2번 모듈(02-pcluster-deployment.md) 에서 push 했던 ECR

```bash
export AWS_REGION=us-east-1
export ECR_REPO_NAME=pytorch-training-custom

# 리포지토리 URI 저장
export ECR_REPO_URI=$(aws ecr describe-repositories \
  --repository-names ${ECR_REPO_NAME} \
  --region ${AWS_REGION} \
  --query 'repositories[0].repositoryUri' \
  --output text)

export IMAGE_TAG=latest

export TRAINING_IMAGE_URI=${ECR_REPO_URI}:${IMAGE_TAG}

aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO_URI}

docker pull ${TRAINING_IMAGE_URI}
```

**예상 출력:**
```
Login Succeeded

latest: Pulling from pytorch-training-custom
Digest: sha256:1234567890abcdef...
Status: Downloaded newer image for 123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-training-custom:latest
```

> ⏱️ **예상 소요 시간:** 약 5-10분 (이미지 크기 ~15-20GB)

#### 이미지 확인

```bash
# 로컬 Docker 이미지 확인
docker images | grep pytorch-training-custom
```

**예상 출력:**
```
123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-training-custom:latest    abc123def456     31.1GB         10.4GB
```

---

### 3.1.3 Enroot SQSH 포맷 변환

부트스트랩 스크립트로 생성된 **헬퍼 스크립트**를 사용하여 Docker 이미지를 Enroot SQSH 포맷으로 변환합니다.

> 💡 **변환 프로세스:**
> 1. Docker 이미지 → Enroot import
> 2. `/fsx/containers/images/`에 `.sqsh` 파일로 저장 (공유)
> 3. 모든 Compute Node가 이 파일을 읽어서 사용

#### 변환 실행

```bash
# import-container.sh 헬퍼 스크립트 사용
sudo bash /fsx/import-container.sh ${TRAINING_IMAGE_URI} pytorch-training
```

**예상 출력:**
```
Importing container image...
Source: 123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-training-custom:latest
Output: pytorch-training.sqsh
[INFO] Fetching image

d43920b07d21de366b78471c16147bd2a28063ae40c4ef9c9ca02a2a6738146d

[INFO] Extracting image content...
[INFO] Creating squashfs filesystem...

Parallel mksquashfs: Using 32 processors
Creating 4.0 filesystem on /fsx/containers/images/pytorch-training.sqsh, block size 131072.
[===============================================================================================================|] 250989/250989 100%

Exportable Squashfs 4.0 filesystem, lzo compressed, data block size 131072
        uncompressed data, compressed metadata, compressed fragments,
        compressed xattrs, compressed ids
        duplicates are removed
Filesystem size 16766768.27 Kbytes (16373.80 Mbytes)
        90.14% of uncompressed filesystem size (18600340.20 Kbytes)
Inode table size 1663087 bytes (1624.11 Kbytes)
        32.07% of uncompressed inode table size (5185940 bytes)
Directory table size 1567010 bytes (1530.28 Kbytes)
        41.36% of uncompressed directory table size (3788590 bytes)
Number of duplicate files found 11488
Number of inodes 139377
Number of files 116377
Number of fragments 9168
Number of symbolic links 10083
Number of device nodes 0
Number of fifo nodes 0
Number of socket nodes 0
Number of directories 12917
Number of ids (unique uids + gids) 1
Number of uids 1
        root (0)
Number of gids 1
        root (0)

✓ Import completed!

Available container images:
-rw-r--r-- 1 root root 16G Nov 29 20:06 /fsx/containers/images/pytorch-training.sqsh
```

> ⏱️ **예상 소요 시간:** 약 10-15분 (이미지 크기와 압축 속도에 따라)

#### 변환된 이미지 확인

```bash
# SQSH 이미지 확인
ls -lh /fsx/containers/images/

# Enroot로 이미지 목록 확인
enroot list
```

**예상 출력:**
```
total 17G
-rw-r--r-- 1 root root 16G Nov 29 20:06 pytorch-training.sqsh
```

#### 환경 변수 저장

나중에 사용하기 위해 컨테이너 이미지 경로를 환경 변수로 저장합니다:

```bash
export CONTAINER_IMAGE=/fsx/containers/images/pytorch-training.sqsh

echo "Container Image: ${CONTAINER_IMAGE}"
```

---

## 3.2 분산 학습 작업 제출

DeepSpeed를 사용한 분산 학습 작업을 Slurm으로 제출합니다.

### 3.2.1 Sbatch 스크립트 작성

#### 학습 스크립트 이해

먼저 컨테이너에 포함된 학습 스크립트의 동작을 이해합니다:

> 📁 **학습 스크립트:** `/workspace/train_distributed_deepspeed.py` (컨테이너 내부)
> - 소스 코드: [examples/containers/pytorch/train_distributed_deepspeed.py](../examples/containers/pytorch/train_distributed_deepspeed.py)

**주요 기능:**
- Qwen 2.5-0.5B 모델 사용
- WikiText-2 데이터셋 로드 (`/lustre/data/wikitext-2/`)
- DeepSpeed로 분산 학습
- 체크포인트 자동 저장 (`/lustre/checkpoints/`)
- TensorBoard 로그 (`/lustre/logs/`)
- 최종 모델 저장 (`/lustre/results/`)

**스토리지 경로 (환경 변수로 제어):**
```python
lustre_base = os.environ.get('LUSTRE_BASE', '/lustre')
experiment_name = os.environ.get('EXPERIMENT_NAME', f'qwen-wikitext-{timestamp}')

data_path = f"{lustre_base}/data/wikitext-2"
checkpoint_path = f"{lustre_base}/checkpoints/{experiment_name}"
log_path = f"{lustre_base}/logs/{experiment_name}"
result_path = f"{lustre_base}/results/{experiment_name}"
```

**S3 자동 동기화:**
- `/lustre/checkpoints/` → `s3://${S3_BUCKET_NAME}/checkpoints/` (AutoExport)
- `/lustre/logs/` → `s3://${S3_BUCKET_NAME}/logs/` (AutoExport)
- `/lustre/results/` → `s3://${S3_BUCKET_NAME}/results/` (AutoExport)

---

#### Sbatch 스크립트 생성

분산 학습을 위한 Slurm 배치 스크립트를 작성합니다:

```bash
# Experiment 이름 설정
export EXPERIMENT_NAME=qwen-wikitext-$(date +%Y%m%d-%H%M%S)

# Sbatch 스크립트 생성
cat > train-distributed.sbatch << 'EOF'
#!/bin/bash
#SBATCH --job-name=distributed-training
#SBATCH --partition=compute-gpu
#SBATCH --nodes=2                      # 2개 노드 사용
#SBATCH --ntasks-per-node=1            # 노드당 1개 태스크 (DeepSpeed launcher)
#SBATCH --gpus-per-node=1              # 노드당 1개 GPU (g5.8xlarge)
#SBATCH --time=02:00:00                # 최대 2시간
#SBATCH --output=%x-%j.out             #lustre에 로그를 저장할거라면 /lustre/logs/%x-%j.out
#SBATCH --error=%x-%j.err              #lustre에 로그를 저장할거라면 /lustre/logs/%x-%j.err

# 환경 변수 설정
export EXPERIMENT_NAME=${EXPERIMENT_NAME:-qwen-wikitext-default}
export LUSTRE_BASE=/lustre
export CONTAINER_IMAGE="/fsx/containers/images/pytorch-training.sqsh"

# Master 노드 정보
export MASTER_ADDR=$(scontrol show hostname $SLURM_NODELIST | head -n 1)
export MASTER_PORT=29500

# NCCL 설정
export NCCL_DEBUG=INFO
export FI_PROVIDER=efa
export NCCL_PROTO=simple
export NCCL_SOCKET_IFNAME=ens5
export GLOO_SOCKET_IFNAME=ens5
export NCCL_IB_DISABLE=1

# DeepSpeed 설정
export DEEPSPEED_CONFIG=/workspace/ds_config.json

echo "=========================================="
echo "Job ID: $SLURM_JOB_ID"
echo "Job Name: $SLURM_JOB_NAME"
echo "Nodes: $SLURM_JOB_NUM_NODES"
echo "Node List: $SLURM_NODELIST"
echo "Master: $MASTER_ADDR:$MASTER_PORT"
echo "GPUs per node: $SLURM_GPUS_PER_NODE"
echo "Experiment: $EXPERIMENT_NAME"
echo "Container: $CONTAINER_IMAGE"
echo "=========================================="

srun --container-image=${CONTAINER_IMAGE} \
     --container-mounts=/dev/infiniband:/dev/infiniband,/lustre:/lustre,/fsx:/fsx \
     --container-writable \
     bash -c "
     torchrun \
       --nproc_per_node=1 \
       --nnodes=${SLURM_JOB_NUM_NODES} \
       --node_rank=\${SLURM_PROCID} \
       --master_addr=${MASTER_ADDR} \
       --master_port=${MASTER_PORT} \
       --rdzv_backend=c10d \
       --rdzv_endpoint=${MASTER_ADDR}:${MASTER_PORT} \
       /workspace/train_distributed_deepspeed.py
     "


echo "=========================================="
echo "Training completed at $(date)"
echo "Results saved to: ${LUSTRE_BASE}/results/${EXPERIMENT_NAME}/"
echo "Checkpoints: ${LUSTRE_BASE}/checkpoints/${EXPERIMENT_NAME}/"
echo "=========================================="

EOF

echo "✅ Sbatch script created: train-distributed.sbatch"
```

**스크립트 주요 구성:**

| 섹션 | 설명 |
|------|------|
| **SBATCH 지시자** | Slurm 리소스 요청 (노드, GPU, 시간 등) |
| **환경 변수** | 실험 이름, 경로, NCCL 설정 |
| **Master 노드 설정** | 분산 학습을 위한 마스터 주소 |
| **srun + Pyxis** | 컨테이너 실행 및 마운트 |
| **deepspeed launcher** | 멀티 노드 분산 학습 시작 |

**컨테이너 마운트 설명:**
```bash
--container-mounts=/lustre:/lustre,/fsx:/fsx
```
- Host의 `/lustre` → 컨테이너의 `/lustre` (데이터, 결과)
- Host의 `/fsx` → 컨테이너의 `/fsx` (코드, 설정)

**DeepSpeed 파라미터:**
```bash
--num_nodes=${SLURM_JOB_NUM_NODES}     # Slurm이 할당한 노드 수
--num_gpus=${SLURM_GPUS_PER_NODE}      # 노드당 GPU 수
--master_addr=${MASTER_ADDR}           # 첫 번째 노드 주소
--master_port=${MASTER_PORT}           # 통신 포트
--node_rank=${SLURM_NODEID}            # 현재 노드 순번
```

---

### 3.2.2 작업 제출

Sbatch 스크립트를 Slurm에 제출합니다:

```bash
# 작업 제출
sbatch train-distributed.sbatch
```

**예상 출력:**
```
Submitted batch job 2
```

---
### 3.2.3 작업 모니터링

#### 작업 큐 확인

```bash
# 작업 상태 확인
export JOB_ID=$(squeue -u $USER -h -o %i | head -n 1)
[ -z "$JOB_ID" ] && read -p "Enter JOB_ID: " JOB_ID
echo "JOB_ID: $JOB_ID"

squeue

scontrol show job ${JOB_ID}
```

#### 실시간 로그 확인

```bash
# 표준 출력 로그 (실시간)
tail -f distributed-training-${JOB_ID}.out
```

**예상 로그 출력:**
```
$ tail -f distributed-training-12.out
Job ID: 12
Job Name: distributed-training
Nodes: 2
Node List: compute-gpu-st-distributed-ml-[1-2]
Master: compute-gpu-st-distributed-ml-1:29500
GPUs per node: 1
Experiment: qwen-wikitext-20251129-201659
Container: /fsx/containers/images/pytorch-training.sqsh
==========================================
directory 임시 조치

⚠ /scratch not found, using /tmp for caching
📦 Cache directories:
   HF_DATASETS_CACHE: /tmp/hf_cache_1000
   TRANSFORMERS_CACHE: /tmp/transformers_cache_1000
   TRITON_CACHE_DIR: /tmp/triton_cache_1000

======================================================================
🚀 Distributed Training Starting
======================================================================
📍 Node: compute-gpu-st-distributed-ml-1
🎯 Rank: 0/2 (Local Rank: 0)
📂 Dataset: /lustre/data/wikitext-2
💾 Checkpoints: /lustre/checkpoints/qwen-wikitext-20251129-201659
📊 Logs: /lustre/logs/qwen-wikitext-20251129-201659
🎯 Results: /lustre/results/qwen-wikitext-20251129-201659
🔧 Experiment: qwen-wikitext-20251129-201659
======================================================================

[Rank 0] Creating output directories...
✓ [Rank 0] Output directories created and writable
⚠ /scratch not found, using /tmp for caching
📦 Cache directories:
   HF_DATASETS_CACHE: /tmp/hf_cache_1000
   TRANSFORMERS_CACHE: /tmp/transformers_cache_1000
   TRITON_CACHE_DIR: /tmp/triton_cache_1000

======================================================================
🚀 Distributed Training Starting
======================================================================
📍 Node: compute-gpu-st-distributed-ml-2
🎯 Rank: 1/2 (Local Rank: 0)
📂 Dataset: /lustre/data/wikitext-2
💾 Checkpoints: /lustre/checkpoints/qwen-wikitext-20251129-201659
📊 Logs: /lustre/logs/qwen-wikitext-20251129-201659
🎯 Results: /lustre/results/qwen-wikitext-20251129-201659
🔧 Experiment: qwen-wikitext-20251129-201659
======================================================================

compute-gpu-st-distributed-ml-1:7614:7614 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ens5
compute-gpu-st-distributed-ml-1:7614:7614 [0] NCCL INFO Bootstrap : Using ens5:10.1.94.228<0>
compute-gpu-st-distributed-ml-1:7614:7614 [0] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:7614:7614 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
compute-gpu-st-distributed-ml-2:7070:7070 [0] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:7070:7070 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ens5
compute-gpu-st-distributed-ml-2:7070:7070 [0] NCCL INFO Bootstrap : Using ens5:10.1.113.246<0>
compute-gpu-st-distributed-ml-2:7070:7070 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin symbol (>= v5). ncclCollNetPlugin symbols v4 and lower are not supported.
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.12.1-aws
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Using Libfabric version 1.22
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Using CUDA driver version 12080
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Setting FI_EFA_FORK_SAFE environment variable to 1
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Setting NCCL_NVLSTREE_MAX_CHUNKSIZE to 512KiB
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Setting NCCL_NVLS_CHUNKSIZE to 512KiB
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Internode latency set at 150.0 us
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Creating one domain per process
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Using transport protocol SENDRECV
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Selected Provider is efa (found 1 nics)
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Could not disable CUDA API usage for HMEM, disabling GDR
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Setting FI_OPT_EFA_SENDRECV_IN_ORDER_ALIGNED_128_BYTES not supported.
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO Using network AWS Libfabric
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO DMA-BUF is available on GPU device 0
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO ncclCommInitRankConfig comm 0x573f9cb382e0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 1e0 commId 0x1ce724326e09a7e5 - Init START
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin symbol (>= v5). ncclCollNetPlugin symbols v4 and lower are not supported.
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.12.1-aws
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Using Libfabric version 1.22
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Using CUDA driver version 12080
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Setting FI_EFA_FORK_SAFE environment variable to 1
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Setting NCCL_NVLSTREE_MAX_CHUNKSIZE to 512KiB
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Setting NCCL_NVLS_CHUNKSIZE to 512KiB
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Internode latency set at 150.0 us
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Creating one domain per process
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Using transport protocol SENDRECV
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Selected Provider is efa (found 1 nics)
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Could not disable CUDA API usage for HMEM, disabling GDR
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Setting FI_OPT_EFA_SENDRECV_IN_ORDER_ALIGNED_128_BYTES not supported.
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO Using network AWS Libfabric
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO DMA-BUF is available on GPU device 0
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO ncclCommInitRankConfig comm 0x60630f7f62f0 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 1e0 commId 0x1ce724326e09a7e5 - Init START
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO Bootstrap timings total 0.040572 (create 0.000033, send 0.000142, recv 0.039682, ring 0.000075, delay 0.000000)
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO Bootstrap timings total 0.001249 (create 0.000031, send 0.000262, recv 0.000439, ring 0.000280, delay 0.000000)
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO comm 0x573f9cb382e0 rank 0 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO Channel 00/02 : 0 1
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO Channel 01/02 : 0 1
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO P2P Chunksize set to 131072
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO comm 0x60630f7f62f0 rank 1 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] 0/-1/-1->1->-1
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO P2P Chunksize set to 131072
compute-gpu-st-distributed-ml-1:7614:7692 [0] NCCL INFO [Proxy Service] Device 0 CPU core 9
compute-gpu-st-distributed-ml-2:7070:7147 [0] NCCL INFO [Proxy Service] Device 0 CPU core 22
compute-gpu-st-distributed-ml-2:7070:7148 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 11
compute-gpu-st-distributed-ml-1:7614:7693 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 12
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO NCCL_PROTO set by environment to simple
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO NCCL_PROTO set by environment to simple
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO CC Off, Multi-GPU CC Off, workFifoBytes 1048576
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO ncclCommInitRankConfig comm 0x573f9cb382e0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 1e0 commId 0x1ce724326e09a7e5 - Init COMPLETE
compute-gpu-st-distributed-ml-1:7614:7691 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 0 nranks 2 total 0.21 (kernels 0.14, alloc 0.01, bootstrap 0.04, allgathers 0.00, topo 0.00, graphs 0.00, connections 0.00, rest 0.00)
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO ncclCommInitRankConfig comm 0x60630f7f62f0 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 1e0 commId 0x1ce724326e09a7e5 - Init COMPLETE
compute-gpu-st-distributed-ml-2:7070:7146 [0] NCCL INFO Init timings - ncclCommInitRankConfig: rank 1 nranks 2 total 0.17 (kernels 0.14, alloc 0.01, bootstrap 0.00, allgathers 0.00, topo 0.00, graphs 0.00, connections 0.00, rest 0.00)
compute-gpu-st-distributed-ml-1:7614:7695 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 11
compute-gpu-st-distributed-ml-1:7614:7692 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-2:7070:7150 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 7
compute-gpu-st-distributed-ml-2:7070:7147 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-1:7614:7694 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [receive] via NET/AWS Libfabric/0
compute-gpu-st-distributed-ml-1:7614:7692 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-1:7614:7694 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [receive] via NET/AWS Libfabric/0
compute-gpu-st-distributed-ml-1:7614:7692 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-1:7614:7694 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [send] via NET/AWS Libfabric/0
compute-gpu-st-distributed-ml-1:7614:7692 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-1:7614:7694 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [send] via NET/AWS Libfabric/0
compute-gpu-st-distributed-ml-2:7070:7149 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [receive] via NET/AWS Libfabric/0
compute-gpu-st-distributed-ml-2:7070:7147 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-2:7070:7149 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [receive] via NET/AWS Libfabric/0
compute-gpu-st-distributed-ml-2:7070:7147 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-2:7070:7149 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [send] via NET/AWS Libfabric/0
compute-gpu-st-distributed-ml-2:7070:7147 [0] NCCL INFO NET/OFI Global registrations supported
compute-gpu-st-distributed-ml-2:7070:7149 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [send] via NET/AWS Libfabric/0
compute-gpu-st-distributed-ml-1:7614:7694 [0] NCCL INFO Connected all rings
compute-gpu-st-distributed-ml-2:7070:7149 [0] NCCL INFO Connected all rings
[Rank 0] Synchronized, proceeding...
[Rank 0] Loading Qwen2.5-0.5B model...
[Rank 1] Synchronized, proceeding...
[Rank 1] Loading Qwen2.5-0.5B model...
[Rank 1] Loading tokenizer...
[Rank 0] Loading tokenizer...
[Rank 1] Loading WikiText-2 dataset from /lustre/data/wikitext-2...
[Rank 1] Original dataset size: 36718
[Rank 1] Filtering empty texts...
[Rank 0] Loading WikiText-2 dataset from /lustre/data/wikitext-2...
[Rank 0] Original dataset size: 36718
[Rank 0] Filtering empty texts...
[Rank 1] Filtered dataset size: 23767
[Rank 1] Tokenizing dataset...
[Rank 0] Filtered dataset size: 23767
[Rank 0] Tokenizing dataset...
[Rank 1] Tokenization complete. Dataset size: 23767
[Rank 1] Setting up training configuration...
[Rank 0] Tokenization complete. Dataset size: 23767
[Rank 0] Setting up training configuration...

======================================================================
🏋️  [Rank 1] Starting Distributed Training
======================================================================
📊 Total Samples: 23767
🔢 Batch Size per Device: 4
🔄 Gradient Accumulation Steps: 2
🌐 World Size: 2
📈 Effective Batch Size: 16
📝 Logs: tensorboard --logdir=/lustre/logs/qwen-wikitext-20251129-201659
======================================================================


======================================================================
🏋️  [Rank 0] Starting Distributed Training
======================================================================
📊 Total Samples: 23767
🔢 Batch Size per Device: 4
🔄 Gradient Accumulation Steps: 2
🌐 World Size: 2
📈 Effective Batch Size: 16
📝 Logs: tensorboard --logdir=/lustre/logs/qwen-wikitext-20251129-201659
======================================================================

compute-gpu-st-distributed-ml-2:7070:7351 [0] NCCL INFO Connected binomial trees
compute-gpu-st-distributed-ml-1:7614:7888 [0] NCCL INFO Connected binomial trees
compute-gpu-st-distributed-ml-1:7614:8102 [0] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-2:7070:7561 [0] NCCL INFO Connected all trees
{'loss': 7.4095, 'grad_norm': 3120.0, 'learning_rate': 0.0, 'epoch': 0.0}
{'loss': 6.3676, 'grad_norm': 2112.0, 'learning_rate': 1.8000000000000001e-06, 'epoch': 0.01}
{'loss': 1.7161, 'grad_norm': 18.0, 'learning_rate': 3.8000000000000005e-06, 'epoch': 0.01}
{'loss': 0.637, 'grad_norm': 6.4375, 'learning_rate': 5.8e-06, 'epoch': 0.02}
{'loss': 0.6704, 'grad_norm': 4.8125, 'learning_rate': 7.800000000000002e-06, 'epoch': 0.03}
{'loss': 0.7214, 'grad_norm': 4.5625, 'learning_rate': 9.800000000000001e-06, 'epoch': 0.03}
{'loss': 0.5843, 'grad_norm': 3.71875, 'learning_rate': 1.18e-05, 'epoch': 0.04}
{'loss': 0.7451, 'grad_norm': 3.25, 'learning_rate': 1.38e-05, 'epoch': 0.05}
{'loss': 0.5315, 'grad_norm': 3.484375, 'learning_rate': 1.58e-05, 'epoch': 0.05}
{'loss': 0.5753, 'grad_norm': 2.765625, 'learning_rate': 1.7800000000000002e-05, 'epoch': 0.06}
{'loss': 0.5538, 'grad_norm': 5.5, 'learning_rate': 1.98e-05, 'epoch': 0.07}
{'loss': 0.553, 'grad_norm': 3.1875, 'learning_rate': 1.993732590529248e-05, 'epoch': 0.07}
{'loss': 0.6442, 'grad_norm': 2.859375, 'learning_rate': 1.9867688022284122e-05, 'epoch': 0.08}
{'loss': 0.5673, 'grad_norm': 2.8125, 'learning_rate': 1.979805013927577e-05, 'epoch': 0.09}
{'loss': 0.5269, 'grad_norm': 3.125, 'learning_rate': 1.972841225626741e-05, 'epoch': 0.09}

...

{'loss': 0.5743, 'grad_norm': 2.59375, 'learning_rate': 1.0396935933147634e-05, 'epoch': 1.0}
{'loss': 0.5684, 'grad_norm': 3.09375, 'learning_rate': 1.0327298050139276e-05, 'epoch': 1.0}
{'loss': 0.5329, 'grad_norm': 2.46875, 'learning_rate': 1.0257660167130921e-05, 'epoch': 1.01}
{'loss': 0.4766, 'grad_norm': 2.53125, 'learning_rate': 1.0188022284122564e-05, 'epoch': 1.02}
{'loss': 0.5193, 'grad_norm': 3.328125, 'learning_rate': 1.0118384401114208e-05, 'epoch': 1.02}
{'loss': 0.5086, 'grad_norm': 2.703125, 'learning_rate': 1.0048746518105849e-05, 'epoch': 1.03}
{'loss': 0.5069, 'grad_norm': 3.1875, 'learning_rate': 9.979108635097493e-06, 'epoch': 1.04}
{'loss': 0.4974, 'grad_norm': 3.03125, 'learning_rate': 9.909470752089138e-06, 'epoch': 1.04}
{'loss': 0.5145, 'grad_norm': 2.703125, 'learning_rate': 9.83983286908078e-06, 'epoch': 1.05}

...

{'loss': 0.5762, 'grad_norm': 2.765625, 'learning_rate': 1.601671309192201e-07, 'epoch': 1.99}
{'loss': 0.4222, 'grad_norm': 2.46875, 'learning_rate': 9.052924791086352e-08, 'epoch': 1.99}
{'loss': 0.5291, 'grad_norm': 2.65625, 'learning_rate': 2.0891364902506967e-08, 'epoch': 2.0}
{'train_runtime': 2233.4294, 'train_samples_per_second': 21.283, 'train_steps_per_second': 1.331, 'train_loss': 0.562542522418868, 'epoch': 2.0}

======================================================================
✅ Training Completed Successfully!
======================================================================
💾 Saving final model to /lustre/results/qwen-wikitext-20251129-201659...
✓ Model saved to: /lustre/results/qwen-wikitext-20251129-201659
✓ Training info saved to: /lustre/results/qwen-wikitext-20251129-201659/training_info.txt
📊 View logs: tensorboard --logdir=/lustre/logs/qwen-wikitext-20251129-201659
📤 Results will sync to S3 (if configured)
======================================================================

[Rank 0] Training job finished successfully! 🎉
[Rank 1] Training job finished successfully! 🎉
compute-gpu-st-distributed-ml-2:7070:11027 [0] NCCL INFO misc/socket.cc:47 -> 3
compute-gpu-st-distributed-ml-2:7070:11027 [0] NCCL INFO misc/socket.cc:58 -> 3
compute-gpu-st-distributed-ml-2:7070:11027 [0] NCCL INFO misc/socket.cc:781 -> 3
compute-gpu-st-distributed-ml-2:7070:7147 [0] NCCL INFO misc/socket.cc:832 -> 3
compute-gpu-st-distributed-ml-1:7614:9432 [0] NCCL INFO misc/socket.cc:47 -> 3
compute-gpu-st-distributed-ml-1:7614:9432 [0] NCCL INFO misc/socket.cc:58 -> 3
compute-gpu-st-distributed-ml-1:7614:9432 [0] NCCL INFO misc/socket.cc:781 -> 3
compute-gpu-st-distributed-ml-1:7614:7692 [0] NCCL INFO misc/socket.cc:832 -> 3
compute-gpu-st-distributed-ml-2:7070:11027 [0] NCCL INFO comm 0x60630f7f62f0 rank 1 nranks 2 cudaDev 0 busId 1e0 - Abort COMPLETE
compute-gpu-st-distributed-ml-1:7614:9432 [0] NCCL INFO comm 0x573f9cb382e0 rank 0 nranks 2 cudaDev 0 busId 1e0 - Abort COMPLETE
==========================================
Training completed at Sat Nov 29 22:08:07 UTC 2025
Results saved to: /lustre/results/qwen-wikitext-20251129-201659/
Checkpoints: /lustre/checkpoints/qwen-wikitext-20251129-201659/
==========================================

```

#### 트러블슈팅
아래와 같은 권한 문제로 학습이 중단되면 user를 `ubuntu`로 바꾸거나 chmod로 권한 변경 후 재시도합니다.
```bash
[Rank 0] Creating output directories...
✗ [Rank 0] Error creating directories: [Errno 13] Permission denied: '/lustre/checkpoints/qwen-wikitext-20251202-142643'
```

```bash
# user 변경
sudo chown -R $USER:$USER /lustre
```

### 3.3.1 로컬 결과 확인

#### 체크포인트 확인

```bash
# 체크포인트 디렉토리 확인
ls -lh /lustre/checkpoints/${EXPERIMENT_NAME}/

# 저장된 체크포인트 목록
find /lustre/checkpoints/${EXPERIMENT_NAME}/ -name "*.bin" -o -name "checkpoint-*"
```

**예상 출력**:

```
ubuntu@ip-10-0-3-12:~$ # 체크포인트 디렉토리 확인
ubuntu@ip-10-0-3-12:~$ ls -lh /lustre/checkpoints/${EXPERIMENT_NAME}/
total 65K
drwxrwxr-x 2 ubuntu ubuntu 33K Nov 29 21:49 checkpoint-1486
drwxrwxr-x 2 ubuntu ubuntu 33K Nov 29 22:07 checkpoint-2972
ubuntu@ip-10-0-3-12:~$ 
ubuntu@ip-10-0-3-12:~$ # 저장된 체크포인트 목록
ubuntu@ip-10-0-3-12:~$ find /lustre/checkpoints/${EXPERIMENT_NAME}/ -name "*.bin" -o -name "checkpoint-*"
/lustre/checkpoints/qwen-wikitext-20251129-201659/checkpoint-1486
/lustre/checkpoints/qwen-wikitext-20251129-201659/checkpoint-1486/training_args.bin
/lustre/checkpoints/qwen-wikitext-20251129-201659/checkpoint-2972
/lustre/checkpoints/qwen-wikitext-20251129-201659/checkpoint-2972/training_args.bin
```

#### 최종 결과 확인

```bash
EXPERIMENT_NAME=$(tail -3 distributed-training-${JOB_ID}.out | grep -oP '(?<=/)[\w-]+(?=/$)' | head -1)
echo "EXPERIMENT_NAME: $EXPERIMENT_NAME"

# 결과 디렉토리 확인
ls -lh /lustre/results/${EXPERIMENT_NAME}/

# 학습 정보 확인
cat /lustre/results/${EXPERIMENT_NAME}/training_info.txt
```

**예상 출력:**
```
ubuntu@ip-10-0-3-12:~$ # 결과 디렉토리 확인
ubuntu@ip-10-0-3-12:~$ ls -lh /lustre/results/${EXPERIMENT_NAME}/
total 947M
-rw-rw-r-- 1 ubuntu ubuntu  605 Nov 29 22:07 added_tokens.json
-rw-rw-r-- 1 ubuntu ubuntu 2.4K Nov 29 22:07 chat_template.jinja
-rw-rw-r-- 1 ubuntu ubuntu 1.3K Nov 29 22:07 config.json
-rw-rw-r-- 1 ubuntu ubuntu  117 Nov 29 22:07 generation_config.json
-rw-rw-r-- 1 ubuntu ubuntu 1.6M Nov 29 22:07 merges.txt
-rw-rw-r-- 1 ubuntu ubuntu 943M Nov 29 22:07 model.safetensors
-rw-rw-r-- 1 ubuntu ubuntu  502 Nov 29 22:07 special_tokens_map.json
-rw-rw-r-- 1 ubuntu ubuntu  11M Nov 29 22:07 tokenizer.json
-rw-rw-r-- 1 ubuntu ubuntu 4.6K Nov 29 22:07 tokenizer_config.json
-rw-rw-r-- 1 ubuntu ubuntu 5.4K Nov 29 22:07 training_args.bin
-rw-rw-r-- 1 ubuntu ubuntu  238 Nov 29 22:07 training_info.txt
-rw-rw-r-- 1 ubuntu ubuntu 2.7M Nov 29 22:07 vocab.json
ubuntu@ip-10-0-3-12:~$ 
ubuntu@ip-10-0-3-12:~$ # 학습 정보 확인
ubuntu@ip-10-0-3-12:~$ cat /lustre/results/${EXPERIMENT_NAME}/training_info.txt
Experiment Name: qwen-wikitext-20251129-201659
Dataset: WikiText-2
Model: Qwen2.5-0.5B
Nodes: 2
Total Samples: 23767
Epochs: 2
Batch Size (per device): 4
Gradient Accumulation: 2
Learning Rate: 2e-05
Completed: 2025-11-29T22:07:56.257921
```
</details>

✅ 분산 학습 실행이 완료되었습니다!


---

## 📚 네비게이션

| 이전 | 상위 | 다음 |
|------|------|------|
| [◀ 클러스터 배포](./02-pcluster-deployment.md) | [📑 목차](../README.md#-가이드-목차) | Coming Soon |
