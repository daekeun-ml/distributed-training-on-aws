# Multi Queue Test

## 시나리오 1: 큐(Queue) 동적 추가
**목적:** 기존 클러스터에 새로운 큐를 동적으로 추가할 수 있는지 검증

**검증 내용:**
- Queue 1이 운영 중인 클러스터에서 `pcluster update` 명령을 통해 Queue 2를 추가할 수 있는가?
- 단일 Capacity Reservation ID를 여러 Queue에서 공유하여 사용할 수 있는가?

#### Head Node에서 기존 Queue(Partition) 확인
```
$ sinfo
PARTITION    AVAIL  TIMELIMIT  NODES  STATE NODELIST
compute-gpu*    up   infinite      2   idle compute-gpu-st-distributed-ml-[1-2]
```

#### 기존 pcluster config(일부)

`QueueUpdateStrategy` 가 **TERMINATE** 로 설정 되어있어야 합니다.

```yaml
  SlurmSettings:
    ScaledownIdletime: -1 # Disable automatic scale-down
    QueueUpdateStrategy: TERMINATE
    # ... 나머지 설정

  SlurmQueues:
  - Name: compute-gpu
    CapacityType: CAPACITY_BLOCK
    Networking:
      SubnetIds:
      - subnet-xxxx
      PlacementGroup:
        Enabled: false
      AdditionalSecurityGroups:
      - sg-xxxx
    ComputeSettings:
      LocalStorage:
        EphemeralVolume:
          MountDir: /scratch # Local NVMe scratch space
        RootVolume:
          Size: 512
    JobExclusiveAllocation: true # Each job gets exclusive access to nodes
    ComputeResources:
    - Name: distributed-ml
      InstanceType: p5.48xlarge
      MinCount: 2
      MaxCount: 2
      # Capacity Reservation 사용 시 아래 주석 해제
      CapacityReservationTarget:
        CapacityReservationId: cr-xxxxxxxxxxxxxxxxx
      Efa:
        Enabled: true
        GdrSupport: true
```

#### pcluster config 변경
```yaml
  SlurmQueues:
  # ===== Queue 1: 기존 compute-gpu Queue (p5.48xlarge 2대 -> 1대) =====
  - Name: compute-gpu
    CapacityType: CAPACITY_BLOCK
    Networking:
      SubnetIds:
      - subnet-xxxx
      PlacementGroup:
        Enabled: false
      AdditionalSecurityGroups:
      - sg-xxxx
    ComputeSettings:
      LocalStorage:
        EphemeralVolume:
          MountDir: /scratch
        RootVolume:
          Size: 512
    JobExclusiveAllocation: true
    ComputeResources:
    - Name: distributed-ml
      InstanceType: p5.48xlarge
      MinCount: 1
      MaxCount: 1
      CapacityReservationTarget:
        CapacityReservationId: cr-xxxxxxxxxxxxxxxxx
      Efa:
        Enabled: true
        GdrSupport: true
    Iam:
      AdditionalIamPolicies:
      - Policy: arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      - Policy: arn:aws:iam::aws:policy/AmazonS3FullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess
    CustomActions:
      OnNodeConfigured:
        Sequence:
        - Script: SKIP

  # ===== Queue 2: compute-gpu-2 (p5.48xlarge 1대) =====
  - Name: compute-gpu-2
    CapacityType: CAPACITY_BLOCK
    Networking:
      SubnetIds:
      - subnet-xxxx
      PlacementGroup:
        Enabled: false
      AdditionalSecurityGroups:
      - sg-xxxx
    ComputeSettings:
      LocalStorage:
        EphemeralVolume:
          MountDir: /scratch
        RootVolume:
          Size: 512
    JobExclusiveAllocation: true
    ComputeResources:
    - Name: distributed-ml-2
      InstanceType: p5.48xlarge
      MinCount: 1
      MaxCount: 1
      CapacityReservationTarget:
        CapacityReservationId: cr-xxxxxxxxxxxxxxxxx  # 동일한 Capacity Reservation 사용
      Efa:
        Enabled: true
        GdrSupport: true
    Iam:
      AdditionalIamPolicies:
      - Policy: arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      - Policy: arn:aws:iam::aws:policy/AmazonS3FullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess
    CustomActions:
      OnNodeConfigured:
        Sequence:
        - Script: SKIP
```

#### pcluster update
```bash
# dry-run 으로 configuration validation
$ pcluster update-cluster -n ${CLUSTER_NAME} -r ${AWS_REGION} -c examples/configs/cluster-config.yaml  --dryrun 

# pcluster update 실행
$ pcluster update-cluster -n ${CLUSTER_NAME} -r ${AWS_REGION} -c examples/configs/cluster-config.yaml 
{
  "cluster": {
    "clusterName": "ml-training-cluster",
    "cloudformationStackStatus": "UPDATE_IN_PROGRESS",
    "cloudformationStackArn": "arn:aws:cloudformation:us-east-2:xxxx:stack/ml-training-cluster/xxxx",
    "region": "us-east-2",
    "version": "3.14.0",
    "clusterStatus": "UPDATE_IN_PROGRESS",
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
  ],
  "changeSet": [
    {
      "parameter": "Scheduling.SlurmQueues[compute-gpu].ComputeResources[distributed-ml].MaxCount",
      "requestedValue": "1",
      "currentValue": "2"
    },
    {
      "parameter": "Scheduling.SlurmQueues[compute-gpu].ComputeResources[distributed-ml].MinCount",
      "requestedValue": "1",
      "currentValue": "2"
    },
    {
      "parameter": "Scheduling.SlurmQueues",
      "requestedValue": "{'Name': 'compute-gpu-2', 'CapacityType': 'CAPACITY_BLOCK', 'Networking': {'SubnetIds': ['subnet-xxxx'], 'PlacementGroup': {'Enabled': False}, 'AdditionalSecurityGroups': ['sg-xxxx']}, 'ComputeSettings': {'LocalStorage': {'EphemeralVolume': {'MountDir': '/scratch'}, 'RootVolume': {'Size': 512}}}, 'JobExclusiveAllocation': True, 'ComputeResources': [{'Name': 'distributed-ml-2', 'InstanceType': 'p5.48xlarge', 'MinCount': 1, 'MaxCount': 1, 'CapacityReservationTarget': {'CapacityReservationId': 'cr-xxxxxxxxxxxxxxxxx'}, 'Efa': {'Enabled': True, 'GdrSupport': True}}], 'Iam': {'AdditionalIamPolicies': [{'Policy': 'arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore'}, {'Policy': 'arn:aws:iam::aws:policy/AmazonS3FullAccess'}, {'Policy': 'arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess'}, {'Policy': 'arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess'}]}, 'CustomActions': {'OnNodeConfigured': {'Sequence': [{'Script': 'https://raw.githubusercontent.com/aws-samples/aws-parallelcluster-post-install-scripts/main/docker/postinstall.sh'}, {'Script': 's3://..../scripts/bootstrap/compute-node-enroot-pyxis-setup.sh'}]}}}",
      "currentValue": "-"
    }
  ]
}
```

#### Head Node에서 추가 된 Queue 확인 + 기존 Queue에 줄어든 resource 확인

```
$ sinfo
PARTITION     AVAIL  TIMELIMIT  NODES  STATE NODELIST
compute-gpu*     up   infinite      1   idle compute-gpu-st-distributed-ml-1
compute-gpu-2    up   infinite      1   idle compute-gpu-2-st-distributed-ml-2-1
```

약 20분에서 30분 정도 시간이 소요 될 수 있습니다.


아래 시나리오가 검증 되었습니다!
- Queue 1이 운영 중인 클러스터에서 `pcluster update` 명령을 통해 Queue 2를 추가할 수 있는가? => YES
- 단일 Capacity Reservation ID를 여러 Queue에서 공유하여 사용할 수 있는가? => YES

## 시나리오 2: 큐 제거 및 리소스 재배치
**목적:** 큐 삭제 시 컴퓨트 노드 리소스를 다른 큐로 이관할 수 있는지 검증

**검증 내용:**
- 운영 중인 2개의 Queue 중 하나를 제거하면서, 해당 큐의 컴퓨트 노드 리소스를 남은 Queue로 추가 할 수 있는가?

#### 시나리오 1에서 만들었던 Queue 2를 제거하면서 Queue 1로 노드 하나 추가.

기존 cluster config
```yaml
Scheduling:
  Scheduler: slurm
  SlurmSettings:
    ScaledownIdletime: -1 # Disable automatic scale-down
    QueueUpdateStrategy: TERMINATE

# ... 나머지 설정

  SlurmQueues:
  # ===== Queue 1: compute-gpu (p5.48xlarge 1대) =====
  - Name: compute-gpu
    CapacityType: CAPACITY_BLOCK
    Networking:
      SubnetIds:
      - subnet-xxxx
      PlacementGroup:
        Enabled: false
      AdditionalSecurityGroups:
      - sg-xxxx
    ComputeSettings:
      LocalStorage:
        EphemeralVolume:
          MountDir: /scratch
        RootVolume:
          Size: 512
    JobExclusiveAllocation: true
    ComputeResources:
    - Name: distributed-ml
      InstanceType: p5.48xlarge
      MinCount: 1
      MaxCount: 1
      CapacityReservationTarget:
        CapacityReservationId: cr-xxxxxxxxxxxxxxxxx
      Efa:
        Enabled: true
        GdrSupport: true
    Iam:
      AdditionalIamPolicies:
      - Policy: arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      - Policy: arn:aws:iam::aws:policy/AmazonS3FullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess
    CustomActions:
      OnNodeConfigured:
        Sequence:
        - Script: SKIP

  # ===== Queue 2: compute-gpu-2 (p5.48xlarge 1대) =====
  - Name: compute-gpu-2
    CapacityType: CAPACITY_BLOCK
    Networking:
      SubnetIds:
      - subnet-xxxx
      PlacementGroup:
        Enabled: false
      AdditionalSecurityGroups:
      - sg-xxxx
    ComputeSettings:
      LocalStorage:
        EphemeralVolume:
          MountDir: /scratch
        RootVolume:
          Size: 512
    JobExclusiveAllocation: true
    ComputeResources:
    - Name: distributed-ml-2
      InstanceType: p5.48xlarge
      MinCount: 1
      MaxCount: 1
      CapacityReservationTarget:
        CapacityReservationId: cr-xxxxxxxxxxxxxxxxx # 동일한 Capacity Reservation 사용
      Efa:
        Enabled: true
        GdrSupport: true
    Iam:
      AdditionalIamPolicies:
      - Policy: arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      - Policy: arn:aws:iam::aws:policy/AmazonS3FullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess
    CustomActions:
      OnNodeConfigured:
        Sequence:
        - Script: SKIP
```

config 변경
```
Scheduling:
  Scheduler: slurm
  SlurmSettings:
    ScaledownIdletime: -1 # Disable automatic scale-down
    QueueUpdateStrategy: TERMINATE

# ... 나머지 설정

  SlurmQueues:
  # ===== Queue 1: compute-gpu (p5.48xlarge 1대 -> 2) =====
  - Name: compute-gpu
    CapacityType: CAPACITY_BLOCK
    Networking:
      SubnetIds:
      - subnet-xxxx
      PlacementGroup:
        Enabled: false
      AdditionalSecurityGroups:
      - sg-xxxx
    ComputeSettings:
      LocalStorage:
        EphemeralVolume:
          MountDir: /scratch
        RootVolume:
          Size: 512
    JobExclusiveAllocation: true
    ComputeResources:
    - Name: distributed-ml
      InstanceType: p5.48xlarge
      MinCount: 2
      MaxCount: 2
      CapacityReservationTarget:
        CapacityReservationId: cr-xxxxxxxxxxxxxxxxx
      Efa:
        Enabled: true
        GdrSupport: true
    Iam:
      AdditionalIamPolicies:
      - Policy: arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      - Policy: arn:aws:iam::aws:policy/AmazonS3FullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess
      - Policy: arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess
    CustomActions:
      OnNodeConfigured:
        Sequence:
        - Script: SKIP

  # ===== Queue 2: compute-gpu-2 삭제 =====
```

pcluster update
```
# dry-run 으로 configuration validation
$ pcluster update-cluster -n ${CLUSTER_NAME} -r ${AWS_REGION} -c examples/configs/cluster-config.yaml --dryrun true
{
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
  ],
  "message": "Request would have succeeded, but DryRun flag is set.",
  "changeSet": [
    {
      "parameter": "Scheduling.SlurmQueues[compute-gpu].ComputeResources[distributed-ml].MaxCount",
      "requestedValue": "2",
      "currentValue": "1"
    },
    {
      "parameter": "Scheduling.SlurmQueues[compute-gpu].ComputeResources[distributed-ml].MinCount",
      "requestedValue": "2",
      "currentValue": "1"
    },
    {
      "parameter": "Scheduling.SlurmQueues",
      "requestedValue": "-",
      "currentValue": "{'Name': 'compute-gpu-2', 'CapacityType': 'CAPACITY_BLOCK', 'Networking': {'SubnetIds': ['subnet-xxxx'], 'PlacementGroup': {'Enabled': False}, 'AdditionalSecurityGroups': ['sg-xxxx']}, 'ComputeSettings': {'LocalStorage': {'EphemeralVolume': {'MountDir': '/scratch'}, 'RootVolume': {'Size': 512}}}, 'JobExclusiveAllocation': True, 'ComputeResources': [{'Name': 'distributed-ml-2', 'InstanceType': 'p5.48xlarge', 'MinCount': 1, 'MaxCount': 1, 'CapacityReservationTarget': {'CapacityReservationId': 'cr-xxxxxxxxxxxxx'}, 'Efa': {'Enabled': True, 'GdrSupport': True}}], 'Iam': {'AdditionalIamPolicies': [{'Policy': 'arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore'}, {'Policy': 'arn:aws:iam::aws:policy/AmazonS3FullAccess'}, {'Policy': 'arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess'}, {'Policy': 'arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess'}]}, 'CustomActions': {'OnNodeConfigured': {'Sequence': [{'Script': 'https://raw.githubusercontent.com/aws-samples/aws-parallelcluster-post-install-scripts/main/docker/postinstall.sh'}, {'Script': 's3://.../scripts/bootstrap/compute-node-enroot-pyxis-setup.sh'}]}}}"
    }
  ]
}

# pcluster update 실행
$ pcluster update-cluster -n ${CLUSTER_NAME} -r ${AWS_REGION} -c examples/configs/cluster-config.yaml              
{
  "cluster": {
    "clusterName": "ml-training-cluster",
    "cloudformationStackStatus": "UPDATE_IN_PROGRESS",
    "cloudformationStackArn": "arn:aws:cloudformation:us-east-2:xxxx:stack/ml-training-cluster/xxxx",
    "region": "us-east-2",
    "version": "3.14.0",
    "clusterStatus": "UPDATE_IN_PROGRESS",
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
  ],
  "changeSet": [
    {
      "parameter": "Scheduling.SlurmQueues[compute-gpu].ComputeResources[distributed-ml].MaxCount",
      "requestedValue": "2",
      "currentValue": "1"
    },
    {
      "parameter": "Scheduling.SlurmQueues[compute-gpu].ComputeResources[distributed-ml].MinCount",
      "requestedValue": "2",
      "currentValue": "1"
    },
    {
      "parameter": "Scheduling.SlurmQueues",
      "requestedValue": "-",
      "currentValue": "{'Name': 'compute-gpu-2', 'CapacityType': 'CAPACITY_BLOCK', 'Networking': {'SubnetIds': ['subnet-xxxx'], 'PlacementGroup': {'Enabled': False}, 'AdditionalSecurityGroups': ['sg-xxxx']}, 'ComputeSettings': {'LocalStorage': {'EphemeralVolume': {'MountDir': '/scratch'}, 'RootVolume': {'Size': 512}}}, 'JobExclusiveAllocation': True, 'ComputeResources': [{'Name': 'distributed-ml-2', 'InstanceType': 'p5.48xlarge', 'MinCount': 1, 'MaxCount': 1, 'CapacityReservationTarget': {'CapacityReservationId': 'cr-xxxxxxxxxxxxx'}, 'Efa': {'Enabled': True, 'GdrSupport': True}}], 'Iam': {'AdditionalIamPolicies': [{'Policy': 'arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore'}, {'Policy': 'arn:aws:iam::aws:policy/AmazonS3FullAccess'}, {'Policy': 'arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess'}, {'Policy': 'arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess'}]}, 'CustomActions': {'OnNodeConfigured': {'Sequence': [{'Script': 'https://raw.githubusercontent.com/aws-samples/aws-parallelcluster-post-install-scripts/main/docker/postinstall.sh'}, {'Script': 's3://.../scripts/bootstrap/compute-node-enroot-pyxis-setup.sh'}]}}}"
    }
  ]
}

```

Head Node에서 cluster 확인 
```bash
$ sinfo
PARTITION    AVAIL  TIMELIMIT  NODES  STATE NODELIST
compute-gpu*    up   infinite      2   idle compute-gpu-st-distributed-ml-[1-2]
```

약 20분에서 30분 정도 시간이 소요 될 수 있습니다.


아래 시나리오가 검증 되었습니다!
- 운영 중인 2개의 Queue 중 하나를 제거하면서, 해당 큐의 컴퓨트 노드 리소스를 남은 Queue로 추가 할 수 있는가? => YES

