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
squeue

scontrol show job ${JOB_ID}
```

#### 실시간 로그 확인

```bash
# 표준 출력 로그 (실시간)
tail -f distributed-training-${JOB_ID}.out