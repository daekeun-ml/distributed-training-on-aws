# 1. 사전 요구사항

> 💡 **목표:** ParallelCluster 배포에 필요한 도구 설치 및 코어 인프라를 구성합니다.

> ⚠️ **중요:** 
> - 이 가이드의 대부분의 작업은 CLI를 통해 수행되며, 예제는 **us-east-1(N.Virginia)** 리전을 기준으로 작성되었습니다.
> - AWS CLI 사용을 위한 **IAM 사용자 자격 증명**(Access Key ID, Secret Access Key)이 준비되어 있어야 합니다.


## 목차

- [개요](#개요)
- [사전 준비사항](#사전-준비사항)
- [1. 필요 도구 설치](#1-필요-도구-설치)
  - [1.1 AWS CLI 설치](#11-aws-cli-설치)
  - [1.2 ParallelCluster CLI 설치](#12-parallelcluster-cli-설치)
  - [1.3 Session Manager Plugin 설치](#13-session-manager-plugin-설치)
- [2. 레포지토리 클론](#2-레포지토리-클론)
- [3. 코어 인프라 구성](#3-코어-인프라-구성)
  - [3.1 CloudFormation 템플릿 배포](#31-cloudformation-템플릿-배포)
  - [3.2 배포 검증](#32-배포-검증)
- [4. ECR 및 예제 Custom DLC 준비](#4-ecr-및-예제-custom-dlc-준비)
  - [4.1 ECR Private Repository 생성](#41-ecr-private-repository-생성)
  - [4.2 Custom DLC 이미지 빌드](#42-custom-dlc-이미지-빌드)
  - [4.3 ECR 로그인](#43-ecr-로그인)
  - [4.4 이미지 빌드 및 푸시](#44-이미지-빌드-및-푸시)
  - [4.5 ECR 이미지 확인](#45-ecr-이미지-확인)
- [5. S3 버킷 준비](#5-s3-버킷-준비)
  - [5.1 S3 버킷 생성](#51-s3-버킷-생성)
  - [5.2 부트스트랩 스크립트 업로드](#52-부트스트랩-스크립트-업로드)
  - [5.3 학습 데이터셋 준비](#53-학습-데이터셋-준비)
  - [5.4 FSx Lustre와 S3 연동 설정](#54-fsx-lustre와-s3-연동-설정)
  - [5.5 환경 변수 저장](#55-환경-변수-저장)
  - [5.6 S3 버킷 구조 최종 확인](#56-s3-버킷-구조-최종-확인)  
- [다음 단계](#다음-단계)

---

## 개요

이 문서에서는 다음 작업을 수행합니다:

- ✅ AWS CLI 및 ParallelCluster CLI 설치
- ✅ VPC 네트워크, 공유 스토리지 등 코어 인프라 구성
- ✅ ECR 리포지토리 및 예제 컨테이너 준비
- ✅ S3 버킷 준비

---

## 1. 필요 도구 설치

### 1.1 AWS CLI 설치

AWS CLI는 AWS 리소스를 관리하기 위한 명령줄 도구입니다.

#### Linux / macOS

```bash
# AWS CLI v2 다운로드 및 설치
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

#### macOS (Homebrew 사용)

```bash
brew install awscli
```

#### 설치 확인

```bash
aws --version
```

**예상 출력:**
```
aws-cli/2.x.x Python/3.x.x Linux/x86_64
```

#### AWS CLI 구성

```bash
aws configure
```

다음 정보를 입력합니다:

```
AWS Access Key ID [None]: YOUR_ACCESS_KEY
AWS Secret Access Key [None]: YOUR_SECRET_KEY
Default region name [None]: us-east-1
Default output format [None]: json
```

#### 구성 확인

```bash
# 현재 계정 정보 확인
aws sts get-caller-identity
```

**예상 출력:**
```json
{
    "UserId": "AIDAXXXXXXXXXXXXXXXXX",
    "Account":[REDACTED:BANK_ACCOUNT_NUMBER]12",
    "Arn": "arn:aws:iam::123456789012:user/your-username"
}
```

---

### 1.2 ParallelCluster CLI 설치

ParallelCluster CLI는 HPC 클러스터를 생성하고 관리하는 도구입니다.

#### Python 및 pip 확인

```bash
# Python 3.8 이상 필요
python3 --version

# pip 확인
pip3 --version
```

#### ParallelCluster CLI 설치

```bash
pip3 install --upgrade "aws-parallelcluster==3.14.0"
```

> 📝 **참고:** 
> - 특정 버전(3.14.0)을 설치하여 가이드와의 호환성 보장
> - 최신 버전은 [공식 릴리스](https://github.com/aws/aws-parallelcluster/releases)에서 확인

#### 설치 확인

```bash
pcluster version
```

**예상 출력:**
```json
{
  "version": "3.14.0"
}
```

---

### 1.3 Session Manager Plugin 설치

Session Manager는 SSH 키 없이 안전하게 EC2 인스턴스에 접속할 수 있는 AWS Systems Manager의 기능입니다. 이후 실습에서 ParallelCluster의 Head Node에 접속할 때 사용합니다.

> 💡 **왜 Session Manager를 사용하나요?**
> - SSH 키 관리 불필요
> - 보안 그룹에서 22번 포트 개방 불필요
> - AWS IAM 기반 접근 제어
> - 세션 로그 자동 기록

#### AL2023 and RHEL 8,9

```bash
# Session Manager Plugin 설치
sudo dnf install -y https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm
```

#### Ubuntu / Debian

```bash
# 다운로드
curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb" -o "session-manager-plugin.deb"

# 설치
sudo dpkg -i session-manager-plugin.deb
```

#### macOS

```bash
# 다운로드 및 설치
curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac/sessionmanager-bundle.zip" -o "sessionmanager-bundle.zip"
unzip sessionmanager-bundle.zip
sudo ./sessionmanager-bundle/install -i /usr/local/sessionmanagerplugin -b /usr/local/bin/session-manager-plugin
```

#### 설치 확인

```bash
session-manager-plugin --version
```

**예상 출력:**
```
1.2.xxx
```

> 📝 **참고:** 
> - 자세한 설치 방법은 [공식 문서](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)를 참조하세요.

---

## 2. 레포지토리 클론

이 가이드의 예제 파일들(설정 파일, Dockerfile, 스크립트 등)을 사용하기 위해 레포지토리를 클론합니다.

```bash
# 작업 디렉토리로 이동
cd ~

# 레포지토리 클론
git clone https://github.com/ninedongsu/distributed-training-on-aws.git

# 프로젝트 디렉토리로 이동
cd distributed-training-on-aws/pcluster-container
```

**디렉토리 구조 확인:**

```bash
ls -la
```

**예상 출력:**
```
drwxr-xr-x  docs/
drwxr-xr-x  examples/
  ├── configs/
  ├── containers/
  ├── scripts/
  └── templates/
drwxr-xr-x  images/
-rw-r--r--  README.md
```

> 📝 **참고:** 
> - 이후 모든 명령은 `~/distributed-training-on-aws/pcluster-container` 디렉토리를 기준으로 합니다.
> - 레포지토리 URL은 실제 GitHub 주소로 변경하세요.

---

## 3. 코어 인프라 구성

ParallelCluster를 배포하기 전에 필요한 네트워크 및 스토리지 인프라를 구성합니다.

### 3.1 CloudFormation 템플릿 배포

AWS에서 제공하는 사전 구성된 템플릿을 사용하여 다음 리소스를 자동으로 생성합니다:

- **VPC 및 서브넷**: Public/Private 서브넷 포함
- **보안 그룹**: 클러스터 간 통신을 위한 규칙 (EFA 지원)
- **FSx for Lustre**: 고성능 공유 파일 시스템 (학습 데이터용)
- **FSx for OpenZFS**: Home 디렉토리용 파일 시스템
- **NAT Gateway**: Private 서브넷의 인터넷 연결
- **S3 Endpoint**: S3 접근을 위한 VPC 엔드포인트

> 📝 **템플릿 정보:**
> - 템플릿 전체 내용은 [examples/templates/parallelcluster-prerequisites.yaml](../examples/templates/parallelcluster-prerequisites.yaml)에서 확인할 수 있습니다.
> - FSx Lustre는 **PERSISTENT_1** 배포 유형을 사용하며, 100 또는 200 MB/s/TiB의 처리량을 지원합니다.

#### 환경 변수 설정

```bash
export AWS_REGION=us-east-1  # 원하는 리전
export STACK_NAME=parallelcluster-prerequisites
```

#### 사용 가능한 Availability Zone 확인

템플릿에서 AZ 지정이 필수이므로, 먼저 사용 가능한 AZ를 확인합니다:

```bash
# us-east-1 리전의 AZ 목록 조회
aws ec2 describe-availability-zones \
  --region ${AWS_REGION} \
  --query 'AvailabilityZones[*].[ZoneName,State]' \
  --output table
```

**예상 출력:**
```
-----------------------------
|DescribeAvailabilityZones|
+--------------+------------+
|  us-east-1a  |  available |
|  us-east-1b  |  available |
|  us-east-1c  |  available |
|  us-east-1d  |  available |
|  us-east-1e  |  available |
|  us-east-1f  |  available |
+--------------+------------+
```

원하는 AZ를 환경 변수로 설정:

```bash
export PRIMARY_AZ=us-east-1f  # 원하는 AZ 선택
```

#### CloudFormation 스택 생성

**옵션 1: 로컬 템플릿 파일 사용 (권장)**

```bash
# 템플릿 파일 경로 설정 (이 레포지토리 기준)
export TEMPLATE_FILE=../examples/templates/parallelcluster-prerequisites.yaml

# 기본 설정으로 생성
aws cloudformation create-stack \
  --stack-name ${STACK_NAME} \
  --template-body file://${TEMPLATE_FILE} \
  --region ${AWS_REGION} \
  --parameters \
    ParameterKey=PrimarySubnetAZ,ParameterValue=${PRIMARY_AZ}
```

**옵션 2: S3에 업로드하여 사용**

자신의 S3 버킷에 템플릿을 업로드하고 사용할 수 있습니다:

```bash
# S3 버킷 생성 (이미 있다면 skip)
export TEMPLATE_BUCKET=my-cloudformation-templates-${AWS_REGION}
aws s3 mb s3://${TEMPLATE_BUCKET} --region ${AWS_REGION}

# 템플릿 업로드
aws s3 cp ../examples/templates/parallelcluster-prerequisites.yaml \
  s3://${TEMPLATE_BUCKET}/parallelcluster-prerequisites.yaml

# 스택 생성
aws cloudformation create-stack \
  --stack-name ${STACK_NAME} \
  --template-url https://${TEMPLATE_BUCKET}.s3.amazonaws.com/parallelcluster-prerequisites.yaml \
  --region ${AWS_REGION} \
  --parameters \
    ParameterKey=PrimarySubnetAZ,ParameterValue=${PRIMARY_AZ}
```

**커스텀 설정으로 생성:**

```bash
aws cloudformation create-stack \
  --stack-name ${STACK_NAME} \
  --template-body file://${TEMPLATE_FILE} \
  --region ${AWS_REGION} \
  --parameters \
    ParameterKey=VPCName,ParameterValue="ML Training VPC" \
    ParameterKey=PrimarySubnetAZ,ParameterValue=${PRIMARY_AZ} \
    ParameterKey=Capacity,ParameterValue=2400 \
    ParameterKey=PerUnitStorageThroughput,ParameterValue=200 \
    ParameterKey=Compression,ParameterValue=LZ4 \
    ParameterKey=LustreVersion,ParameterValue=2.15 \
    ParameterKey=OpenZFSCapacity,ParameterValue=512 \
    ParameterKey=OpenZFSThroughput,ParameterValue=320 \
    ParameterKey=CreateS3Endpoint,ParameterValue=true
```

#### 배포 진행 상황 모니터링

```bash
# 스택 생성 상태 확인
aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].StackStatus' \
  --output text
```

**예상 상태:**
- `CREATE_IN_PROGRESS`: 생성 중
- `CREATE_COMPLETE`: 생성 완료 ✅
- `CREATE_FAILED`: 생성 실패 ❌

> ⏱️ **예상 소요 시간:** 약 15-20분

#### 실시간 이벤트 모니터링

```bash
# 이벤트 로그 확인 (계속 업데이트)
watch -n 10 "aws cloudformation describe-stack-events \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --max-items 5 \
  --query 'StackEvents[*].[Timestamp,ResourceStatus,ResourceType,LogicalResourceId]' \
  --output table"
```

또는 스택 완료까지 대기:

```bash
# 스택 생성 완료까지 대기
aws cloudformation wait stack-create-complete \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION}
```

---

### 3.2 배포 검증

스택 생성이 완료되면 생성된 리소스를 확인합니다.

#### 출력값 확인

```bash
# CloudFormation 출력값 조회
aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].Outputs' \
  --output table
```

**주요 출력값:**

| OutputKey | 설명 | 예시 |
|-----------|------|------|
| `VPC` | VPC ID | vpc-0a1b2c3d4e5f6g7h8 |
| `PublicSubnet` | Public 서브넷 ID | subnet-0a1b2c3d |
| `PrimaryPrivateSubnet` | Private 서브넷 ID | subnet-4e5f6g7h |
| `SecurityGroup` | 보안 그룹 ID | sg-0a1b2c3d4e5f6g7h8 |
| `FSxLustreFilesystemId` | FSx Lustre 파일 시스템 ID | fs-0a1b2c3d4e5f6g7h8 |
| `FSxLustreFilesystemMountname` | FSx Lustre 마운트 이름 | xxxxxxxx |
| `FSxLustreFilesystemDNSname` | FSx Lustre DNS 이름 | fs-xxx.fsx.us-east-1.amazonaws.com |
| `FSxORootVolumeId` | FSx OpenZFS 루트 볼륨 ID | fsvol-0a1b2c3d4e5f6g7h8 |

#### 출력값을 환경 변수로 저장

나중에 사용하기 위해 출력값을 환경 변수로 저장합니다:

```bash
# 출력값 추출 및 환경 변수 설정
export VPC_ID=$(aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].Outputs[?OutputKey==`VPC`].OutputValue' \
  --output text)

export PUBLIC_SUBNET_ID=$(aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].Outputs[?OutputKey==`PublicSubnet`].OutputValue' \
  --output text)

export PRIVATE_SUBNET_ID=$(aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].Outputs[?OutputKey==`PrimaryPrivateSubnet`].OutputValue' \
  --output text)

export SECURITY_GROUP_ID=$(aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].Outputs[?OutputKey==`SecurityGroup`].OutputValue' \
  --output text)

export FSX_LUSTRE_ID=$(aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].Outputs[?OutputKey==`FSxLustreFilesystemId`].OutputValue' \
  --output text)

export FSX_LUSTRE_MOUNT_NAME=$(aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].Outputs[?OutputKey==`FSxLustreFilesystemMountname`].OutputValue' \
  --output text)

export FSX_LUSTRE_DNS=$(aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].Outputs[?OutputKey==`FSxLustreFilesystemDNSname`].OutputValue' \
  --output text)

export FSX_OPENZFS_ROOT_VOLUME_ID=$(aws cloudformation describe-stacks \
  --stack-name ${STACK_NAME} \
  --region ${AWS_REGION} \
  --query 'Stacks[0].Outputs[?OutputKey==`FSxORootVolumeId`].OutputValue' \
  --output text)

# 확인
echo "VPC ID: $VPC_ID"
echo "Public Subnet: $PUBLIC_SUBNET_ID"
echo "Private Subnet: $PRIVATE_SUBNET_ID"
echo "Security Group: $SECURITY_GROUP_ID"
echo "FSx Lustre ID: $FSX_LUSTRE_ID"
echo "FSx Lustre Mount Name: $FSX_LUSTRE_MOUNT_NAME"
echo "FSx Lustre DNS: $FSX_LUSTRE_DNS"
echo "FSx OpenZFS Root Volume ID: $FSX_OPENZFS_ROOT_VOLUME_ID"
```

> 💡 **팁:** 이 환경 변수들을 파일로 저장하여 세션 간에 유지할 수 있습니다.

```bash
# 환경 변수를 파일로 저장
cat > ~/pcluster-env.sh << EOF
export AWS_REGION=${AWS_REGION}
export STACK_NAME=${STACK_NAME}
export PRIMARY_AZ=${PRIMARY_AZ}
export VPC_ID=${VPC_ID}
export PUBLIC_SUBNET_ID=${PUBLIC_SUBNET_ID}
export PRIVATE_SUBNET_ID=${PRIVATE_SUBNET_ID}
export SECURITY_GROUP_ID=${SECURITY_GROUP_ID}
export FSX_LUSTRE_ID=${FSX_LUSTRE_ID}
export FSX_LUSTRE_MOUNT_NAME=${FSX_LUSTRE_MOUNT_NAME}
export FSX_LUSTRE_DNS=${FSX_LUSTRE_DNS}
export FSX_OPENZFS_ROOT_VOLUME_ID=${FSX_OPENZFS_ROOT_VOLUME_ID}
EOF

# 나중에 사용 시
source ~/pcluster-env.sh
```

#### 리소스 상태 확인 (선택 사항)

**VPC 확인:**
```bash
aws ec2 describe-vpcs \
  --vpc-ids ${VPC_ID} \
  --region ${AWS_REGION} \
  --query 'Vpcs[0].[VpcId,CidrBlock,State]' \
  --output table
```

**서브넷 확인:**
```bash
aws ec2 describe-subnets \
  --subnet-ids ${PUBLIC_SUBNET_ID} ${PRIVATE_SUBNET_ID} \
  --region ${AWS_REGION} \
  --query 'Subnets[*].[SubnetId,CidrBlock,AvailabilityZone,MapPublicIpOnLaunch]' \
  --output table
```

**보안 그룹 확인:**
```bash
aws ec2 describe-security-groups \
  --group-ids ${SECURITY_GROUP_ID} \
  --region ${AWS_REGION} \
  --query 'SecurityGroups[0].[GroupId,GroupName,Description]' \
  --output table
```

**FSx for Lustre 확인:**
```bash
aws fsx describe-file-systems \
  --file-system-ids ${FSX_LUSTRE_ID} \
  --region ${AWS_REGION} \
  --query 'FileSystems[0].[FileSystemId,Lifecycle,StorageCapacity,FileSystemTypeVersion]' \
  --output table
```

**예상 출력:**
```
--------------------------------------------------------------------
|                     DescribeFileSystems                          |
+----------------------+------------+--------+---------------------+
|  fs-0a1b2c3d4e5f... |  AVAILABLE | 1200   | 2.15                |
+----------------------+------------+--------+---------------------+
```

**FSx for OpenZFS 확인:**
```bash
aws fsx describe-volumes \
  --volume-ids ${FSX_OPENZFS_ROOT_VOLUME_ID} \
  --region ${AWS_REGION} \
  --query 'Volumes[0].[VolumeId,Lifecycle,VolumeType]' \
  --output table
```

---

## 4. ECR 및 예제 Custom DLC 준비

컨테이너 기반 학습을 위해 Amazon ECR(Elastic Container Registry)에 커스텀 Deep Learning Container(DLC)를 준비합니다.

> 💡 **Custom DLC란?**
> - AWS에서 제공하는 공식 Deep Learning Container를 베이스로 사용
> - 추가 라이브러리 및 학습 스크립트를 포함하여 커스터마이징
> - ECR에 저장하여 클러스터에서 사용

### 4.1 ECR Private Repository 생성

학습용 컨테이너 이미지를 저장할 프라이빗 리포지토리를 생성합니다.

#### 리포지토리 이름 설정

```bash
export ECR_REPO_NAME=pytorch-training-custom
```

#### ECR 리포지토리 생성

```bash
aws ecr create-repository \
  --repository-name ${ECR_REPO_NAME} \
  --region ${AWS_REGION}
```

#### 리포지토리 URI 저장

```bash
export ECR_REPO_URI=$(aws ecr describe-repositories \
  --repository-names ${ECR_REPO_NAME} \
  --region ${AWS_REGION} \
  --query 'repositories[0].repositoryUri' \
  --output text)

echo "ECR Repository URI: ${ECR_REPO_URI}"
```

#### 리포지토리 확인

```bash
aws ecr describe-repositories \
  --repository-names ${ECR_REPO_NAME} \
  --region ${AWS_REGION} \
  --query 'repositories[0].[repositoryName,repositoryUri,createdAt]' \
  --output table
```

---

### 4.2 Custom DLC 이미지 빌드

AWS에서 제공하는 PyTorch DLC를 베이스로 분산 학습에 필요한 라이브러리를 추가한 커스텀 이미지를 빌드합니다.

#### Dockerfile 및 학습 스크립트 위치

> 📁 **파일 위치:** 
> - `examples/containers/pytorch/Dockerfile`
> - `examples/containers/pytorch/ds_config.json`
> - `examples/containers/pytorch/train_distributed_deepspeed.py`

#### Dockerfile 내용

```dockerfile
FROM public.ecr.aws/deep-learning-containers/pytorch-training:2.5.1-gpu-py311-cu124-ubuntu22.04-ec2-v1.30

RUN apt-get update && apt-get install -y \
    openssh-server \
    pdsh \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

RUN pip install \
    transformers>=4.37.0 \
    flash-attn --no-build-isolation \
    deepspeed \
    accelerate \
    datasets

WORKDIR /workspace

COPY ds_config.json /workspace/
COPY train_distributed_deepspeed.py /workspace/
```

**Dockerfile 구성 설명:**

| 항목 | 설명 |
|------|------|
| **Base Image** | AWS 공식 PyTorch 2.5.1 DLC (CUDA 12.4, Python 3.11, Ubuntu 22.04) |
| **Python Libraries** | `transformers`: Hugging Face Transformers<br>`flash-attn`: Flash Attention 최적화<br>`deepspeed`: DeepSpeed 분산 학습<br>`accelerate`: Hugging Face Accelerate<br>`datasets`: 데이터셋 로드 |
| **Working Directory** | `/workspace`: 학습 스크립트 실행 디렉토리 |
| **Training Scripts** | `ds_config.json`: DeepSpeed 설정 파일<br>`train_distributed_deepspeed.py`: 분산 학습 스크립트 |

> 💡 **왜 AWS DLC를 사용하나요?**
> - AWS에 최적화된 PyTorch 및 CUDA 설정
> - EFA(Elastic Fabric Adapter) 지원
> - NCCL 최적화
> - 정기적인 보안 업데이트 및 패치

#### 작업 디렉토리 이동

```bash
# Dockerfile이 있는 디렉토리로 이동
cd examples/containers/pytorch/
```

> 📝 **참고:** 
> - `ds_config.json`과 `train_distributed_deepspeed.py` 파일이 같은 디렉토리에 있어야 합니다.
> - 실제 파일 내용은 [examples/containers/pytorch/](../examples/containers/pytorch/) 디렉토리를 참조하세요.

---

### 4.3 ECR 로그인

컨테이너 이미지를 푸시하기 전에 ECR에 로그인합니다.

```bash
# ECR 로그인
aws ecr get-login-password --region ${AWS_REGION} | \
  docker login --username AWS --password-stdin ${ECR_REPO_URI}
```

**예상 출력:**
```
Login Succeeded
```

---

### 4.4 이미지 빌드 및 푸시

#### 이미지 빌드

```bash
# 이미지 태그 설정
export IMAGE_TAG=latest

# Docker 이미지 빌드
docker build -t ${ECR_REPO_NAME}:${IMAGE_TAG} .
```

**빌드 진행 상황:**
```
[+] Building 245.3s (10/10) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 425B
 => [internal] load .dockerignore
 => [1/5] FROM public.ecr.aws/deep-learning-containers/pytorch-training:2.5.1...
 => [2/5] RUN apt-get update && apt-get install -y openssh-server...
 => [3/5] RUN pip install transformers>=4.37.0...
 => [4/5] WORKDIR /workspace
 => [5/5] COPY ds_config.json /workspace/
 => [6/5] COPY train_distributed_deepspeed.py /workspace/
 => exporting to image
 => => naming to docker.io/library/pytorch-training-custom:latest
```

> ⏱️ **예상 소요 시간:** 약 5-10분

#### 로컬 이미지 확인

```bash
docker images ${ECR_REPO_NAME}
```

**예상 출력:**
```
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
pytorch-training-custom   latest    9d2cf2ea9849   27 seconds ago   20.3GB
```

#### ECR 태그 지정

```bash
docker tag ${ECR_REPO_NAME}:${IMAGE_TAG} ${ECR_REPO_URI}:${IMAGE_TAG}
```

#### ECR에 이미지 푸시

```bash
docker push ${ECR_REPO_URI}:${IMAGE_TAG}
```

**푸시 진행 상황:**
```
The push refers to repository [123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-training-custom]
5f70bf18a086: Pushed
a3b5c80a4eba: Pushed
7f18b442972b: Pushed
3ce63537e70c: Pushed
latest: digest: sha256:1234567890abcdef... size: 4321
```

> ⏱️ **예상 소요 시간:** 약 10-20분

---

### 4.5 ECR 이미지 확인

#### ECR에 푸시된 이미지 확인

```bash
aws ecr describe-images \
  --repository-name ${ECR_REPO_NAME} \
  --region ${AWS_REGION} \
  --query 'imageDetails[*].[imageTags[0],imagePushedAt,imageSizeInBytes]' \
  --output table
```

**예상 출력:**
```
---------------------------------------------------------------
|                       DescribeImages                        |
+--------+------------------------------------+---------------+
|  latest|  2025-11-29T14:57:42.983000+00:00  |  10388392074  |
+--------+------------------------------------+---------------+
```

---

## 5. S3 버킷 준비

ParallelCluster 운영 및 학습 데이터 저장을 위한 S3 버킷을 준비합니다.

> 💡 **S3 버킷 용도:**
> - **부트스트랩 스크립트**: 클러스터 생성 시 자동 실행될 스크립트
> - **학습 데이터셋**: FSx Lustre와 연동하여 사용
> - **학습 결과**: 체크포인트, 로그, 모델 저장

### 5.1 S3 버킷 생성

#### 버킷 이름 설정

S3 버킷 이름은 전역적으로 고유해야 하므로 AWS 계정 ID를 포함합니다:

```bash
# AWS 계정 ID 가져오기
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# 버킷 이름 설정
export S3_BUCKET_NAME=parallelcluster-${AWS_ACCOUNT_ID}-${AWS_REGION}

echo "S3 Bucket Name: ${S3_BUCKET_NAME}"
```

#### S3 버킷 생성

```bash
# S3 버킷 생성
aws s3 mb s3://${S3_BUCKET_NAME} --region ${AWS_REGION}
```

**예상 출력:**
```
make_bucket: parallelcluster-123456789012-us-east-1
```

#### 버킷 확인

```bash
# 버킷 목록 확인
aws s3 ls | grep ${S3_BUCKET_NAME}
```

**예상 출력:**
```
2025-11-29 16:08:26 parallelcluster-123456789012-us-east-1
```

---

### 5.2 부트스트랩 스크립트 업로드

클러스터 생성 시 자동으로 실행될 부트스트랩 스크립트를 업로드합니다.

> 💡 **부트스트랩 스크립트 역할:**
> - **head-node-enroot-pyxis-setup.sh**: Head Node에서 Enroot와 Pyxis 설치 및 설정
> - **compute-node-enroot-pyxis-setup.sh**: Compute Node에서 Enroot와 Pyxis 설치 및 설정

#### 스크립트 디렉토리 구조 생성

```bash
# S3에 디렉토리 구조 생성
aws s3api put-object \
  --bucket ${S3_BUCKET_NAME} \
  --key scripts/ \
  --region ${AWS_REGION}

aws s3api put-object \
  --bucket ${S3_BUCKET_NAME} \
  --key scripts/bootstrap/ \
  --region ${AWS_REGION}

#### 부트스트랩 스크립트 파일 확인

업로드할 스크립트 파일이 있는지 확인합니다:

```bash
# 레포지토리 루트로 이동
cd ~/distributed-training-on-aws/pcluster-container

# 스크립트 파일 확인
ls -lh examples/scripts/bootstrap/
```

**예상 출력:**
```
-rw-r--r--. 1 user  staff 7.5K Nov 29 14:31 compute-node-enroot-pyxis-setup.sh
-rw-r--r--. 1 user  staff 8.4K Nov 29 14:31 head-node-enroot-pyxis-setup.sh
```

#### 부트스트랩 스크립트 업로드

```bash
# Head Node 스크립트 업로드
aws s3 cp examples/scripts/bootstrap/head-node-enroot-pyxis-setup.sh \
  s3://${S3_BUCKET_NAME}/scripts/bootstrap/ \
  --region ${AWS_REGION}

# Compute Node 스크립트 업로드
aws s3 cp examples/scripts/bootstrap/compute-node-enroot-pyxis-setup.sh \
  s3://${S3_BUCKET_NAME}/scripts/bootstrap/ \
  --region ${AWS_REGION}
```

**예상 출력:**
```
upload: examples/scripts/bootstrap/head-node-enroot-pyxis-setup.sh to s3://parallelcluster-123456789012-us-east-1/scripts/bootstrap/head-node-enroot-pyxis-setup.sh
upload: examples/scripts/bootstrap/compute-node-enroot-pyxis-setup.sh to s3://parallelcluster-123456789012-us-east-1/scripts/bootstrap/compute-node-enroot-pyxis-setup.sh
```

#### 업로드된 파일 확인

```bash
# 부트스트랩 스크립트 확인
aws s3 ls s3://${S3_BUCKET_NAME}/scripts/bootstrap/
```

**예상 출력:**
```
2025-11-29 16:11:37       7654 compute-node-enroot-pyxis-setup.sh
2025-11-29 16:11:35       8517 head-node-enroot-pyxis-setup.sh
```

#### 스크립트 URL 환경 변수 저장

나중에 클러스터 설정 파일에서 사용할 스크립트 URL을 환경 변수로 저장합니다:

```bash
# 부트스트랩 스크립트 URL
export HEAD_NODE_BOOTSTRAP_SCRIPT=s3://${S3_BUCKET_NAME}/scripts/bootstrap/head-node-enroot-pyxis-setup.sh
export COMPUTE_NODE_BOOTSTRAP_SCRIPT=s3://${S3_BUCKET_NAME}/scripts/bootstrap/compute-node-enroot-pyxis-setup.sh

# 확인
echo "Head Node Bootstrap: ${HEAD_NODE_BOOTSTRAP_SCRIPT}"
echo "Compute Node Bootstrap: ${COMPUTE_NODE_BOOTSTRAP_SCRIPT}"
```

**예상 출력:**
```
Head Node Bootstrap: s3://parallelcluster-123456789012-us-east-1/scripts/bootstrap/head-node-enroot-pyxis-setup.sh
Compute Node Bootstrap: s3://parallelcluster-123456789012-us-east-1/scripts/bootstrap/compute-node-enroot-pyxis-setup.sh
```

#### 환경 변수 파일에 추가

```bash
# 환경 변수 파일에 추가
cat >> ~/pcluster-env.sh << EOF
export HEAD_NODE_BOOTSTRAP_SCRIPT=${HEAD_NODE_BOOTSTRAP_SCRIPT}
export COMPUTE_NODE_BOOTSTRAP_SCRIPT=${COMPUTE_NODE_BOOTSTRAP_SCRIPT}
EOF
```

> 📝 **참고:** 
> - 이 스크립트들은 다음 단계인 클러스터 배포 시 자동으로 실행됩니다.
> - Head Node와 Compute Node에 각각 Enroot와 Pyxis가 설치되어 컨테이너 기반 작업을 실행할 수 있게 됩니다.

---

### 5.3 학습 데이터셋 준비

학습에 사용할 데이터셋을 S3에 업로드합니다. 이 예제에서는 Hugging Face의 WikiText-2 데이터셋을 사용합니다.
이 데이터는 FSx Lustre를 통해 고성능으로 접근할 수 있습니다.

#### S3 디렉토리 구조

#### 데이터셋 준비 스크립트

레포지토리에 포함된 데이터셋 준비 스크립트를 사용합니다.

> 📁 **파일 위치:** `examples/scripts/python/dataset_prepare_and_upload.py`

**스크립트 내용:**
```python
import os
from datasets import load_dataset

def prepare_wikitext():
    """WikiText-2 데이터셋 다운로드 및 준비"""
    print("📥 Downloading WikiText-2...")
    dataset = load_dataset("wikitext", "wikitext-2-raw-v1")
    
    output_dir = "./wikitext-2-prepared"
    dataset.save_to_disk(output_dir)
    
    print(f"✅ Dataset saved to {output_dir}")
    print(f"📊 Train samples: {len(dataset['train'])}")
    print(f"📊 Validation samples: {len(dataset['validation'])}")
    print(f"📊 Test samples: {len(dataset['test'])}")
    
    return output_dir

if __name__ == "__main__":
    # 데이터셋 준비
    wikitext_dir = prepare_wikitext()
    
    # 환경 변수에서 S3 정보 가져오기
    s3_bucket = os.environ.get('S3_BUCKET_NAME')
    aws_region = os.environ.get('AWS_REGION', 'us-east-1')
    
    if s3_bucket:
        s3_path = f"s3://{s3_bucket}/data/wikitext-2/"
        
        print(f"\n📤 To upload to S3, run the following command:")
        print(f"\naws s3 sync {wikitext_dir} {s3_path} --region {aws_region}")
    else:
        print("\n⚠️  S3_BUCKET_NAME environment variable not set.")
        print("Set it with: export S3_BUCKET_NAME=your-bucket-name")
        print(f"\nThen run:")
        print(f"aws s3 sync {wikitext_dir} s3://YOUR-BUCKET/data/wikitext-2/ --region us-east-1")
```

#### 필요한 Python 패키지 설치

```bash
# datasets 라이브러리 설치
pip3 install datasets
```

#### 데이터셋 다운로드 및 준비

```bash
# 레포지토리 루트로 이동
cd ~/distributed-training-on-aws/pcluster-container

# 환경 변수 로드 (S3_BUCKET_NAME 필요)
source ~/pcluster-env.sh

# 스크립트 실행
python3 examples/scripts/python/dataset_prepare_and_upload.py
```

**예상 출력:**
```
📥 Downloading WikiText-2...
Downloading data files: 100%|████████████████████| 3/3 [00:01<00:00,  2.14it/s]
Extracting data files: 100%|█████████████████████| 3/3 [00:00<00:00, 45.23it/s]
Generating train split: 36718 examples [00:02, 15234.56 examples/s]
Generating validation split: 3760 examples [00:00, 18234.12 examples/s]
Generating test split: 4358 examples [00:00, 17654.34 examples/s]
✅ Dataset saved to ./wikitext-2-prepared
📊 Train samples: 36718
📊 Validation samples: 3760
📊 Test samples: 4358

📤 To upload to S3, run the following command:

aws s3 sync ./wikitext-2-prepared s3://parallelcluster-123456789012-us-east-1/data/wikitext-2/ --region us-east-1
```

> ⏱️ **예상 소요 시간:** 약 2-3분 (다운로드)

#### S3에 업로드

스크립트가 출력한 명령어를 복사하여 실행합니다:

```bash
# 스크립트 출력 명령어 실행
aws s3 sync ./wikitext-2-prepared s3://parallelcluster-123456789012-us-east-1/data/wikitext-2/ --region us-east-1
```

**예상 출력:**
```
upload: ./wikitext-2-prepared/dataset_info.json to s3://parallelcluster-123456789012-us-east-1/data/wikitext-2/dataset_info.json
upload: ./wikitext-2-prepared/train/data-00000-of-00001.arrow to s3://parallelcluster-123456789012-us-east-1/data/wikitext-2/train/data-00000-of-00001.arrow
upload: ./wikitext-2-prepared/validation/data-00000-of-00001.arrow to s3://parallelcluster-123456789012-us-east-1/data/wikitext-2/validation/data-00000-of-00001.arrow
upload: ./wikitext-2-prepared/test/data-00000-of-00001.arrow to s3://parallelcluster-123456789012-us-east-1/data/wikitext-2/test/data-00000-of-00001.arrow
upload: ./wikitext-2-prepared/state.json to s3://parallelcluster-123456789012-us-east-1/data/wikitext-2/state.json
```

> ⏱️ **예상 소요 시간:** 약 1-2분 (업로드)

#### 업로드된 데이터 확인

```bash
# S3에 업로드된 데이터 확인
aws s3 ls s3://${S3_BUCKET_NAME}/data/wikitext-2/ --recursive --human-readable
```

**예상 출력:**
```
2024-01-01 12:00:00    2.1 KiB data/wikitext-2/dataset_info.json
2024-01-01 12:00:00    4.5 MiB data/wikitext-2/train/data-00000-of-00001.arrow
2024-01-01 12:00:00  512.3 KiB data/wikitext-2/validation/data-00000-of-00001.arrow
2024-01-01 12:00:00  589.7 KiB data/wikitext-2/test/data-00000-of-00001.arrow
2024-01-01 12:00:00      156 data/wikitext-2/state.json
```

#### 로컬 파일 정리 (선택사항)

```bash
# 업로드 완료 후 로컬 파일 삭제
rm -rf ./wikitext-2-prepared
```

---

### 5.4 FSx Lustre와 S3 연동 설정

FSx Lustre가 S3 데이터를 자동으로 가져오고 내보낼 수 있도록 Data Repository Association (DRA)을 설정합니다.

> 💡 **Data Repository Association (DRA)이란?**
> - FSx Lustre와 S3 버킷 간의 연결을 설정
> - S3의 데이터를 FSx로 자동 import (Lazy Loading)
> - FSx의 변경사항을 S3로 자동 export (백업)
> - 여러 개의 S3 경로를 FSx의 다른 경로에 매핑 가능

#### FSx Lustre 디렉토리 구조

FSx Lustre에서 다음과 같은 디렉토리 구조를 사용합니다:

```
/lustre/
├── data/              # S3 data/ 와 연동 (학습 데이터)
├── checkpoints/       # S3 checkpoints/ 와 연동 (체크포인트 저장/복원)
├── logs/              # S3 logs/ 와 연동 (학습 로그)
└── results/           # S3 results/ 와 연동 (최종 결과)
```

#### DRA 환경 변수 설정

```bash
# DRA 이름 및 경로 설정
export DRA_DATA_NAME=training-data
export DRA_CHECKPOINTS_NAME=training-checkpoints
export DRA_LOGS_NAME=training-logs
export DRA_RESULTS_NAME=training-results
```

#### Data Repository Association 생성

**1. 학습 데이터용 DRA:**
```bash
aws fsx create-data-repository-association \
  --file-system-id ${FSX_LUSTRE_ID} \
  --file-system-path /data \
  --data-repository-path s3://${S3_BUCKET_NAME}/data/ \
  --batch-import-meta-data-on-create \
  --s3 '{
    "AutoImportPolicy": {
      "Events": ["NEW", "CHANGED", "DELETED"]
    }
  }' \
  --region ${AWS_REGION}
```

**2. 체크포인트용 DRA:**
```bash
aws fsx create-data-repository-association \
  --file-system-id ${FSX_LUSTRE_ID} \
  --file-system-path /checkpoints \
  --data-repository-path s3://${S3_BUCKET_NAME}/checkpoints/ \
  --s3 '{
    "AutoImportPolicy": {
      "Events": ["NEW", "CHANGED", "DELETED"]
    },
    "AutoExportPolicy": {
      "Events": ["NEW", "CHANGED", "DELETED"]
    }
  }' \
  --region ${AWS_REGION}
```

**3. 로그용 DRA:**
```bash
aws fsx create-data-repository-association \
  --file-system-id ${FSX_LUSTRE_ID} \
  --file-system-path /logs \
  --data-repository-path s3://${S3_BUCKET_NAME}/logs/ \
  --s3 '{
    "AutoExportPolicy": {
      "Events": ["NEW", "CHANGED", "DELETED"]
    }
  }' \
  --region ${AWS_REGION}
```

**4. 결과용 DRA:**
```bash
aws fsx create-data-repository-association \
  --file-system-id ${FSX_LUSTRE_ID} \
  --file-system-path /results \
  --data-repository-path s3://${S3_BUCKET_NAME}/results/ \
  --s3 '{
    "AutoExportPolicy": {
      "Events": ["NEW", "CHANGED", "DELETED"]
    }
  }' \
  --region ${AWS_REGION}
```

**예상 출력 (각 DRA마다):**
```json
{
    "Association": {
        "AssociationId": "dra-0a1b2c3d4e5f6g7h8",
        "ResourceARN": "arn:aws:fsx:us-east-1:123456789012:association/fs-xxx/dra-xxx",
        "FileSystemId": "fs-0a1b2c3d4e5f6g7h8",
        "Lifecycle": "CREATING",
        "FileSystemPath": "/data",
        "DataRepositoryPath": "s3://parallelcluster-123456789012-us-east-1/data/",
        "BatchImportMetaDataOnCreate": true,
        "ImportedFileChunkSize": 1024,
        "S3": {
            "AutoImportPolicy": {
                "Events": ["NEW", "CHANGED", "DELETED"]
            }
        }
    }
}
```

> 💡 **DRA 설정 설명:**
> - **AutoImportPolicy**: S3에서 FSx로 자동 가져오기
>   - `data/`: 학습 데이터는 import만 (읽기 전용)
>   - `checkpoints/`: import & export (저장 및 복원)
> - **AutoExportPolicy**: FSx에서 S3로 자동 내보내기
>   - `checkpoints/`, `logs/`, `results/`: FSx에서 생성된 파일을 S3로 백업
> - **BatchImportMetaDataOnCreate**: 생성 시 S3 메타데이터 일괄 가져오기

#### DRA 생성 상태 확인

```bash
# 모든 DRA 목록 확인
aws fsx describe-data-repository-associations \
  --filters Name=file-system-id,Values=${FSX_LUSTRE_ID} \
  --region ${AWS_REGION} \
  --query 'Associations[*].[AssociationId,FileSystemPath,DataRepositoryPath,Lifecycle]' \
  --output table
```

**예상 출력:**
```
---------------------------------------------------------------
|          DescribeDataRepositoryAssociations                |
+----------------------+---------------+-----------+-----------+
|  dra-0a1b2c3d...    |  /data        | s3://.../data/       | AVAILABLE |
|  dra-1b2c3d4e...    |  /checkpoints | s3://.../checkpoints/| AVAILABLE |
|  dra-2c3d4e5f...    |  /logs        | s3://.../logs/       | AVAILABLE |
|  dra-3d4e5f6g...    |  /results     | s3://.../results/    | AVAILABLE |
+----------------------+---------------+-----------+-----------+
```

#### DRA 상태가 AVAILABLE이 될 때까지 대기

```bash
# DRA 생성 완료 확인 (모든 DRA가 AVAILABLE 상태가 될 때까지)
while true; do
  STATUS=$(aws fsx describe-data-repository-associations \
    --filters Name=file-system-id,Values=${FSX_LUSTRE_ID} \
    --region ${AWS_REGION} \
    --query 'Associations[?Lifecycle!=`AVAILABLE`].Lifecycle' \
    --output text)
  
  if [ -z "$STATUS" ]; then
    echo "✅ All DRAs are AVAILABLE!"
    break
  else
    echo "Waiting for DRAs to be AVAILABLE... (Current: $STATUS)"
    sleep 30
  fi
done
```

> ⏱️ **예상 소요 시간:** 각 DRA당 1-2분, 총 5-10분

#### 데이터 접근 예시

DRA 설정이 완료되면 클러스터에서 다음과 같이 데이터에 접근할 수 있습니다.

> 💡 **Lazy Loading:** FSx Lustre는 파일에 처음 접근할 때 S3에서 자동으로 데이터를 가져옵니다. 메타데이터는 DRA 생성 시 즉시 로드되므로 파일 목록은 바로 확인할 수 있습니다.

```bash
# 클러스터 Head Node에서 실행 (클러스터 생성 후)

# WikiText-2 데이터셋 확인 (5.3에서 업로드한 데이터)
# S3: s3://bucket/data/wikitext-2/
# FSx: /lustre/data/wikitext-2/
ls -lh /lustre/data/wikitext-2/

# 예상 출력:
# drwxr-xr-x 2 root root 4.0K Jan 1 12:00 train
# drwxr-xr-x 2 root root 4.0K Jan 1 12:00 validation
# drwxr-xr-x 2 root root 4.0K Jan 1 12:00 test
# -rw-r--r-- 1 root root 2.1K Jan 1 12:00 dataset_info.json
# -rw-r--r-- 1 root root  156 Jan 1 12:00 state.json

# 학습 데이터 파일 확인
ls -lh /lustre/data/wikitext-2/train/

# 데이터 읽기 테스트 (첫 접근 시 S3에서 자동 로드)
head /lustre/data/wikitext-2/dataset_info.json

# 체크포인트 저장 (FSx → S3로 자동 export)
# 학습 스크립트에서 사용할 경로
echo "epoch_10_checkpoint" > /lustre/checkpoints/model_epoch_10.txt

# 로그 저장 (FSx → S3로 자동 export)
echo "Training started at $(date)" > /lustre/logs/training.log

# 최종 결과 저장 (FSx → S3로 자동 export)
echo "Training completed" > /lustre/results/final_model_info.txt

#### FSx Lustre 디렉토리 환경 변수 저장

나중에 학습 스크립트에서 사용할 수 있도록 경로를 저장합니다:

```bash
# FSx Lustre 경로 환경 변수
export LUSTRE_DATA_DIR=/lustre/data
export LUSTRE_CHECKPOINT_DIR=/lustre/checkpoints
export LUSTRE_LOG_DIR=/lustre/logs
export LUSTRE_RESULTS_DIR=/lustre/results

# 환경 변수 파일에 추가
cat >> ~/pcluster-env.sh << EOF
export LUSTRE_DATA_DIR=${LUSTRE_DATA_DIR}
export LUSTRE_CHECKPOINT_DIR=${LUSTRE_CHECKPOINT_DIR}
export LUSTRE_LOG_DIR=${LUSTRE_LOG_DIR}
export LUSTRE_RESULTS_DIR=${LUSTRE_RESULTS_DIR}
EOF
```

---

### 5.5 환경 변수 저장

S3 버킷 및 이미지 정보를 환경 변수 파일에 추가합니다:

```bash
# 환경 변수 파일에 추가
cat >> ~/pcluster-env.sh << EOF
export AWS_ACCOUNT_ID=${AWS_ACCOUNT_ID}
export S3_BUCKET_NAME=${S3_BUCKET_NAME}
export ECR_REPO_NAME=${ECR_REPO_NAME}
export ECR_REPO_URI=${ECR_REPO_URI}
export IMAGE_TAG=${IMAGE_TAG}
export TRAINING_IMAGE_URI=${TRAINING_IMAGE_URI}
EOF

# 확인
source ~/pcluster-env.sh
```

#### 전체 환경 변수 확인

```bash
# 저장된 모든 환경 변수 확인
cat ~/pcluster-env.sh
```

**예상 출력:**
```bash
export AWS_REGION=us-east-1
export STACK_NAME=parallelcluster-prerequisites
export PRIMARY_AZ=us-east-1a
export VPC_ID=vpc-0a1b2c3d4e5f6g7h8
export PUBLIC_SUBNET_ID=subnet-0a1b2c3d
export PRIVATE_SUBNET_ID=subnet-4e5f6g7h
export SECURITY_GROUP_ID=sg-0a1b2c3d4e5f6g7h8
export FSX_LUSTRE_ID=fs-0a1b2c3d4e5f6g7h8
export FSX_LUSTRE_MOUNT_NAME=xxxxxxxx
export FSX_LUSTRE_DNS=fs-xxx.fsx.us-east-1.amazonaws.com
export FSX_OPENZFS_ROOT_VOLUME_ID=fsvol-0a1b2c3d4e5f6g7h8
export HEAD_NODE_BOOTSTRAP_SCRIPT=s3://parallelcluster-123456789012-us-east-1/scripts/bootstrap/head-node-enroot-pyxis-setup.sh
export COMPUTE_NODE_BOOTSTRAP_SCRIPT=s3://parallelcluster-123456789012-us-east-1/scripts/bootstrap/compute-node-enroot-pyxis-setup.sh
export AWS_ACCOUNT_ID=123456789012
export S3_BUCKET_NAME=parallelcluster-123456789012-us-east-1
export ECR_REPO_NAME=pytorch-training-custom
export ECR_REPO_URI=123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-training-custom
export IMAGE_TAG=latest
export TRAINING_IMAGE_URI=123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-training-custom:latest
export LUSTRE_DATA_DIR=/lustre/data
export LUSTRE_CHECKPOINT_DIR=/lustre/checkpoints
export LUSTRE_LOG_DIR=/lustre/logs
export LUSTRE_RESULTS_DIR=/lustre/results
```

---

### 5.6 S3 버킷 구조 최종 확인

```bash
# 전체 버킷 구조 확인
aws s3 ls s3://${S3_BUCKET_NAME}/ --recursive --human-readable --summarize
```

**예상 구조:**
```
2024-01-01 12:00:00    3.2 KiB scripts/bootstrap/head-node-enroot-pyxis-setup.sh
2024-01-01 12:00:00    2.8 KiB scripts/bootstrap/compute-node-enroot-pyxis-setup.sh
2024-01-01 12:00:00    1.2 KiB data/sample/README.txt
                           PRE checkpoints/
                           PRE logs/
                           PRE results/

Total Objects: 3
   Total Size: 7.2 KiB
```

---

## 다음 단계

✅ 사전 요구사항 준비가 완료되었습니다!

이제 **[2. ParallelCluster 배포](./02-pcluster-deployment.md)** 로 진행하여 클러스터를 생성하세요.

---

## 📚 네비게이션

| 이전 | 상위 | 다음 |
|------|------|------|
| [◀ README](../README.md) | [📑 목차](../README.md#-가이드-목차) | [클러스터 배포 ▶](./02-pcluster-deployment.md) |
