## 2. ParallelCluster 배포

> 💡 **목표:** AWS ParallelCluster를 생성하고 Slurm 스케줄러를 설정합니다.

⏱️ **예상 소요 시간:** 30-40분

## 목차

- [개요](#개요)
- [2.1 클러스터 설정 파일 준비](#21-클러스터-설정-파일-준비)
- [2.2 클러스터 생성](#22-클러스터-생성)
- [2.3 클러스터 접속 및 검증](#23-클러스터-접속-및-검증)
- [2.4 Slurm 기본 사용](#24-slurm-기본-사용)
- [다음 단계](#다음-단계)

---

## 개요

이 문서에서는 다음 작업을 수행합니다:

- ✅ ParallelCluster 설정 파일 작성
- ✅ 클러스터 생성 및 검증
- ✅ Slurm 기본 명령어 사용 (nvidia-smi w/ srun)

---

## 2.1 클러스터 설정 파일 준비

ParallelCluster 생성을 위한 YAML 설정 파일을 준비합니다.

### 환경 변수 확인

먼저 이전 단계에서 설정한 환경 변수들이 로드되어 있는지 확인합니다:

```bash
# 환경 변수 로드
source ~/pcluster-env.sh

# 주요 변수 확인
echo "Region: ${AWS_REGION}"
echo "VPC ID: ${VPC_ID}"
echo "Public Subnet: ${PUBLIC_SUBNET_ID}"
echo "Private Subnet: ${PRIVATE_SUBNET_ID}"
echo "Security Group: ${SECURITY_GROUP_ID}"
echo "FSx Lustre ID: ${FSX_LUSTRE_ID}"
echo "FSx OpenZFS Volume ID: ${FSX_OPENZFS_ROOT_VOLUME_ID}"
echo "Head Node Bootstrap: ${HEAD_NODE_BOOTSTRAP_SCRIPT}"
echo "Compute Node Bootstrap: ${COMPUTE_NODE_BOOTSTRAP_SCRIPT}"
```

### 클러스터 설정 파일 생성

환경 변수를 사용하여 클러스터 설정 파일을 생성합니다:

> 📝 **템플릿 파일 참조:**
> - 전체 설정 파일 템플릿은 [examples/templates/cluster-config.yaml.template](../examples/templates/cluster-config.yaml.template)에서 확인할 수 있습니다.
> - 아래 명령은 환경 변수를 사용하여 템플릿을 실제 설정 파일로 변환합니다.

```bash
# 설정 파일 디렉토리로 이동
cd ~/distributed-training-on-aws/pcluster-container
mkdir -p examples/configs

# 인스턴스 타입 및 수량 설정 (필요시 변경)
export COMPUTE_INSTANCE_TYPE=g5.8xlarge
export COMPUTE_MIN_COUNT=2
export COMPUTE_MAX_COUNT=2

# 클러스터 설정 파일 생성
cat > examples/configs/cluster-config.yaml << EOF
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
Region: ${AWS_REGION}

DevSettings:
  Timeouts:
    HeadNodeBootstrapTimeout: 43200  # 12 hours
    ComputeNodeBootstrapTimeout: 7200  # 2 hours

Imds:
  ImdsSupport: v2.0

Image:
  Os: ubuntu2204

HeadNode:
  InstanceType: m5.8xlarge
  Networking:
    SubnetId: ${PUBLIC_SUBNET_ID}
    ElasticIp: false
    AdditionalSecurityGroups:
      - ${SECURITY_GROUP_ID}
  LocalStorage:
    RootVolume:
      Size: 500
      DeleteOnTermination: true  # Root and /home volume for users
  Iam:
    AdditionalIamPolicies:
      # Grant ECR, SSM and S3 access
      - Policy: arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      - Policy: arn:aws:iam::aws:policy/AmazonS3FullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess
  CustomActions:
    OnNodeConfigured:
      Sequence:
        - Script: 'https://raw.githubusercontent.com/aws-samples/aws-parallelcluster-post-install-scripts/main/docker/postinstall.sh'
        - Script: '${HEAD_NODE_BOOTSTRAP_SCRIPT}'

Scheduling:
  Scheduler: slurm
  SlurmSettings:
    ScaledownIdletime: -1  # Disable automatic scale-down
    QueueUpdateStrategy: DRAIN
    CustomSlurmSettings:
      # Simple accounting to text file
      - JobCompType: jobcomp/filetxt
      - JobCompLoc: /home/slurm/slurm-job-completions.txt
      - JobAcctGatherType: jobacct_gather/linux
      # Increase timeout before marking node as DOWN
      - SlurmdTimeout: 1800
      - ResumeTimeout: 1800
      - SuspendTimeout: 300
      - ReturnToService: 2
  SlurmQueues:
    - Name: compute-gpu
      CapacityType: ONDEMAND
      Networking:
        SubnetIds:
          - ${PRIVATE_SUBNET_ID}
        PlacementGroup:
          Enabled: true  # Capacity Reservation 사용 시 false로 변경
        AdditionalSecurityGroups:
          - ${SECURITY_GROUP_ID}
      ComputeSettings:
        LocalStorage:
          EphemeralVolume:
            MountDir: /scratch  # Local NVMe scratch space
          RootVolume:
            Size: 512
      JobExclusiveAllocation: true  # Each job gets exclusive access to nodes
      ComputeResources:
        - Name: distributed-ml
          InstanceType: ${COMPUTE_INSTANCE_TYPE}
          MinCount: ${COMPUTE_MIN_COUNT}
          MaxCount: ${COMPUTE_MAX_COUNT}
          # Capacity Reservation 사용 시 아래 주석 해제
          # CapacityReservationTarget:
          #   CapacityReservationId: cr-0a1f6b92ded769450  # Replace with your Capacity Reservation ID
          Efa:
            Enabled: true
            #GdrSupport: true  # p4d/p5 인스턴스만 지원
      Iam:
        AdditionalIamPolicies:
          - Policy: arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
          - Policy: arn:aws:iam::aws:policy/AmazonS3FullAccess
          - Policy: arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess
          - Policy: arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess
      CustomActions:
        OnNodeConfigured:
          Sequence:
            - Script: 'https://raw.githubusercontent.com/aws-samples/aws-parallelcluster-post-install-scripts/main/docker/postinstall.sh'
            - Script: '${COMPUTE_NODE_BOOTSTRAP_SCRIPT}'

SharedStorage:
  - Name: shared-workspace-zfs
    StorageType: FsxOpenZfs
    MountDir: /fsx
    FsxOpenZfsSettings:
      VolumeId: ${FSX_OPENZFS_ROOT_VOLUME_ID}

  - Name: fsx-lustre
    MountDir: /lustre
    StorageType: FsxLustre
    FsxLustreSettings:
      FileSystemId: ${FSX_LUSTRE_ID}

Monitoring:
  DetailedMonitoring: true
  Logs:
    CloudWatch:
      Enabled: true
  Dashboards:
    CloudWatch:
      Enabled: true
EOF

echo "✅ Cluster configuration file created: examples/configs/cluster-config.yaml"
```

### 설정 파일 주요 구성 요소

**HeadNode 설정:**
- **InstanceType**: `m5.8xlarge` - 32 vCPU, 128GB RAM (Slurm 컨트롤러용)
- **SubnetId**: Public 서브넷 사용 (Session Manager 접속용)
- **RootVolume**: 500GB (사용자 홈 디렉토리 포함)
- **CustomActions**: Docker 및 Enroot/Pyxis 설치 스크립트

**Compute Node 설정:**
- **InstanceType**: 환경 변수로 설정 (기본: `g5.8xlarge`)
- **SubnetId**: Private 서브넷
- **MinCount/MaxCount**: 환경 변수로 조정 가능
- **EFA**: 활성화 (고성능 네트워킹)
- **LocalStorage**: 
  - `/scratch`: NVMe 임시 스토리지
  - Root Volume: 512GB
- **CustomActions**: Docker 및 Enroot/Pyxis 설치 스크립트

**SharedStorage:**
- **FSx OpenZFS** (`/fsx`): Home 디렉토리 및 사용자 데이터
- **FSx Lustre** (`/lustre`): 학습 데이터셋
  - 기존 FSx Lustre 파일 시스템을 사용 (`FileSystemId`로 참조)
  - **Data Repository Association (DRA)**은 이미 01-prerequisites.md에서 설정됨
  - 클러스터가 마운트하면 기존 DRA 설정이 자동으로 적용됨:
    - `/lustre/data` ↔ `s3://${S3_BUCKET_NAME}/data/`
    - `/lustre/checkpoints` ↔ `s3://${S3_BUCKET_NAME}/checkpoints/`
    - `/lustre/logs` ↔ `s3://${S3_BUCKET_NAME}/logs/`
    - `/lustre/results` ↔ `s3://${S3_BUCKET_NAME}/results/`

> 💡 **DRA는 FSx 레벨의 설정**이므로 ParallelCluster YAML에서 별도 설정이 필요 없습니다.

---

### Capacity Reservation 사용 (선택사항)

GPU 인스턴스 가용성을 보장하기 위해 Capacity Reservation을 사용할 수 있습니다.

#### Capacity Reservation 생성 (AWS Console 또는 CLI)

```bash
# Capacity Reservation 생성 예시
aws ec2 create-capacity-reservation \
  --instance-type g5.12xlarge \
  --instance-platform Linux/UNIX \
  --availability-zone ${PRIMARY_AZ} \
  --instance-count 2 \
  --instance-match-criteria targeted \
  --region ${AWS_REGION}
```

#### 설정 파일 수정

Capacity Reservation을 사용하려면 설정 파일에서 다음을 수정:

1. **PlacementGroup 비활성화**:
```yaml
PlacementGroup:
  Enabled: false  # Capacity Reservation과 함께 사용 불가
```

2. **CapacityReservationTarget 추가**:
```yaml
ComputeResources:
  - Name: distributed-ml
    InstanceType: ${COMPUTE_INSTANCE_TYPE}
    MinCount: 2  # Reservation 수량과 일치
    MaxCount: 2
    CapacityReservationTarget:
      CapacityReservationId: cr-0123456789abcdef0  # 실제 ID로 변경
```

> ⚠️ **주의:** Capacity Reservation 사용 시 MinCount를 Reservation 수량에 맞춰 설정해야 합니다.

---

### 설정 파일 확인

생성된 설정 파일을 확인합니다:

```bash
# 설정 파일 내용 확인
cat examples/configs/cluster-config.yaml

> ⚠️ **주의:**
> - 환경 변수가 제대로 치환되었는지 꼭 확인하세요.

---

## 2.2 클러스터 생성

### 클러스터 이름 설정

```bash
export CLUSTER_NAME=ml-training-cluster
```

### 클러스터 생성 시작

```bash
# 클러스터 생성
pcluster create-cluster \
  --cluster-name ${CLUSTER_NAME} \
  --cluster-configuration examples/configs/cluster-config.yaml \
  --region ${AWS_REGION}
```

**예상 출력:**
```json
{
  "cluster": {
    "clusterName": "ml-training-cluster",
    "cloudformationStackStatus": "CREATE_IN_PROGRESS",
    "cloudformationStackArn": "arn:aws:cloudformation:us-east-1:123456789012:stack/ml-training-cluster/883840a0-cd49-11f0-8ba1-0edd122729eb",
    "region": "us-east-1",
    "version": "3.14.0",
    "clusterStatus": "CREATE_IN_PROGRESS",
    "scheduler": {
      "type": "slurm"
    }
  },
  "validationMessages": [
    {
      "level": "WARNING",
      "type": "DetailedMonitoringValidator",
      "message": "Detailed Monitoring is enabled for EC2 instances in your compute fleet. The Amazon EC2 console will display monitoring graphs with a 1-minute period for these instances. Note that this will increase the cost. If you want to avoid this and use basic monitoring instead, please set `Monitoring / DetailedMonitoring` to false."
    },
    {
      "level": "WARNING",
      "type": "KeyPairValidator",
      "message": "If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in"
    }
  ]
}
```

### 클러스터 생성 상태 모니터링

```bash
# 클러스터 상태 확인
pcluster describe-cluster \
  --cluster-name ${CLUSTER_NAME} \
  --region ${AWS_REGION} \
  --query 'clusterStatus'
```

**예상 상태:**
- `CREATE_IN_PROGRESS`: 생성 중
- `CREATE_COMPLETE`: 생성 완료 ✅
- `CREATE_FAILED`: 생성 실패 ❌

> ⏱️ **예상 소요 시간: 약 25-35분**

### CloudFormation 스택 확인

```bash
# CloudFormation 스택 이벤트 확인
aws cloudformation describe-stack-events \
  --stack-name ${CLUSTER_NAME} \
  --region ${AWS_REGION} \
  --max-items 10 \
  --query 'StackEvents[*].[Timestamp,ResourceStatus,ResourceType,LogicalResourceId]' \
  --output table
```

---

## 2.3 클러스터 접속 및 검증

클러스터 생성이 완료되면 Head Node에 접속하여 환경을 확인합니다.

### Head Node 접속

Session Manager를 통해 Head Node에 접속합니다:

```bash
aws ssm start-session --target $(pcluster describe-cluster --region ${AWS_REGION} -n ${CLUSTER_NAME} | jq '.headNode.instanceId' | tr -d '"')
```

**예상 출력:**
```
$ aws ssm start-session --target $(pcluster describe-cluster --region ${AWS_REGION} -n ${CLUSTER_NAME} | jq '.headNode.instanceId' | tr -d '"')

Starting session with SessionId: i-06e9f603643fc3f26-alsudcf75qe2lzy5vdidhs825i
$ 
```

Ubuntu 사용자로 전환 합니다.
```bash
sudo su - ubuntu
```

> 💡 **Session Manager 사용:**
> - SSH 키 없이 안전하게 접속
> - IAM 기반 인증
> - 세션 로그 자동 기록

---

### ⚠️ FSx Lustre 마운트 문제 해결 (중요)

> 🚨 **현재 알려진 이슈 (2025.11.30 기준):**
> 
> Head Node의 Lustre 클라이언트 커널 모듈 버전과 실제 시스템 커널 버전이 일치하지 않아 
> FSx Lustre가 자동으로 마운트되지 않는 현상이 발생하고 있습니다.
> 
> 이는 Ubuntu 22.04 이미지의 커널 업데이트와 Lustre 클라이언트 패키지 버전 불일치로 인한 문제입니다.
> **현재는 수동으로 마운트를 진행해야 하며, 향후 업데이트 시 자동화 방법을 안내하겠습니다.**

#### 1. 마운트 상태 확인

먼저 FSx Lustre가 정상적으로 마운트되었는지 확인합니다:

```bash
# 마운트된 파일시스템 확인
df -h | grep lustre

# 또는 직접 디렉토리 접근 시도
ls -la /lustre
```

**정상적인 경우 (자동 마운트 성공):**
```
10.1.30.23@tcp:/czrc3amv  2.2T   16M  2.2T   1% /lustre
```

**문제가 있는 경우:**
```bash
ls: cannot open directory '/lustre': No such device
```

#### 2. 커널 및 Lustre 버전 불일치 확인

마운트가 실패한 경우, 커널 버전과 Lustre 모듈 버전을 확인합니다:

```bash
# 현재 실행 중인 커널 버전 확인
uname -r

# 설치된 Lustre 클라이언트 모듈 확인
dpkg -l | grep lustre
```

**예상 출력:**
```bash
# uname -r
6.8.0-1043-aws

# dpkg -l | grep lustre
ii  lustre-client-modules-6.8.0-1039-aws  2.15.6-1fsx21  amd64
```

> 📝 **문제 원인:** 
> - 시스템 커널: `6.8.0-1043-aws`
> - Lustre 모듈: `6.8.0-1039-aws`
> - **버전 불일치**로 인해 Lustre 모듈을 로드할 수 없음

#### 3. 올바른 Lustre 모듈 설치

현재 커널 버전에 맞는 Lustre 클라이언트 모듈을 설치합니다:

```bash
# rpm 패키지 관리 도구 설치 (필요 시)
sudo apt-get install -y rpm

# 현재 커널 버전에 맞는 Lustre 모듈 설치
sudo apt-get install -y lustre-client-modules-$(uname -r)
```

**예상 출력:**
```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  lustre-client-modules-6.8.0-1043-aws
0 upgraded, 1 newly installed, 0 to remove and 32 not upgraded.
Need to get 25.2 MB of archives.
After this operation, 128 MB of additional disk space will be used.
Get:1 https://fsx-lustre-client-repo.s3.amazonaws.com/ubuntu jammy/main amd64 lustre-client-modules-6.8.0-1043-aws amd64 2.15.6-1fsx25 [25.2 MB]
Fetched 25.2 MB in 0s (68.9 MB/s)
Selecting previously unselected package lustre-client-modules-6.8.0-1043-aws.
...
Setting up lustre-client-modules-6.8.0-1043-aws (2.15.6-1fsx25) ...
```

#### 4. Lustre 커널 모듈 로드

Lustre 파일시스템 모듈을 커널에 로드합니다:

```bash
# Lustre 모듈 로드
sudo modprobe lustre

# 모듈 로드 확인
lsmod | grep lustre
```

**예상 출력:**
```
lustre               1126400  0
mdc                   294912  1 lustre
lov                   356352  2 mdc,lustre
lmv                   229376  1 lustre
ptlrpc               1544192  7 fld,osc,fid,lov,mdc,lmv,lustre
obdclass             3399680  8 fld,osc,fid,ptlrpc,lov,mdc,lmv,lustre
lnet                  839680  6 osc,obdclass,ptlrpc,ksocklnd,lmv,lustre
libcfs                237568  11 fld,lnet,osc,fid,obdclass,ptlrpc,ksocklnd,lov,mdc,lmv,lustre
```

#### 5. 파일시스템 등록 확인

Lustre 파일시스템이 커널에 등록되었는지 확인합니다:

```bash
# 지원되는 파일시스템 확인
cat /proc/filesystems | grep lustre
```

**예상 출력:**
```
nodev   lustre
```

✅ `lustre`가 표시되면 정상입니다!

#### 6. FSx Lustre 마운트

이제 FSx Lustre를 수동으로 마운트합니다:

```bash
# Lustre 마운트
sudo mount /lustre

# 마운트 확인
df -h | grep lustre
```

**예상 출력:**
```
10.1.30.23@tcp:/czrc3amv  2.2T   16M  2.2T   1% /lustre
```

#### 7. Lustre 디렉토리 구조 확인

마운트가 성공하면 DRA로 연결된 디렉토리를 확인합니다:

```bash
# Lustre 디렉토리 확인
ls -la /lustre/
```

**예상 출력:**
```
total 167
drwxrwxrwt  8 root root 33280 Nov 29 17:27 .
drwxr-xr-x 23 root root  4096 Nov 29 17:50 ..
drwxrwxr-x  2 root root 33280 Nov 29 17:03 checkpoints
drwxrwxr-x  3 root root 33280 Nov 29 16:17 data
drwxrwxr-x  2 root root 33280 Nov 29 17:24 logs
drwxrwxr-x  2 root root 33280 Nov 29 17:27 results
```

✅ **마운트 성공!** 이제 정상적으로 FSx Lustre를 사용할 수 있습니다.

---

### 기본 환경 확인

Head Node에 접속한 후 다음 명령으로 환경을 확인합니다:

#### OS 정보

```bash
# OS 정보
cat /etc/os-release
```

**예상 출력:**
```
NAME="Ubuntu"
VERSION="22.04.x LTS (Jammy Jellyfish)"
ID=ubuntu
ID_LIKE=debian

...

```

#### 공유 스토리지 확인

```bash
# 마운트된 공유 스토리지 확인
df -h | grep -E 'fsx|lustre'

# 또는 전체 마운트 확인
mount | grep -E 'fsx|lustre'
```

**예상 출력:**
```
10.0.1.100@tcp:/fsvol-xxx  512G   64M  512G   1% /fsx
10.0.1.101@tcp:/yyyyyyy    1.2T  1.1M  1.2T   1% /lustre
```

#### WikiText-2 데이터셋 확인

```bash
# 01-prerequisites.md에서 업로드한 데이터 확인
ls -lh /lustre/data/wikitext-2/
```

**예상 출력:**
```
total 0
-rw-r--r-- 1 root root   43 Nov 29 16:49 dataset_dict.json
drwxr-xr-x 2 root root 4.0K Nov 29 16:49 test
drwxr-xr-x 2 root root 4.0K Nov 29 16:49 train
drwxr-xr-x 2 root root 4.0K Nov 29 16:49 validation
```

> 💡 **Lazy Loading:** 파일 메타데이터는 즉시 보이지만, 실제 데이터는 파일 접근 시 S3에서 로드됩니다.

#### Enroot 확인

```bash
# Enroot 버전 확인
enroot version

# Enroot 설정 확인
enroot list
```

**예상 출력:**
```
3.4.1
```

#### Pyxis 확인

```bash
# Pyxis 플러그인 확인
ls -la /usr/local/lib/slurm/

# Slurm 설정에서 Pyxis 확인
grep -i pyxis /opt/slurm/etc/plugstack.conf
```

**예상 출력:**
```
total 24
drwxr-xr-x 2 root root  4096 Nov 29 17:15 .
drwxr-xr-x 4 root root  4096 Nov 29 17:00 ..
-rwxr-xr-x 1 root root 14896 Nov 29 17:15 spank_pyxis.so

optional /usr/local/lib/slurm/spank_pyxis.so
```

---

## 2.4 Slurm 기본 사용

### Slurm 노드 상태 확인

```bash
# 노드 정보 확인
sinfo
```

**예상 출력:**
```
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
compute-gpu*  up   infinite      2  idle~ compute-gpu-distributed-ml-[1-4]
```

> 📝 **노드 상태:**
> - `idle~`: 유휴 상태, 필요 시 자동 프로비저닝
> - `alloc`: 작업에 할당됨
> - `mix`: 일부 리소스 사용 중
> - `down`: 사용 불가

### Slurm 파티션 확인

```bash
# 파티션 정보
scontrol show partition compute-gpu
```

### 간단한 nvidia-smi 테스트

Compute Node를 프로비저닝하고 GPU를 확인하는 간단한 테스트를 실행합니다:

```bash
# nvidia-smi 테스트 작업 제출
srun --partition=compute-gpu \
     --nodes=1 \
     --ntasks=1 \
     --gpus-per-node=1 \
     nvidia-smi
```

**예상 출력:**
```
TBU
```

### 작업 큐 확인

```bash
# 실행 중인 작업 확인
squeue

# 본인의 작업만 확인
squeue -u $USER

# 작업 상세 정보
scontrol show job <JOB_ID>
```

### Compute Node 상태 확인

```bash
# 프로비저닝된 노드 확인
sinfo

# 특정 노드 상세 정보
scontrol show node compute-gpu-distributed-ml-1
```

---

## 다음 단계

✅ ParallelCluster 배포가 완료되었습니다!

이제 **[3. 분산 학습 실행](./03-distributed-training.md)**으로 진행하여 실제 학습 작업을 실행하세요.

---

### 환경 변수 저장

```bash
# 클러스터 이름 저장
cat >> ~/pcluster-env.sh << EOF
export CLUSTER_NAME=${CLUSTER_NAME}
EOF
```

---

## 📚 네비게이션

| 이전 | 상위 | 다음 |
|------|------|------|
| [◀ 사전 요구사항](./01-prerequisites.md) | [📑 목차](../README.md#-가이드-목차) | [분산 학습 ▶](./03-distributed-training.md) |