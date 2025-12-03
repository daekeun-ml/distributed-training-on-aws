
---
# 수행 일자 : 2025.12.02
## p5e.48xlarge NCCL Tests 결과 (Single Node)

### 환경
- ap-southeast-2(Sydney) 리전
- p5e.48xlarge x 1대 
- Lustre Persist_V1
- All Recude 연산

### 결과
```bash
$ tail -f nccl-all_reduce_perf_21.out 
compute-gpu-st-distributed-ml-1: i-0a59d0ef2fec95909
--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

# Collective test starting: all_reduce_perf
# nThread 1 nGpus 1 minBytes 8 maxBytes 17179869184 step: 2(factor) warmup iters: 1 iters: 100 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid  32159 on compute-gpu-st-distributed-ml-1 device  0 [0000:53:00] NVIDIA H200
#  Rank  1 Group  0 Pid  32160 on compute-gpu-st-distributed-ml-1 device  1 [0000:64:00] NVIDIA H200
#  Rank  2 Group  0 Pid  32161 on compute-gpu-st-distributed-ml-1 device  2 [0000:75:00] NVIDIA H200
#  Rank  3 Group  0 Pid  32162 on compute-gpu-st-distributed-ml-1 device  3 [0000:86:00] NVIDIA H200
#  Rank  4 Group  0 Pid  32163 on compute-gpu-st-distributed-ml-1 device  4 [0000:97:00] NVIDIA H200
#  Rank  5 Group  0 Pid  32164 on compute-gpu-st-distributed-ml-1 device  5 [0000:a8:00] NVIDIA H200
#  Rank  6 Group  0 Pid  32165 on compute-gpu-st-distributed-ml-1 device  6 [0000:b9:00] NVIDIA H200
#  Rank  7 Group  0 Pid  32166 on compute-gpu-st-distributed-ml-1 device  7 [0000:ca:00] NVIDIA H200
compute-gpu-st-distributed-ml-1:32159:32159 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:32159:32159 [0] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:32159:32159 [0] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:32163:32163 [4] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:32161:32161 [2] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:32162:32162 [3] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:32165:32165 [6] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:32160:32160 [1] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:32164:32164 [5] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:32166:32166 [7] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:32161:32161 [2] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:32163:32163 [4] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:32165:32165 [6] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:32159:32159 [0] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:32160:32160 [1] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:32162:32162 [3] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:32164:32164 [5] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:32166:32166 [7] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:32163:32163 [4] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:32163:32163 [4] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:32161:32161 [2] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:32161:32161 [2] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:32162:32162 [3] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:32164:32164 [5] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:32164:32164 [5] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:32165:32165 [6] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:32165:32165 [6] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:32166:32166 [7] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:32166:32166 [7] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:32160:32160 [1] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:32160:32160 [1] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:32162:32162 [3] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/147 to environment
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO DMA-BUF is available on GPU device 0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO ncclCommInitRank comm 0x5df33bf07b40 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0x6c13ed52155019e2 - Init START
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO DMA-BUF is available on GPU device 2
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO ncclCommInitRank comm 0x64e618ee9620 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x6c13ed52155019e2 - Init START
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO DMA-BUF is available on GPU device 1
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO ncclCommInitRank comm 0x5f4ac174e750 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x6c13ed52155019e2 - Init START
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO DMA-BUF is available on GPU device 6
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO DMA-BUF is available on GPU device 7
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO ncclCommInitRank comm 0x6519761ad730 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0x6c13ed52155019e2 - Init START
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO DMA-BUF is available on GPU device 4
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO ncclCommInitRank comm 0x62a62e903510 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x6c13ed52155019e2 - Init START
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO DMA-BUF is available on GPU device 5
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO ncclCommInitRank comm 0x60ff9b8389e0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x6c13ed52155019e2 - Init START
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO DMA-BUF is available on GPU device 3
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO ncclCommInitRank comm 0x5b30f9f29650 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x6c13ed52155019e2 - Init START
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO ncclCommInitRank comm 0x64c37e929310 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0x6c13ed52155019e2 - Init START
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Bootstrap timings total 0.812049 (create 0.000049, send 0.000147, recv 0.701821, ring 0.005957, delay 0.000001)
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO Bootstrap timings total 0.110407 (create 0.000048, send 0.000172, recv 0.000216, ring 0.109564, delay 0.000001)
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO Bootstrap timings total 0.187206 (create 0.000055, send 0.000158, recv 0.186276, ring 0.000297, delay 0.000001)
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO Bootstrap timings total 0.001162 (create 0.000046, send 0.000128, recv 0.000357, ring 0.000234, delay 0.000001)
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO Bootstrap timings total 0.002296 (create 0.000055, send 0.000183, recv 0.001128, ring 0.000227, delay 0.000001)
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO Bootstrap timings total 0.001287 (create 0.000045, send 0.000161, recv 0.000209, ring 0.000514, delay 0.000000)
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO Bootstrap timings total 0.015722 (create 0.000052, send 0.000146, recv 0.009061, ring 0.000545, delay 0.000001)
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO Bootstrap timings total 0.006831 (create 0.000053, send 0.000143, recv 0.000229, ring 0.005939, delay 0.000001)
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO MNNVL busId 0x64000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO MNNVL busId 0x75000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO MNNVL busId 0x86000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO MNNVL busId 0x97000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO MNNVL busId 0x53000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO MNNVL busId 0xb9000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO MNNVL busId 0xca000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO MNNVL busId 0xa8000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/147
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO Setting affinity for GPU 3 to 0-23,96-119
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NVLS multicast support is available on dev 3 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO Setting affinity for GPU 2 to 0-23,96-119
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NVLS multicast support is available on dev 2 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Setting affinity for GPU 0 to 24-47,120-143
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NVLS multicast support is available on dev 0 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO Setting affinity for GPU 1 to 24-47,120-143
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NVLS multicast support is available on dev 1 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO Setting affinity for GPU 4 to 72-95,168-191
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NVLS multicast support is available on dev 4 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO Setting affinity for GPU 7 to 48-71,144-167
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NVLS multicast support is available on dev 7 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO Setting affinity for GPU 5 to 72-95,168-191
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NVLS multicast support is available on dev 5 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO Setting affinity for GPU 6 to 48-71,144-167
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NVLS multicast support is available on dev 6 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO comm 0x5f4ac174e750 rank 1 nRanks 8 nNodes 1 localRanks 8 localRank 1 MNNVL 0
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO comm 0x64e618ee9620 rank 2 nRanks 8 nNodes 1 localRanks 8 localRank 2 MNNVL 0
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO comm 0x64c37e929310 rank 3 nRanks 8 nNodes 1 localRanks 8 localRank 3 MNNVL 0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO comm 0x60ff9b8389e0 rank 4 nRanks 8 nNodes 1 localRanks 8 localRank 4 MNNVL 0
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO Trees [0] 5/-1/-1->4->7 [1] 5/-1/-1->4->7 [2] 5/-1/-1->4->7 [3] 5/-1/-1->4->7 [4] 5/-1/-1->4->7 [5] 5/-1/-1->4->7 [6] 5/-1/-1->4->7 [7] 5/-1/-1->4->7 [8] 5/-1/-1->4->7 [9] 5/-1/-1->4->7 [10] 5/-1/-1->4->7 [11] 5/-1/-1->4->7 [12] 5/-1/-1->4->7 [13] 5/-1/-1->4->7 [14] 5/-1/-1->4->7 [15] 5/-1/-1->4->7 [16] 5/-1/-1->4->7 [17] 5/-1/-1->4->7 [18] 5/-1/-1->4->7 [19] 5/-1/-1->4->7 [20] 5/-1/-1->4->7 [21] 5/-1/-1->4->7 [22] 5/-1/-1->4->7 [23] 5/-1/-1->4->7
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO comm 0x5b30f9f29650 rank 5 nRanks 8 nNodes 1 localRanks 8 localRank 5 MNNVL 0
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO Trees [0] -1/-1/-1->5->4 [1] -1/-1/-1->5->4 [2] -1/-1/-1->5->4 [3] -1/-1/-1->5->4 [4] -1/-1/-1->5->4 [5] -1/-1/-1->5->4 [6] -1/-1/-1->5->4 [7] -1/-1/-1->5->4 [8] -1/-1/-1->5->4 [9] -1/-1/-1->5->4 [10] -1/-1/-1->5->4 [11] -1/-1/-1->5->4 [12] -1/-1/-1->5->4 [13] -1/-1/-1->5->4 [14] -1/-1/-1->5->4 [15] -1/-1/-1->5->4 [16] -1/-1/-1->5->4 [17] -1/-1/-1->5->4 [18] -1/-1/-1->5->4 [19] -1/-1/-1->5->4 [20] -1/-1/-1->5->4 [21] -1/-1/-1->5->4 [22] -1/-1/-1->5->4 [23] -1/-1/-1->5->4
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO comm 0x6519761ad730 rank 6 nRanks 8 nNodes 1 localRanks 8 localRank 6 MNNVL 0
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO Trees [0] 7/-1/-1->6->1 [1] 7/-1/-1->6->1 [2] 7/-1/-1->6->1 [3] 7/-1/-1->6->1 [4] 7/-1/-1->6->1 [5] 7/-1/-1->6->1 [6] 7/-1/-1->6->1 [7] 7/-1/-1->6->1 [8] 7/-1/-1->6->1 [9] 7/-1/-1->6->1 [10] 7/-1/-1->6->1 [11] 7/-1/-1->6->1 [12] 7/-1/-1->6->1 [13] 7/-1/-1->6->1 [14] 7/-1/-1->6->1 [15] 7/-1/-1->6->1 [16] 7/-1/-1->6->1 [17] 7/-1/-1->6->1 [18] 7/-1/-1->6->1 [19] 7/-1/-1->6->1 [20] 7/-1/-1->6->1 [21] 7/-1/-1->6->1 [22] 7/-1/-1->6->1 [23] 7/-1/-1->6->1
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO comm 0x62a62e903510 rank 7 nRanks 8 nNodes 1 localRanks 8 localRank 7 MNNVL 0
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO Trees [0] 4/-1/-1->7->6 [1] 4/-1/-1->7->6 [2] 4/-1/-1->7->6 [3] 4/-1/-1->7->6 [4] 4/-1/-1->7->6 [5] 4/-1/-1->7->6 [6] 4/-1/-1->7->6 [7] 4/-1/-1->7->6 [8] 4/-1/-1->7->6 [9] 4/-1/-1->7->6 [10] 4/-1/-1->7->6 [11] 4/-1/-1->7->6 [12] 4/-1/-1->7->6 [13] 4/-1/-1->7->6 [14] 4/-1/-1->7->6 [15] 4/-1/-1->7->6 [16] 4/-1/-1->7->6 [17] 4/-1/-1->7->6 [18] 4/-1/-1->7->6 [19] 4/-1/-1->7->6 [20] 4/-1/-1->7->6 [21] 4/-1/-1->7->6 [22] 4/-1/-1->7->6 [23] 4/-1/-1->7->6
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO comm 0x5df33bf07b40 rank 0 nRanks 8 nNodes 1 localRanks 8 localRank 0 MNNVL 0
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 00/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 01/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 02/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 03/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 04/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 05/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 06/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 07/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 08/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 09/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 10/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 11/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 12/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 13/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 14/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 15/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO Trees [0] 6/-1/-1->1->0 [1] 6/-1/-1->1->0 [2] 6/-1/-1->1->0 [3] 6/-1/-1->1->0 [4] 6/-1/-1->1->0 [5] 6/-1/-1->1->0 [6] 6/-1/-1->1->0 [7] 6/-1/-1->1->0 [8] 6/-1/-1->1->0 [9] 6/-1/-1->1->0 [10] 6/-1/-1->1->0 [11] 6/-1/-1->1->0 [12] 6/-1/-1->1->0 [13] 6/-1/-1->1->0 [14] 6/-1/-1->1->0 [15] 6/-1/-1->1->0 [16] 6/-1/-1->1->0 [17] 6/-1/-1->1->0 [18] 6/-1/-1->1->0 [19] 6/-1/-1->1->0 [20] 6/-1/-1->1->0 [21] 6/-1/-1->1->0 [22] 6/-1/-1->1->0 [23] 6/-1/-1->1->0
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO Trees [0] 3/-1/-1->2->-1 [1] 3/-1/-1->2->-1 [2] 3/-1/-1->2->-1 [3] 3/-1/-1->2->-1 [4] 3/-1/-1->2->-1 [5] 3/-1/-1->2->-1 [6] 3/-1/-1->2->-1 [7] 3/-1/-1->2->-1 [8] 3/-1/-1->2->-1 [9] 3/-1/-1->2->-1 [10] 3/-1/-1->2->-1 [11] 3/-1/-1->2->-1 [12] 3/-1/-1->2->-1 [13] 3/-1/-1->2->-1 [14] 3/-1/-1->2->-1 [15] 3/-1/-1->2->-1 [16] 3/-1/-1->2->-1 [17] 3/-1/-1->2->-1 [18] 3/-1/-1->2->-1 [19] 3/-1/-1->2->-1 [20] 3/-1/-1->2->-1 [21] 3/-1/-1->2->-1 [22] 3/-1/-1->2->-1 [23] 3/-1/-1->2->-1
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO Trees [0] 0/-1/-1->3->2 [1] 0/-1/-1->3->2 [2] 0/-1/-1->3->2 [3] 0/-1/-1->3->2 [4] 0/-1/-1->3->2 [5] 0/-1/-1->3->2 [6] 0/-1/-1->3->2 [7] 0/-1/-1->3->2 [8] 0/-1/-1->3->2 [9] 0/-1/-1->3->2 [10] 0/-1/-1->3->2 [11] 0/-1/-1->3->2 [12] 0/-1/-1->3->2 [13] 0/-1/-1->3->2 [14] 0/-1/-1->3->2 [15] 0/-1/-1->3->2 [16] 0/-1/-1->3->2 [17] 0/-1/-1->3->2 [18] 0/-1/-1->3->2 [19] 0/-1/-1->3->2 [20] 0/-1/-1->3->2 [21] 0/-1/-1->3->2 [22] 0/-1/-1->3->2 [23] 0/-1/-1->3->2
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 16/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 17/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 18/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 19/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 20/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 21/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 22/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Channel 23/24 : 0 1 6 7 4 5 2 3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Trees [0] 1/-1/-1->0->3 [1] 1/-1/-1->0->3 [2] 1/-1/-1->0->3 [3] 1/-1/-1->0->3 [4] 1/-1/-1->0->3 [5] 1/-1/-1->0->3 [6] 1/-1/-1->0->3 [7] 1/-1/-1->0->3 [8] 1/-1/-1->0->3 [9] 1/-1/-1->0->3 [10] 1/-1/-1->0->3 [11] 1/-1/-1->0->3 [12] 1/-1/-1->0->3 [13] 1/-1/-1->0->3 [14] 1/-1/-1->0->3 [15] 1/-1/-1->0->3 [16] 1/-1/-1->0->3 [17] 1/-1/-1->0->3 [18] 1/-1/-1->0->3 [19] 1/-1/-1->0->3 [20] 1/-1/-1->0->3 [21] 1/-1/-1->0->3 [22] 1/-1/-1->0->3 [23] 1/-1/-1->0->3
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:32162:32667 [3] NCCL INFO [Proxy Service] Device 3 CPU core 106
compute-gpu-st-distributed-ml-1:32162:32668 [3] NCCL INFO [Proxy Service UDS] Device 3 CPU core 117
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:32165:32669 [6] NCCL INFO [Proxy Service] Device 6 CPU core 58
compute-gpu-st-distributed-ml-1:32165:32670 [6] NCCL INFO [Proxy Service UDS] Device 6 CPU core 166
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Check P2P Type isAllDirectP2p 1 directMode 0
compute-gpu-st-distributed-ml-1:32159:32671 [0] NCCL INFO [Proxy Service] Device 0 CPU core 143
compute-gpu-st-distributed-ml-1:32159:32672 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 32
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:32166:32673 [7] NCCL INFO [Proxy Service] Device 7 CPU core 60
compute-gpu-st-distributed-ml-1:32166:32674 [7] NCCL INFO [Proxy Service UDS] Device 7 CPU core 166
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:32160:32675 [1] NCCL INFO [Proxy Service] Device 1 CPU core 32
compute-gpu-st-distributed-ml-1:32160:32676 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 41
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:32164:32677 [5] NCCL INFO [Proxy Service] Device 5 CPU core 185
compute-gpu-st-distributed-ml-1:32164:32678 [5] NCCL INFO [Proxy Service UDS] Device 5 CPU core 177
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:32163:32679 [4] NCCL INFO [Proxy Service] Device 4 CPU core 79
compute-gpu-st-distributed-ml-1:32163:32680 [4] NCCL INFO [Proxy Service UDS] Device 4 CPU core 185
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:32161:32681 [2] NCCL INFO [Proxy Service] Device 2 CPU core 108
compute-gpu-st-distributed-ml-1:32161:32682 [2] NCCL INFO [Proxy Service UDS] Device 2 CPU core 117
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO 24 coll channels, 24 collnet channels, 16 nvls channels, 32 p2p channels, 32 p2p channels per peer
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO CC Off, workFifoBytes 1048576
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO ncclCommInitRank comm 0x5df33bf07b40 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 53000 commId 0x6c13ed52155019e2 - Init COMPLETE
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO ncclCommInitRank comm 0x60ff9b8389e0 rank 4 nranks 8 cudaDev 4 nvmlDev 4 busId 97000 commId 0x6c13ed52155019e2 - Init COMPLETE
compute-gpu-st-distributed-ml-1:32163:32654 [4] NCCL INFO Init timings - ncclCommInitRank: rank 4 nranks 8 total 2.56 (kernels 0.29, alloc 1.90, bootstrap 0.00, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.24, rest 0.04)
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO ncclCommInitRank comm 0x5b30f9f29650 rank 5 nranks 8 cudaDev 5 nvmlDev 5 busId a8000 commId 0x6c13ed52155019e2 - Init COMPLETE
compute-gpu-st-distributed-ml-1:32164:32649 [5] NCCL INFO Init timings - ncclCommInitRank: rank 5 nranks 8 total 2.56 (kernels 0.30, alloc 1.89, bootstrap 0.00, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.24, rest 0.04)
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO ncclCommInitRank comm 0x6519761ad730 rank 6 nranks 8 cudaDev 6 nvmlDev 6 busId b9000 commId 0x6c13ed52155019e2 - Init COMPLETE
compute-gpu-st-distributed-ml-1:32165:32650 [6] NCCL INFO Init timings - ncclCommInitRank: rank 6 nranks 8 total 2.56 (kernels 0.30, alloc 1.89, bootstrap 0.02, allgathers 0.01, topo 0.06, graphs 0.02, connections 0.25, rest 0.03)
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO ncclCommInitRank comm 0x62a62e903510 rank 7 nranks 8 cudaDev 7 nvmlDev 7 busId ca000 commId 0x6c13ed52155019e2 - Init COMPLETE
compute-gpu-st-distributed-ml-1:32166:32653 [7] NCCL INFO Init timings - ncclCommInitRank: rank 7 nranks 8 total 2.56 (kernels 0.39, alloc 1.80, bootstrap 0.01, allgathers 0.01, topo 0.06, graphs 0.02, connections 0.25, rest 0.03)
compute-gpu-st-distributed-ml-1:32159:32648 [0] NCCL INFO Init timings - ncclCommInitRank: rank 0 nranks 8 total 2.57 (kernels 0.30, alloc 1.10, bootstrap 0.81, allgathers 0.01, topo 0.06, graphs 0.02, connections 0.25, rest 0.03)
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO ncclCommInitRank comm 0x64e618ee9620 rank 2 nranks 8 cudaDev 2 nvmlDev 2 busId 75000 commId 0x6c13ed52155019e2 - Init COMPLETE
compute-gpu-st-distributed-ml-1:32161:32652 [2] NCCL INFO Init timings - ncclCommInitRank: rank 2 nranks 8 total 2.56 (kernels 0.29, alloc 1.72, bootstrap 0.19, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.24, rest 0.04)
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO ncclCommInitRank comm 0x64c37e929310 rank 3 nranks 8 cudaDev 3 nvmlDev 3 busId 86000 commId 0x6c13ed52155019e2 - Init COMPLETE
compute-gpu-st-distributed-ml-1:32162:32651 [3] NCCL INFO Init timings - ncclCommInitRank: rank 3 nranks 8 total 2.56 (kernels 0.29, alloc 1.90, bootstrap 0.00, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.25, rest 0.03)
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO NET/OFI Tuner init: comm with 8 ranks and 1 nodes.
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO ncclCommInitRank comm 0x5f4ac174e750 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId 64000 commId 0x6c13ed52155019e2 - Init COMPLETE
compute-gpu-st-distributed-ml-1:32160:32655 [1] NCCL INFO Init timings - ncclCommInitRank: rank 1 nranks 8 total 2.56 (kernels 0.29, alloc 1.79, bootstrap 0.11, allgathers 0.01, topo 0.06, graphs 0.02, connections 0.24, rest 0.03)
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 00/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 00/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 00/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 01/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 02/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 01/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 01/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 03/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 04/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 02/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 02/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 02/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 05/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 03/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 06/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 04/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 03/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 03/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 04/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 04/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 07/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 05/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 05/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 08/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 06/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 06/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 09/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 05/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 06/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 10/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 11/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 07/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 07/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 07/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 08/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 12/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 08/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 08/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 09/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 13/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 09/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 10/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 11/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 09/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 10/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 11/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 12/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 10/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 15/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 12/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 11/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 12/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 13/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 13/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 14/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 14/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 13/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 16/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 17/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 15/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 14/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 18/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 16/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 15/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 16/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 16/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 17/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 17/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 18/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 19/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 17/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 20/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 19/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 18/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 20/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 19/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 21/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 20/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 21/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 22/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 22/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 21/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Channel 23/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 22/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Channel 23/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Channel 23/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 00/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 01/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 02/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 00/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 00/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 00/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 03/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 01/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 01/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 02/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 01/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 02/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 03/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 04/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 03/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 02/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 03/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 04/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 04/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 05/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 05/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 04/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 05/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 06/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 06/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 06/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 05/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 06/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 07/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 07/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 07/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 07/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 08/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 09/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 08/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 08/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 08/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 09/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 10/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 09/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 09/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 11/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 10/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 10/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 10/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 11/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 11/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 11/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 12/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 12/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 12/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 13/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 12/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 13/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 14/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 13/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 13/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 14/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 14/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 14/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 15/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 15/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 16/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 15/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 16/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 17/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 18/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 16/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 17/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 15/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 16/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 19/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 18/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 20/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 17/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 17/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 19/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 18/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 20/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 18/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 19/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 21/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 21/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 19/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 20/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 22/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 20/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 22/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 21/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Channel 23/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 22/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Channel 23/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Channel 23/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 21/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 22/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Channel 23/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:32163:32683 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:32164:32686 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:32165:32687 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:32159:32685 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:32160:32689 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:32161:32690 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:32162:32684 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:32166:32688 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:32163:32692 [4] NCCL INFO NVLS comm 0x60ff9b8389e0 headRank 6 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:32164:32697 [5] NCCL INFO NVLS comm 0x5b30f9f29650 headRank 7 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:32159:32699 [0] NCCL INFO NVLS comm 0x5df33bf07b40 headRank 2 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:32162:32694 [3] NCCL INFO NVLS comm 0x64c37e929310 headRank 1 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:32161:32698 [2] NCCL INFO NVLS comm 0x64e618ee9620 headRank 0 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:32166:32696 [7] NCCL INFO NVLS comm 0x62a62e903510 headRank 5 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:32160:32695 [1] NCCL INFO NVLS comm 0x5f4ac174e750 headRank 3 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:32165:32693 [6] NCCL INFO NVLS comm 0x6519761ad730 headRank 4 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
           8             2     float     sum      -1    13.13    0.00    0.00      0    12.92    0.00    0.00      0
          16             4     float     sum      -1    12.93    0.00    0.00      0    13.05    0.00    0.00      0
          32             8     float     sum      -1    13.62    0.00    0.00      0    13.55    0.00    0.00      0
          64            16     float     sum      -1    14.88    0.00    0.01      0    14.73    0.00    0.01      0
         128            32     float     sum      -1    15.86    0.01    0.01      0    15.65    0.01    0.01      0
         256            64     float     sum      -1    16.01    0.02    0.03      0    15.87    0.02    0.03      0
         512           128     float     sum      -1    16.58    0.03    0.05      0    15.88    0.03    0.06      0
        1024           256     float     sum      -1    16.81    0.06    0.11      0    16.07    0.06    0.11      0
        2048           512     float     sum      -1    16.84    0.12    0.21      0    16.33    0.13    0.22      0
        4096          1024     float     sum      -1    16.91    0.24    0.42      0    16.35    0.25    0.44      0
        8192          2048     float     sum      -1    20.08    0.41    0.71      0    16.58    0.49    0.86      0
       16384          4096     float     sum      -1    17.79    0.92    1.61      0    17.32    0.95    1.66      0
       32768          8192     float     sum      -1    19.23    1.70    2.98      0    18.71    1.75    3.06      0
       65536         16384     float     sum      -1    19.55    3.35    5.87      0    18.95    3.46    6.05      0
      131072         32768     float     sum      -1    19.93    6.58   11.51      0    19.01    6.90   12.07      0
      262144         65536     float     sum      -1    20.37   12.87   22.52      0    20.18   12.99   22.74      0
      524288        131072     float     sum      -1    21.49   24.40   42.70      0    21.29   24.63   43.10      0
     1048576        262144     float     sum      -1    28.68   36.56   63.98      0    28.58   36.69   64.20      0
     2097152        524288     float     sum      -1    41.38   50.67   88.68      0    41.27   50.81   88.92      0
     4194304       1048576     float     sum      -1    53.28   78.73  137.77      0    53.16   78.90  138.07      0
     8388608       2097152     float     sum      -1    81.91  102.41  179.23      0    81.22  103.28  180.73      0
    16777216       4194304     float     sum      -1    122.2  137.32  240.31      0    121.1  138.51  242.40      0
    33554432       8388608     float     sum      -1    196.3  170.91  299.09      0    196.2  171.01  299.27      0
    67108864      16777216     float     sum      -1    321.4  208.80  365.40      0    321.3  208.86  365.50      0
   134217728      33554432     float     sum      -1    569.3  235.77  412.60      0    568.9  235.91  412.84      0
   268435456      67108864     float     sum      -1   1069.5  251.00  439.25      0   1070.2  250.82  438.93      0
   536870912     134217728     float     sum      -1   2082.9  257.76  451.07      0   2082.6  257.79  451.13      0
  1073741824     268435456     float     sum      -1   4082.4  263.02  460.28      0   4080.8  263.12  460.46      0
  2147483648     536870912     float     sum      -1   8060.9  266.41  466.21      0   8063.2  266.33  466.08      0
  4294967296    1073741824     float     sum      -1    15788  272.04  476.06      0    15788  272.05  476.08      0
  8589934592    2147483648     float     sum      -1    31299  274.45  480.29      0    31302  274.42  480.23      0
 17179869184    4294967296     float     sum      -1    62433  275.17  481.55      0    62355  275.52  482.15      0
compute-gpu-st-distributed-ml-1:32161:32754 [2] NCCL INFO comm 0x64e618ee9620 rank 2 nranks 8 cudaDev 2 busId 75000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:32162:32755 [3] NCCL INFO comm 0x64c37e929310 rank 3 nranks 8 cudaDev 3 busId 86000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:32165:32757 [6] NCCL INFO comm 0x6519761ad730 rank 6 nranks 8 cudaDev 6 busId b9000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:32160:32751 [1] NCCL INFO comm 0x5f4ac174e750 rank 1 nranks 8 cudaDev 1 busId 64000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:32164:32752 [5] NCCL INFO comm 0x5b30f9f29650 rank 5 nranks 8 cudaDev 5 busId a8000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:32166:32756 [7] NCCL INFO comm 0x62a62e903510 rank 7 nranks 8 cudaDev 7 busId ca000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:32163:32758 [4] NCCL INFO comm 0x60ff9b8389e0 rank 4 nranks 8 cudaDev 4 busId 97000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:32159:32753 [0] NCCL INFO comm 0x5df33bf07b40 rank 0 nranks 8 cudaDev 0 busId 53000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 160.437 
#
# Collective test concluded: all_reduce_perf
```

---
## p5e.48xlarge NCCL Tests 결과 (Multi Node)

### 환경
- ap-southeast-2(Sydney) 리전
- p5e.48xlarge x 2대 
- Lustre Persist_V1
- All Reduce 연산

### 결과

```bash
$ tail -f nccl-all_reduce_perf_1.out 
compute-gpu-st-distributed-ml-1: i-0a59d0ef2fec95909
compute-gpu-st-distributed-ml-2: i-03402a5a7bf3c2627
--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-2
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

--------------------------------------------------------------------------
A requested component was not found, or was unable to be opened.  This
means that this component is either not installed or is unable to be
used on your system (e.g., sometimes this means that shared libraries
that the component requires are unable to be found/loaded).  Note that
PMIX stopped checking at the first component that it did not find.

Host:      compute-gpu-st-distributed-ml-1
Framework: gds
Component: shmem2
--------------------------------------------------------------------------

# Collective test starting: all_reduce_perf
# nThread 1 nGpus 1 minBytes 8 maxBytes 17179869184 step: 2(factor) warmup iters: 1 iters: 100 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid  26241 on compute-gpu-st-distributed-ml-1 device  0 [0000:53:00] NVIDIA H200
#  Rank  1 Group  0 Pid  26242 on compute-gpu-st-distributed-ml-1 device  1 [0000:64:00] NVIDIA H200
#  Rank  2 Group  0 Pid  26243 on compute-gpu-st-distributed-ml-1 device  2 [0000:75:00] NVIDIA H200
#  Rank  3 Group  0 Pid  26244 on compute-gpu-st-distributed-ml-1 device  3 [0000:86:00] NVIDIA H200
#  Rank  4 Group  0 Pid  26245 on compute-gpu-st-distributed-ml-1 device  4 [0000:97:00] NVIDIA H200
#  Rank  5 Group  0 Pid  26246 on compute-gpu-st-distributed-ml-1 device  5 [0000:a8:00] NVIDIA H200
#  Rank  6 Group  0 Pid  26247 on compute-gpu-st-distributed-ml-1 device  6 [0000:b9:00] NVIDIA H200
#  Rank  7 Group  0 Pid  26248 on compute-gpu-st-distributed-ml-1 device  7 [0000:ca:00] NVIDIA H200
#  Rank  8 Group  0 Pid  28284 on compute-gpu-st-distributed-ml-2 device  0 [0000:53:00] NVIDIA H200
#  Rank  9 Group  0 Pid  28285 on compute-gpu-st-distributed-ml-2 device  1 [0000:64:00] NVIDIA H200
#  Rank 10 Group  0 Pid  28286 on compute-gpu-st-distributed-ml-2 device  2 [0000:75:00] NVIDIA H200
#  Rank 11 Group  0 Pid  28287 on compute-gpu-st-distributed-ml-2 device  3 [0000:86:00] NVIDIA H200
#  Rank 12 Group  0 Pid  28288 on compute-gpu-st-distributed-ml-2 device  4 [0000:97:00] NVIDIA H200
#  Rank 13 Group  0 Pid  28289 on compute-gpu-st-distributed-ml-2 device  5 [0000:a8:00] NVIDIA H200
#  Rank 14 Group  0 Pid  28290 on compute-gpu-st-distributed-ml-2 device  6 [0000:b9:00] NVIDIA H200
#  Rank 15 Group  0 Pid  28291 on compute-gpu-st-distributed-ml-2 device  7 [0000:ca:00] NVIDIA H200
compute-gpu-st-distributed-ml-1:26241:26241 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26241:26241 [0] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:26241:26241 [0] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:28284:28284 [0] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:28287:28287 [3] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:28285:28285 [1] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:26247:26247 [6] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:28289:28289 [5] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:26242:26242 [1] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:28290:28290 [6] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:26244:26244 [3] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:28286:28286 [2] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:28288:28288 [4] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:26243:26243 [2] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:26246:26246 [5] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:26245:26245 [4] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:28291:28291 [7] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-1:26248:26248 [7] NCCL INFO cudaDriverVersion 12080
compute-gpu-st-distributed-ml-2:28286:28286 [2] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26241:26241 [0] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-2:28285:28285 [1] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26243:26243 [2] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26245:26245 [4] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26246:26246 [5] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26247:26247 [6] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26242:26242 [1] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26244:26244 [3] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26248:26248 [7] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-2:28288:28288 [4] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-2:28289:28289 [5] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-2:28290:28290 [6] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-2:28287:28287 [3] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-2:28291:28291 [7] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-2:28284:28284 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to ^docker,lo,veth
compute-gpu-st-distributed-ml-1:26242:26242 [1] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:26242:26242 [1] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:26243:26243 [2] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:26243:26243 [2] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:26244:26244 [3] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:26244:26244 [3] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:26245:26245 [4] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:26245:26245 [4] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:26246:26246 [5] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:26246:26246 [5] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:26247:26247 [6] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:26247:26247 [6] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:26248:26248 [7] NCCL INFO Bootstrap: Using enp105s0:10.1.104.32<0>
compute-gpu-st-distributed-ml-1:26248:26248 [7] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-2:28286:28286 [2] NCCL INFO Bootstrap: Using enp105s0:10.1.77.247<0>
compute-gpu-st-distributed-ml-2:28286:28286 [2] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-2:28285:28285 [1] NCCL INFO Bootstrap: Using enp105s0:10.1.77.247<0>
compute-gpu-st-distributed-ml-2:28285:28285 [1] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-2:28287:28287 [3] NCCL INFO Bootstrap: Using enp105s0:10.1.77.247<0>
compute-gpu-st-distributed-ml-2:28287:28287 [3] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-2:28288:28288 [4] NCCL INFO Bootstrap: Using enp105s0:10.1.77.247<0>
compute-gpu-st-distributed-ml-2:28288:28288 [4] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-2:28289:28289 [5] NCCL INFO Bootstrap: Using enp105s0:10.1.77.247<0>
compute-gpu-st-distributed-ml-2:28289:28289 [5] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-2:28290:28290 [6] NCCL INFO Bootstrap: Using enp105s0:10.1.77.247<0>
compute-gpu-st-distributed-ml-2:28290:28290 [6] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-2:28291:28291 [7] NCCL INFO Bootstrap: Using enp105s0:10.1.77.247<0>
compute-gpu-st-distributed-ml-2:28291:28291 [7] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-2:28284:28284 [0] NCCL INFO Bootstrap: Using enp105s0:10.1.77.247<0>
compute-gpu-st-distributed-ml-2:28284:28284 [0] NCCL INFO NCCL version 2.27.7+cuda12.8
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/Plugin: Plugin name set by env to libnccl-net.so
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v10)
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO Successfully loaded external plugin libnccl-net.so
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Initializing aws-ofi-nccl 1.16.3
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Using Libfabric version 2.1
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Using CUDA driver version 12080 with runtime 12080
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Configuring AWS-specific options
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Internode latency set at 75.0 us
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Using transport protocol RDMA (platform set)
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Selected provider is efa, fabric is efa-direct (found 32 nics)
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID of rdmap116s0: f184380400004601
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a014df700000000
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID of rdmap133s0: c57dc21900006100
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a014df700000001
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID of rdmap82s0: e726302500000901
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a014df700000002
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID of rdmap99s0: a9300d8100001c00
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a014df700000003
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID of rdmap184s0: c9e1fc5f0000be01
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a014df700000004
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID of rdmap201s0: 1b4b35e20000d601
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a014df700000005
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID of rdmap150s0: e99ee3bc00008300
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a014df700000006
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID of rdmap167s0: bf1931f600009b00
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a014df700000007
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID of rdmap116s0: f184380400004601
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a014df700000000
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID of rdmap133s0: c57dc21900006100
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a014df700000001
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID of rdmap82s0: e726302500000901
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a014df700000002
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID of rdmap99s0: a9300d8100001c00
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a014df700000003
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID of rdmap184s0: c9e1fc5f0000be01
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a014df700000004
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID of rdmap201s0: 1b4b35e20000d601
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a014df700000005
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID of rdmap150s0: e99ee3bc00008300
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a014df700000006
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID of rdmap167s0: bf1931f600009b00
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a014df700000007
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID of rdmap116s0: f184380400004601
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID of rdmap116s0: f184380400004601
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID of rdmap116s0: 5918dda700004600
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a014df700000000
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a014df700000000
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID of rdmap133s0: c57dc21900006100
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID of rdmap133s0: c57dc21900006100
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID of rdmap116s0: f184380400004601
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a01682000000000
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID of rdmap133s0: 95b1197200006101
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a014df700000001
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID of rdmap82s0: e726302500000901
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a014df700000001
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID of rdmap82s0: e726302500000901
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a014df700000000
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID of rdmap133s0: c57dc21900006100
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a014df700000002
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID of rdmap99s0: a9300d8100001c00
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a014df700000002
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID of rdmap99s0: a9300d8100001c00
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a01682000000001
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID of rdmap82s0: 01dfac0500000901
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 0 device #0 0000:74:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 0 device #1 0000:73:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 0 device #2 0000:72:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 0 device #3 0000:71:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 1 device #0 0000:85:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 1 device #1 0000:84:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 1 device #2 0000:83:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 1 device #3 0000:82:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 2 device #0 0000:52:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 2 device #1 0000:51:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 2 device #2 0000:50:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 2 device #3 0000:4f:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 3 device #0 0000:63:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 3 device #1 0000:62:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 3 device #2 0000:61:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 3 device #3 0000:60:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 4 device #0 0000:b8:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 4 device #1 0000:b7:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 4 device #2 0000:b6:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 4 device #3 0000:b5:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 5 device #0 0000:c9:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 5 device #1 0000:c8:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 5 device #2 0000:c7:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 5 device #3 0000:c6:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 6 device #0 0000:96:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 6 device #1 0000:95:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 6 device #2 0000:94:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 6 device #3 0000:93:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 7 device #0 0000:a7:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 7 device #1 0000:a6:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 7 device #2 0000:a5:00.0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI NIC group 7 device #3 0000:a4:00.0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a014df700000001
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID of rdmap82s0: e726302500000901
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a014df700000003
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID of rdmap184s0: c9e1fc5f0000be01
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a014df700000003
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID of rdmap184s0: c9e1fc5f0000be01
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a014df700000002
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID of rdmap99s0: a9300d8100001c00
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a014df700000004
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID of rdmap201s0: 1b4b35e20000d601
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a01682000000002
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a014df700000004
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID of rdmap99s0: 870dfce200002001
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID of rdmap201s0: 1b4b35e20000d601
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID of rdmap116s0: f184380400004601
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID of rdmap116s0: f184380400004601
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Creating one domain per thread
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a01682000000003
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID of rdmap184s0: af4236a70000be01
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID of rdmap116s0: f184380400004601
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a014df700000003
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID of rdmap184s0: c9e1fc5f0000be01
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a01682000000004
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID of rdmap201s0: 3587fbec0000d601
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a014df700000005
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a014df700000005
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a01682000000005
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID of rdmap150s0: e99ee3bc00008300
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a014df700000000
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID of rdmap133s0: c57dc21900006100
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID of rdmap150s0: e99ee3bc00008300
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID of rdmap150s0: cd28a12600008301
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a014df700000000
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a01682000000006
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID for dev[0]: 00000000000000000a014df700000000
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID of rdmap133s0: c57dc21900006100
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID of rdmap133s0: c57dc21900006100
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a014df700000004
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID of rdmap201s0: 1b4b35e20000d601
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID of rdmap167s0: f16216ac00009b00
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a01682000000007
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a014df700000006
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a014df700000001
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID of rdmap82s0: e726302500000901
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a014df700000006
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID of rdmap167s0: bf1931f600009b00
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID of rdmap167s0: bf1931f600009b00
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a014df700000001
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID for dev[1]: 00000000000000000a014df700000001
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID of rdmap82s0: e726302500000901
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID of rdmap82s0: e726302500000901
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a014df700000005
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID of rdmap150s0: e99ee3bc00008300
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a014df700000002
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID of rdmap99s0: a9300d8100001c00
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a014df700000007
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a014df700000007
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a014df700000002
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID for dev[2]: 00000000000000000a014df700000002
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID of rdmap99s0: a9300d8100001c00
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID of rdmap99s0: a9300d8100001c00
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a014df700000006
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a014df700000003
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID of rdmap184s0: c9e1fc5f0000be01
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID of rdmap167s0: bf1931f600009b00
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a014df700000003
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID of rdmap184s0: c9e1fc5f0000be01
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID for dev[3]: 00000000000000000a014df700000003
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID of rdmap184s0: c9e1fc5f0000be01
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a014df700000004
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID of rdmap201s0: 1b4b35e20000d601
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a014df700000007
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a014df700000004
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID for dev[4]: 00000000000000000a014df700000004
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID of rdmap201s0: 1b4b35e20000d601
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID of rdmap201s0: 1b4b35e20000d601
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a014df700000005
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a014df700000005
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID for dev[5]: 00000000000000000a014df700000005
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID of rdmap150s0: e99ee3bc00008300
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID of rdmap150s0: e99ee3bc00008300
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID of rdmap150s0: e99ee3bc00008300
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a014df700000006
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID of rdmap167s0: bf1931f600009b00
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a014df700000006
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID for dev[6]: 00000000000000000a014df700000006
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a014df700000007
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID of rdmap167s0: bf1931f600009b00
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID of rdmap167s0: bf1931f600009b00
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a014df700000007
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI GUID for dev[7]: 00000000000000000a014df700000007
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/147 to environment
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Support for global registrations: false
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Support for DMA-BUF registrations: false
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/145 to environment
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Skipping adding NCCL_BUFFSIZE=8388608 to environment, already set
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Skipping adding NCCL_P2P_NET_CHUNKSIZE=524288 to environment, already set
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Skipping adding FI_EFA_FORK_SAFE=1 to environment, already set
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Adding NCCL_NET_FORCE_FLUSH=0 to environment
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Adding NCCL_NVLSTREE_MAX_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Adding NCCL_NVLS_CHUNKSIZE=524288 to environment
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Adding NCCL_TOPO_FILE=/proc/self/fd/163 to environment
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO Initialized NET plugin Libfabric
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO Assigned NET plugin Libfabric to comm
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO Using network Libfabric
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO DMA-BUF is available on GPU device 1
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO ncclCommInitRank comm 0x5807d129f610 rank 9 nranks 16 cudaDev 1 nvmlDev 1 busId 64000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO DMA-BUF is available on GPU device 3
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO ncclCommInitRank comm 0x5565ccde75d0 rank 11 nranks 16 cudaDev 3 nvmlDev 3 busId 86000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO DMA-BUF is available on GPU device 0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO ncclCommInitRank comm 0x55861914a600 rank 0 nranks 16 cudaDev 0 nvmlDev 0 busId 53000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO DMA-BUF is available on GPU device 6
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO ncclCommInitRank comm 0x603b5c4a92c0 rank 6 nranks 16 cudaDev 6 nvmlDev 6 busId b9000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO DMA-BUF is available on GPU device 6
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO DMA-BUF is available on GPU device 0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO ncclCommInitRank comm 0x618dae3dc250 rank 14 nranks 16 cudaDev 6 nvmlDev 6 busId b9000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO DMA-BUF is available on GPU device 2
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO DMA-BUF is available on GPU device 5
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO ncclCommInitRank comm 0x6267f170ca50 rank 8 nranks 16 cudaDev 0 nvmlDev 0 busId 53000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO DMA-BUF is available on GPU device 3
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO ncclCommInitRank comm 0x57a93296c420 rank 10 nranks 16 cudaDev 2 nvmlDev 2 busId 75000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO DMA-BUF is available on GPU device 7
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO ncclCommInitRank comm 0x59f9118853a0 rank 13 nranks 16 cudaDev 5 nvmlDev 5 busId a8000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO DMA-BUF is available on GPU device 4
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO ncclCommInitRank comm 0x5bdbaabd65f0 rank 15 nranks 16 cudaDev 7 nvmlDev 7 busId ca000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO ncclCommInitRank comm 0x642d66c73b40 rank 12 nranks 16 cudaDev 4 nvmlDev 4 busId 97000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO ncclCommInitRank comm 0x64bac1531ad0 rank 3 nranks 16 cudaDev 3 nvmlDev 3 busId 86000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO DMA-BUF is available on GPU device 4
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO DMA-BUF is available on GPU device 5
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO ncclCommInitRank comm 0x635d95ab3230 rank 4 nranks 16 cudaDev 4 nvmlDev 4 busId 97000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO DMA-BUF is available on GPU device 2
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO DMA-BUF is available on GPU device 7
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO DMA-BUF is available on GPU device 1
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO ncclCommInitRank comm 0x5a26b77e7b50 rank 5 nranks 16 cudaDev 5 nvmlDev 5 busId a8000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO ncclCommInitRank comm 0x5569a3b3a2b0 rank 2 nranks 16 cudaDev 2 nvmlDev 2 busId 75000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO ncclCommInitRank comm 0x598025a5fac0 rank 7 nranks 16 cudaDev 7 nvmlDev 7 busId ca000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO ncclCommInitRank comm 0x574e68045430 rank 1 nranks 16 cudaDev 1 nvmlDev 1 busId 64000 commId 0x20337669e8838c9f - Init START
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO Bootstrap timings total 0.005835 (create 0.000055, send 0.000152, recv 0.003975, ring 0.001252, delay 0.000001)
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO Bootstrap timings total 0.001913 (create 0.000034, send 0.000118, recv 0.000190, ring 0.001242, delay 0.000000)
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO Bootstrap timings total 0.218272 (create 0.000073, send 0.000164, recv 0.216742, ring 0.000835, delay 0.000000)
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO Bootstrap timings total 0.001734 (create 0.000039, send 0.000104, recv 0.000432, ring 0.000660, delay 0.000000)
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO Bootstrap timings total 0.001467 (create 0.000034, send 0.000109, recv 0.000384, ring 0.000620, delay 0.000000)
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO Bootstrap timings total 0.001783 (create 0.000032, send 0.000107, recv 0.000161, ring 0.000614, delay 0.000000)
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO Bootstrap timings total 0.039450 (create 0.000067, send 0.000310, recv 0.000428, ring 0.000619, delay 0.000000)
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO Bootstrap timings total 0.024717 (create 0.000055, send 0.000172, recv 0.018970, ring 0.001090, delay 0.000001)
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO Bootstrap timings total 0.907328 (create 0.000049, send 0.000375, recv 0.870598, ring 0.035707, delay 0.000001)
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Bootstrap timings total 0.246226 (create 0.000045, send 0.000138, recv 0.244929, ring 0.000668, delay 0.000001)
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO Bootstrap timings total 0.034521 (create 0.000062, send 0.000221, recv 0.000482, ring 0.033317, delay 0.000000)
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO Bootstrap timings total 0.055004 (create 0.000064, send 0.000333, recv 0.020282, ring 0.033870, delay 0.000000)
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO Bootstrap timings total 0.034920 (create 0.000065, send 0.000237, recv 0.000441, ring 0.033687, delay 0.000001)
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO Bootstrap timings total 0.036944 (create 0.000047, send 0.000240, recv 0.000542, ring 0.035697, delay 0.000001)
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO Bootstrap timings total 0.533102 (create 0.000082, send 0.000330, recv 0.498741, ring 0.033491, delay 0.000000)
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO Bootstrap timings total 0.035672 (create 0.000044, send 0.000224, recv 0.000320, ring 0.033378, delay 0.000001)
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO MNNVL busId 0xb9000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO MNNVL busId 0xca000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO MNNVL busId 0x97000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO MNNVL busId 0x75000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO MNNVL busId 0x64000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO MNNVL busId 0x86000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO MNNVL busId 0x53000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO MNNVL busId 0xca000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO MNNVL busId 0x97000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO MNNVL busId 0xa8000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO MNNVL busId 0x75000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO MNNVL busId 0x53000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO MNNVL busId 0xb9000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO MNNVL busId 0x86000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO MNNVL busId 0x64000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO MNNVL busId 0xa8000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/147
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/163
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NCCL_TOPO_FILE set by environment to /proc/self/fd/145
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO Setting affinity for GPU 1 to 24-47,120-143
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NVLS multicast support is available on dev 1 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO Setting affinity for GPU 7 to 48-71,144-167
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO Setting affinity for GPU 6 to 48-71,144-167
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Setting affinity for GPU 0 to 24-47,120-143
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NVLS multicast support is available on dev 0 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO Setting affinity for GPU 3 to 0-23,96-119
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NVLS multicast support is available on dev 3 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NVLS multicast support is available on dev 7 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO Setting affinity for GPU 2 to 0-23,96-119
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NVLS multicast support is available on dev 2 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NVLS multicast support is available on dev 6 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO Setting affinity for GPU 7 to 48-71,144-167
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO Setting affinity for GPU 4 to 72-95,168-191
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NVLS multicast support is available on dev 4 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NVLS multicast support is available on dev 7 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO Setting affinity for GPU 0 to 24-47,120-143
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO Setting affinity for GPU 4 to 72-95,168-191
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO Setting affinity for GPU 5 to 72-95,168-191
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NVLS multicast support is available on dev 4 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NVLS multicast support is available on dev 0 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NVLS multicast support is available on dev 5 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO Setting affinity for GPU 6 to 48-71,144-167
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NVLS multicast support is available on dev 6 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO Setting affinity for GPU 5 to 72-95,168-191
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO Setting affinity for GPU 3 to 0-23,96-119
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NVLS multicast support is available on dev 5 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NVLS multicast support is available on dev 3 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO Setting affinity for GPU 2 to 0-23,96-119
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO Setting affinity for GPU 1 to 24-47,120-143
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NVLS multicast support is available on dev 2 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NVLS multicast support is available on dev 1 (NVLS_NCHANNELS 16)
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO comm 0x642d66c73b40 rank 12 nRanks 16 nNodes 2 localRanks 8 localRank 4 MNNVL 0
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO comm 0x635d95ab3230 rank 4 nRanks 16 nNodes 2 localRanks 8 localRank 4 MNNVL 0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO comm 0x5a26b77e7b50 rank 5 nRanks 16 nNodes 2 localRanks 8 localRank 5 MNNVL 0
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NVLS Head  0:  2 10
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NVLS Head  1:  3 11
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NVLS Head  2:  0  8
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NVLS Head  3:  1  9
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO comm 0x59f9118853a0 rank 13 nRanks 16 nNodes 2 localRanks 8 localRank 5 MNNVL 0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO Trees [0] -1/-1/-1->13->12 [1] 10/-1/-1->13->12 [2] 10/-1/-1->13->12 [3] 10/-1/-1->13->12 [4] 10/-1/-1->13->12 [5] 10/-1/-1->13->12 [6] 10/-1/-1->13->12 [7] 10/-1/-1->13->5 [8] -1/-1/-1->13->12 [9] 10/-1/-1->13->12 [10] 10/-1/-1->13->12 [11] 10/-1/-1->13->12 [12] 10/-1/-1->13->12 [13] 10/-1/-1->13->12 [14] 10/-1/-1->13->12 [15] 10/5/-1->13->-1
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO comm 0x603b5c4a92c0 rank 6 nRanks 16 nNodes 2 localRanks 8 localRank 6 MNNVL 0
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NVLS Head  0:  2 10
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NVLS Head  1:  3 11
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NVLS Head  2:  0  8
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NVLS Head  3:  1  9
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NVLS Head  4:  6 14
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NVLS Head  5:  7 15
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NVLS Head  6:  4 12
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO comm 0x618dae3dc250 rank 14 nRanks 16 nNodes 2 localRanks 8 localRank 6 MNNVL 0
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO Trees [0] 15/-1/-1->14->9 [1] 15/-1/-1->14->9 [2] 15/-1/-1->14->9 [3] 15/-1/-1->14->9 [4] 15/-1/-1->14->6 [5] -1/-1/-1->14->9 [6] 15/-1/-1->14->9 [7] 15/-1/-1->14->9 [8] 15/-1/-1->14->9 [9] 15/-1/-1->14->9 [10] 15/-1/-1->14->9 [11] 15/-1/-1->14->9 [12] 15/6/-1->14->-1 [13] -1/-1/-1->14->9 [14] 15/-1/-1->14->9 [15] 15/-1/-1->14->9
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO comm 0x598025a5fac0 rank 7 nRanks 16 nNodes 2 localRanks 8 localRank 7 MNNVL 0
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NVLS Head  0:  2 10
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NVLS Head  1:  3 11
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NVLS Head  2:  0  8
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NVLS Head  3:  1  9
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NVLS Head  4:  6 14
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NVLS Head  5:  7 15
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NVLS Head  6:  4 12
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NVLS Head  7:  5 13
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO comm 0x5bdbaabd65f0 rank 15 nRanks 16 nNodes 2 localRanks 8 localRank 7 MNNVL 0
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO Trees [0] 12/-1/-1->15->14 [1] 12/-1/-1->15->14 [2] 12/-1/-1->15->14 [3] 12/-1/-1->15->14 [4] 12/-1/-1->15->14 [5] 12/-1/-1->15->7 [6] -1/-1/-1->15->14 [7] 12/-1/-1->15->14 [8] 12/-1/-1->15->14 [9] 12/-1/-1->15->14 [10] 12/-1/-1->15->14 [11] 12/-1/-1->15->14 [12] 12/-1/-1->15->14 [13] 12/7/-1->15->-1 [14] -1/-1/-1->15->14 [15] 12/-1/-1->15->14
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO Trees [0] 4/-1/-1->7->6 [1] 4/-1/-1->7->6 [2] 4/-1/-1->7->6 [3] 4/-1/-1->7->6 [4] 4/-1/-1->7->6 [5] 4/15/-1->7->-1 [6] -1/-1/-1->7->6 [7] 4/-1/-1->7->6 [8] 4/-1/-1->7->6 [9] 4/-1/-1->7->6 [10] 4/-1/-1->7->6 [11] 4/-1/-1->7->6 [12] 4/-1/-1->7->6 [13] 4/-1/-1->7->15 [14] -1/-1/-1->7->6 [15] 4/-1/-1->7->6
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO comm 0x6267f170ca50 rank 8 nRanks 16 nNodes 2 localRanks 8 localRank 0 MNNVL 0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO comm 0x55861914a600 rank 0 nRanks 16 nNodes 2 localRanks 8 localRank 0 MNNVL 0
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NVLS Head  0:  2 10
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NVLS Head  1:  3 11
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NVLS Head  2:  0  8
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NVLS Head  3:  1  9
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NVLS Head  4:  6 14
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NVLS Head  5:  7 15
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NVLS Head  6:  4 12
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NVLS Head  7:  5 13
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO comm 0x5807d129f610 rank 9 nRanks 16 nNodes 2 localRanks 8 localRank 1 MNNVL 0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO comm 0x574e68045430 rank 1 nRanks 16 nNodes 2 localRanks 8 localRank 1 MNNVL 0
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NVLS Head  0:  2 10
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NVLS Head  1:  3 11
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NVLS Head  2:  0  8
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NVLS Head  3:  1  9
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NVLS Head  4:  6 14
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NVLS Head  5:  7 15
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NVLS Head  6:  4 12
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NVLS Head  7:  5 13
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO comm 0x57a93296c420 rank 10 nRanks 16 nNodes 2 localRanks 8 localRank 2 MNNVL 0
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO Trees [0] 11/-1/-1->10->2 [1] -1/-1/-1->10->13 [2] 11/-1/-1->10->13 [3] 11/-1/-1->10->13 [4] 11/-1/-1->10->13 [5] 11/-1/-1->10->13 [6] 11/-1/-1->10->13 [7] 11/-1/-1->10->13 [8] 11/2/-1->10->-1 [9] -1/-1/-1->10->13 [10] 11/-1/-1->10->13 [11] 11/-1/-1->10->13 [12] 11/-1/-1->10->13 [13] 11/-1/-1->10->13 [14] 11/-1/-1->10->13 [15] 11/-1/-1->10->13
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO Trees [0] 6/-1/-1->1->0 [1] 6/-1/-1->1->0 [2] 6/-1/-1->1->0 [3] 6/9/-1->1->-1 [4] -1/-1/-1->1->0 [5] 6/-1/-1->1->0 [6] 6/-1/-1->1->0 [7] 6/-1/-1->1->0 [8] 6/-1/-1->1->0 [9] 6/-1/-1->1->0 [10] 6/-1/-1->1->0 [11] 6/-1/-1->1->9 [12] -1/-1/-1->1->0 [13] 6/-1/-1->1->0 [14] 6/-1/-1->1->0 [15] 6/-1/-1->1->0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO comm 0x5565ccde75d0 rank 11 nRanks 16 nNodes 2 localRanks 8 localRank 3 MNNVL 0
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO Trees [0] 8/-1/-1->11->10 [1] 8/-1/-1->11->3 [2] -1/-1/-1->11->10 [3] 8/-1/-1->11->10 [4] 8/-1/-1->11->10 [5] 8/-1/-1->11->10 [6] 8/-1/-1->11->10 [7] 8/-1/-1->11->10 [8] 8/-1/-1->11->10 [9] 8/3/-1->11->-1 [10] -1/-1/-1->11->10 [11] 8/-1/-1->11->10 [12] 8/-1/-1->11->10 [13] 8/-1/-1->11->10 [14] 8/-1/-1->11->10 [15] 8/-1/-1->11->10
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO comm 0x5569a3b3a2b0 rank 2 nRanks 16 nNodes 2 localRanks 8 localRank 2 MNNVL 0
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NVLS Head  0:  2 10
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NVLS Head  1:  3 11
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NVLS Head  2:  0  8
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NVLS Head  3:  1  9
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NVLS Head  4:  6 14
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NVLS Head  5:  7 15
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NVLS Head  6:  4 12
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NVLS Head  7:  5 13
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO Trees [0] 13/-1/-1->12->15 [1] 13/-1/-1->12->15 [2] 13/-1/-1->12->15 [3] 13/-1/-1->12->15 [4] 13/-1/-1->12->15 [5] 13/-1/-1->12->15 [6] 13/-1/-1->12->4 [7] -1/-1/-1->12->15 [8] 13/-1/-1->12->15 [9] 13/-1/-1->12->15 [10] 13/-1/-1->12->15 [11] 13/-1/-1->12->15 [12] 13/-1/-1->12->15 [13] 13/-1/-1->12->15 [14] 13/4/-1->12->-1 [15] -1/-1/-1->12->15
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO Trees [0] 3/10/-1->2->-1 [1] -1/-1/-1->2->5 [2] 3/-1/-1->2->5 [3] 3/-1/-1->2->5 [4] 3/-1/-1->2->5 [5] 3/-1/-1->2->5 [6] 3/-1/-1->2->5 [7] 3/-1/-1->2->5 [8] 3/-1/-1->2->10 [9] -1/-1/-1->2->5 [10] 3/-1/-1->2->5 [11] 3/-1/-1->2->5 [12] 3/-1/-1->2->5 [13] 3/-1/-1->2->5 [14] 3/-1/-1->2->5 [15] 3/-1/-1->2->5
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO comm 0x64bac1531ad0 rank 3 nRanks 16 nNodes 2 localRanks 8 localRank 3 MNNVL 0
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NVLS Head  0:  2 10
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NVLS Head  1:  3 11
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NVLS Head  2:  0  8
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NVLS Head  3:  1  9
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NVLS Head  4:  6 14
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NVLS Head  5:  7 15
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NVLS Head  6:  4 12
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NVLS Head  7:  5 13
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO Trees [0] 9/-1/-1->8->11 [1] 9/-1/-1->8->11 [2] 9/-1/-1->8->0 [3] -1/-1/-1->8->11 [4] 9/-1/-1->8->11 [5] 9/-1/-1->8->11 [6] 9/-1/-1->8->11 [7] 9/-1/-1->8->11 [8] 9/-1/-1->8->11 [9] 9/-1/-1->8->11 [10] 9/0/-1->8->-1 [11] -1/-1/-1->8->11 [12] 9/-1/-1->8->11 [13] 9/-1/-1->8->11 [14] 9/-1/-1->8->11 [15] 9/-1/-1->8->11
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO Trees [0] 0/-1/-1->3->2 [1] 0/11/-1->3->-1 [2] -1/-1/-1->3->2 [3] 0/-1/-1->3->2 [4] 0/-1/-1->3->2 [5] 0/-1/-1->3->2 [6] 0/-1/-1->3->2 [7] 0/-1/-1->3->2 [8] 0/-1/-1->3->2 [9] 0/-1/-1->3->11 [10] -1/-1/-1->3->2 [11] 0/-1/-1->3->2 [12] 0/-1/-1->3->2 [13] 0/-1/-1->3->2 [14] 0/-1/-1->3->2 [15] 0/-1/-1->3->2
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO Trees [0] 14/-1/-1->9->8 [1] 14/-1/-1->9->8 [2] 14/-1/-1->9->8 [3] 14/-1/-1->9->1 [4] -1/-1/-1->9->8 [5] 14/-1/-1->9->8 [6] 14/-1/-1->9->8 [7] 14/-1/-1->9->8 [8] 14/-1/-1->9->8 [9] 14/-1/-1->9->8 [10] 14/-1/-1->9->8 [11] 14/1/-1->9->-1 [12] -1/-1/-1->9->8 [13] 14/-1/-1->9->8 [14] 14/-1/-1->9->8 [15] 14/-1/-1->9->8
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NVLS Head  0:  2 10
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NVLS Head  1:  3 11
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NVLS Head  2:  0  8
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NVLS Head  3:  1  9
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NVLS Head  4:  6 14
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NVLS Head  5:  7 15
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NVLS Head  6:  4 12
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NVLS Head  7:  5 13
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO Trees [0] 5/-1/-1->4->7 [1] 5/-1/-1->4->7 [2] 5/-1/-1->4->7 [3] 5/-1/-1->4->7 [4] 5/-1/-1->4->7 [5] 5/-1/-1->4->7 [6] 5/12/-1->4->-1 [7] -1/-1/-1->4->7 [8] 5/-1/-1->4->7 [9] 5/-1/-1->4->7 [10] 5/-1/-1->4->7 [11] 5/-1/-1->4->7 [12] 5/-1/-1->4->7 [13] 5/-1/-1->4->7 [14] 5/-1/-1->4->12 [15] -1/-1/-1->4->7
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NVLS Head  4:  6 14
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NVLS Head  5:  7 15
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NVLS Head  6:  4 12
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NVLS Head  7:  5 13
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO Trees [0] -1/-1/-1->5->4 [1] 2/-1/-1->5->4 [2] 2/-1/-1->5->4 [3] 2/-1/-1->5->4 [4] 2/-1/-1->5->4 [5] 2/-1/-1->5->4 [6] 2/-1/-1->5->4 [7] 2/13/-1->5->-1 [8] -1/-1/-1->5->4 [9] 2/-1/-1->5->4 [10] 2/-1/-1->5->4 [11] 2/-1/-1->5->4 [12] 2/-1/-1->5->4 [13] 2/-1/-1->5->4 [14] 2/-1/-1->5->4 [15] 2/-1/-1->5->13
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NVLS Head  7:  5 13
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO Trees [0] 7/-1/-1->6->1 [1] 7/-1/-1->6->1 [2] 7/-1/-1->6->1 [3] 7/-1/-1->6->1 [4] 7/14/-1->6->-1 [5] -1/-1/-1->6->1 [6] 7/-1/-1->6->1 [7] 7/-1/-1->6->1 [8] 7/-1/-1->6->1 [9] 7/-1/-1->6->1 [10] 7/-1/-1->6->1 [11] 7/-1/-1->6->1 [12] 7/-1/-1->6->14 [13] -1/-1/-1->6->1 [14] 7/-1/-1->6->1 [15] 7/-1/-1->6->1
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 00/16 :  0  3 11  8  9 14 15 12 13 10  2  5  4  7  6  1
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 01/16 :  0  1  6  7  4  5  2 10 13 12 15 14  9  8 11  3
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 02/16 :  0  3  2  5  4  7  6  1  9 14 15 12 13 10 11  8
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 03/16 :  0  8 11 10 13 12 15 14  9  1  6  7  4  5  2  3
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 04/16 :  0  3  2  5  4  7 15 12 13 10 11  8  9 14  6  1
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 05/16 :  0  1  6 14  9  8 11 10 13 12 15  7  4  5  2  3
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 06/16 :  0  3  2  5 13 10 11  8  9 14 15 12  4  7  6  1
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 07/16 :  0  1  6  7  4 12 15 14  9  8 11 10 13  5  2  3
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 08/16 :  0  3 11  8  9 14 15 12 13 10  2  5  4  7  6  1
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 09/16 :  0  1  6  7  4  5  2 10 13 12 15 14  9  8 11  3
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 10/16 :  0  3  2  5  4  7  6  1  9 14 15 12 13 10 11  8
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 11/16 :  0  8 11 10 13 12 15 14  9  1  6  7  4  5  2  3
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 12/16 :  0  3  2  5  4  7 15 12 13 10 11  8  9 14  6  1
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 13/16 :  0  1  6 14  9  8 11 10 13 12 15  7  4  5  2  3
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 14/16 :  0  3  2  5 13 10 11  8  9 14 15 12  4  7  6  1
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Channel 15/16 :  0  1  6  7  4 12 15 14  9  8 11 10 13  5  2  3
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Trees [0] 1/-1/-1->0->3 [1] 1/-1/-1->0->3 [2] 1/8/-1->0->-1 [3] -1/-1/-1->0->3 [4] 1/-1/-1->0->3 [5] 1/-1/-1->0->3 [6] 1/-1/-1->0->3 [7] 1/-1/-1->0->3 [8] 1/-1/-1->0->3 [9] 1/-1/-1->0->3 [10] 1/-1/-1->0->8 [11] -1/-1/-1->0->3 [12] 1/-1/-1->0->3 [13] 1/-1/-1->0->3 [14] 1/-1/-1->0->3 [15] 1/-1/-1->0->3
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NCCL_BUFFSIZE set by environment to 8388608.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NCCL_P2P_NET_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO P2P Chunksize set to 524288
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Check P2P Type isAllDirectP2p 1 directMode 0
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26246:26753 [5] NCCL INFO [Proxy Service] Device 5 CPU core 87
compute-gpu-st-distributed-ml-2:28286:28793 [2] NCCL INFO [Proxy Service] Device 2 CPU core 106
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-2:28287:28799 [3] NCCL INFO [Proxy Service] Device 3 CPU core 111
compute-gpu-st-distributed-ml-1:26245:26756 [4] NCCL INFO [Proxy Service] Device 4 CPU core 74
compute-gpu-st-distributed-ml-2:28289:28794 [5] NCCL INFO [Proxy Service] Device 5 CPU core 188
compute-gpu-st-distributed-ml-1:26243:26757 [2] NCCL INFO [Proxy Service] Device 2 CPU core 108
compute-gpu-st-distributed-ml-1:26247:26752 [6] NCCL INFO [Proxy Service] Device 6 CPU core 59
compute-gpu-st-distributed-ml-1:26246:26759 [5] NCCL INFO [Proxy Service UDS] Device 5 CPU core 177
compute-gpu-st-distributed-ml-2:28291:28797 [7] NCCL INFO [Proxy Service] Device 7 CPU core 152
compute-gpu-st-distributed-ml-1:26245:26762 [4] NCCL INFO [Proxy Service UDS] Device 4 CPU core 75
compute-gpu-st-distributed-ml-2:28286:28800 [2] NCCL INFO [Proxy Service UDS] Device 2 CPU core 98
compute-gpu-st-distributed-ml-2:28290:28796 [6] NCCL INFO [Proxy Service] Device 6 CPU core 63
compute-gpu-st-distributed-ml-2:28287:28803 [3] NCCL INFO [Proxy Service UDS] Device 3 CPU core 118
compute-gpu-st-distributed-ml-2:28291:28802 [7] NCCL INFO [Proxy Service UDS] Device 7 CPU core 161
compute-gpu-st-distributed-ml-1:26241:26755 [0] NCCL INFO [Proxy Service] Device 0 CPU core 130
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
compute-gpu-st-distributed-ml-1:26243:26763 [2] NCCL INFO [Proxy Service UDS] Device 2 CPU core 113
compute-gpu-st-distributed-ml-2:28288:28795 [4] NCCL INFO [Proxy Service] Device 4 CPU core 188
compute-gpu-st-distributed-ml-1:26244:26758 [3] NCCL INFO [Proxy Service] Device 3 CPU core 11
compute-gpu-st-distributed-ml-1:26244:26764 [3] NCCL INFO [Proxy Service UDS] Device 3 CPU core 114
compute-gpu-st-distributed-ml-2:28290:28801 [6] NCCL INFO [Proxy Service UDS] Device 6 CPU core 160
compute-gpu-st-distributed-ml-1:26247:26760 [6] NCCL INFO [Proxy Service UDS] Device 6 CPU core 67
compute-gpu-st-distributed-ml-2:28289:28805 [5] NCCL INFO [Proxy Service UDS] Device 5 CPU core 86
compute-gpu-st-distributed-ml-1:26241:26761 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 140
compute-gpu-st-distributed-ml-1:26242:26765 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 131
compute-gpu-st-distributed-ml-1:26242:26754 [1] NCCL INFO [Proxy Service] Device 1 CPU core 34
compute-gpu-st-distributed-ml-1:26248:26766 [7] NCCL INFO [Proxy Service] Device 7 CPU core 58
compute-gpu-st-distributed-ml-1:26248:26767 [7] NCCL INFO [Proxy Service UDS] Device 7 CPU core 69
compute-gpu-st-distributed-ml-2:28284:28798 [0] NCCL INFO [Proxy Service] Device 0 CPU core 36
compute-gpu-st-distributed-ml-2:28284:28804 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 137
compute-gpu-st-distributed-ml-2:28288:28806 [4] NCCL INFO [Proxy Service UDS] Device 4 CPU core 86
compute-gpu-st-distributed-ml-2:28285:28807 [1] NCCL INFO [Proxy Service] Device 1 CPU core 35
compute-gpu-st-distributed-ml-2:28285:28808 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 143
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NCCL_NVLS_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO CC Off, workFifoBytes 1048576
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO ncclCommInitRank comm 0x5569a3b3a2b0 rank 2 nranks 16 cudaDev 2 nvmlDev 2 busId 75000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO ncclCommInitRank comm 0x55861914a600 rank 0 nranks 16 cudaDev 0 nvmlDev 0 busId 53000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-1:26241:26733 [0] NCCL INFO Init timings - ncclCommInitRank: rank 0 nranks 16 total 2.54 (kernels 0.30, alloc 1.70, bootstrap 0.25, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.21, rest 0.00)
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO ncclCommInitRank comm 0x574e68045430 rank 1 nranks 16 cudaDev 1 nvmlDev 1 busId 64000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-1:26242:26737 [1] NCCL INFO Init timings - ncclCommInitRank: rank 1 nranks 16 total 2.53 (kernels 0.30, alloc 1.94, bootstrap 0.00, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.21, rest 0.00)
compute-gpu-st-distributed-ml-1:26243:26738 [2] NCCL INFO Init timings - ncclCommInitRank: rank 2 nranks 16 total 2.53 (kernels 0.30, alloc 1.94, bootstrap 0.00, allgathers 0.01, topo 0.06, graphs 0.01, connections 0.21, rest 0.00)
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO ncclCommInitRank comm 0x635d95ab3230 rank 4 nranks 16 cudaDev 4 nvmlDev 4 busId 97000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-1:26245:26740 [4] NCCL INFO Init timings - ncclCommInitRank: rank 4 nranks 16 total 2.53 (kernels 0.30, alloc 1.93, bootstrap 0.01, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.21, rest 0.00)
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO ncclCommInitRank comm 0x603b5c4a92c0 rank 6 nranks 16 cudaDev 6 nvmlDev 6 busId b9000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-1:26247:26734 [6] NCCL INFO Init timings - ncclCommInitRank: rank 6 nranks 16 total 2.53 (kernels 0.29, alloc 1.73, bootstrap 0.22, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.21, rest 0.00)
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO ncclCommInitRank comm 0x598025a5fac0 rank 7 nranks 16 cudaDev 7 nvmlDev 7 busId ca000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-1:26248:26736 [7] NCCL INFO Init timings - ncclCommInitRank: rank 7 nranks 16 total 2.53 (kernels 0.40, alloc 1.83, bootstrap 0.00, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.21, rest 0.00)
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO ncclCommInitRank comm 0x64bac1531ad0 rank 3 nranks 16 cudaDev 3 nvmlDev 3 busId 86000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-1:26244:26739 [3] NCCL INFO Init timings - ncclCommInitRank: rank 3 nranks 16 total 2.53 (kernels 0.29, alloc 1.91, bootstrap 0.02, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.21, rest 0.00)
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO ncclCommInitRank comm 0x5a26b77e7b50 rank 5 nranks 16 cudaDev 5 nvmlDev 5 busId a8000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-1:26246:26735 [5] NCCL INFO Init timings - ncclCommInitRank: rank 5 nranks 16 total 2.53 (kernels 0.30, alloc 1.93, bootstrap 0.00, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.21, rest 0.00)
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 512 | 512
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO 16 coll channels, 16 collnet channels, 16 nvls channels, 16 p2p channels, 2 p2p channels per peer
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO ncclCommInitRank comm 0x57a93296c420 rank 10 nranks 16 cudaDev 2 nvmlDev 2 busId 75000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-2:28286:28775 [2] NCCL INFO Init timings - ncclCommInitRank: rank 10 nranks 16 total 2.57 (kernels 0.30, alloc 1.89, bootstrap 0.04, allgathers 0.02, topo 0.06, graphs 0.01, connections 0.25, rest 0.00)
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO ncclCommInitRank comm 0x5565ccde75d0 rank 11 nranks 16 cudaDev 3 nvmlDev 3 busId 86000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-2:28287:28777 [3] NCCL INFO Init timings - ncclCommInitRank: rank 11 nranks 16 total 2.57 (kernels 0.30, alloc 1.40, bootstrap 0.53, allgathers 0.01, topo 0.06, graphs 0.01, connections 0.25, rest 0.00)
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO ncclCommInitRank comm 0x618dae3dc250 rank 14 nranks 16 cudaDev 6 nvmlDev 6 busId b9000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-2:28290:28779 [6] NCCL INFO Init timings - ncclCommInitRank: rank 14 nranks 16 total 2.57 (kernels 0.30, alloc 1.87, bootstrap 0.06, allgathers 0.01, topo 0.06, graphs 0.02, connections 0.25, rest 0.00)
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO ncclCommInitRank comm 0x5807d129f610 rank 9 nranks 16 cudaDev 1 nvmlDev 1 busId 64000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-2:28285:28774 [1] NCCL INFO Init timings - ncclCommInitRank: rank 9 nranks 16 total 2.57 (kernels 0.29, alloc 1.03, bootstrap 0.91, allgathers 0.00, topo 0.06, graphs 0.02, connections 0.25, rest 0.00)
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO ncclCommInitRank comm 0x642d66c73b40 rank 12 nranks 16 cudaDev 4 nvmlDev 4 busId 97000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-2:28288:28781 [4] NCCL INFO Init timings - ncclCommInitRank: rank 12 nranks 16 total 2.57 (kernels 0.30, alloc 1.89, bootstrap 0.03, allgathers 0.01, topo 0.06, graphs 0.02, connections 0.25, rest 0.00)
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO ncclCommInitRank comm 0x5bdbaabd65f0 rank 15 nranks 16 cudaDev 7 nvmlDev 7 busId ca000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-2:28291:28778 [7] NCCL INFO Init timings - ncclCommInitRank: rank 15 nranks 16 total 2.57 (kernels 0.30, alloc 1.89, bootstrap 0.03, allgathers 0.01, topo 0.06, graphs 0.02, connections 0.25, rest 0.00)
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO ncclCommInitRank comm 0x6267f170ca50 rank 8 nranks 16 cudaDev 0 nvmlDev 0 busId 53000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-2:28284:28776 [0] NCCL INFO Init timings - ncclCommInitRank: rank 8 nranks 16 total 2.57 (kernels 0.30, alloc 1.89, bootstrap 0.04, allgathers 0.01, topo 0.06, graphs 0.02, connections 0.25, rest 0.00)
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO TUNER/Plugin: Plugin name set by env to /opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO TUNER/Plugin: Using tuner plugin nccl_ofi_tuner
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Region base Tuner is chosen for platform: p5e.48xlarge
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Region Tuner init (platform 0): comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO NET/OFI Tuner init: comm with 16 ranks and 2 nodes.
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO ncclCommInitRank comm 0x59f9118853a0 rank 13 nranks 16 cudaDev 5 nvmlDev 5 busId a8000 commId 0x20337669e8838c9f - Init COMPLETE
compute-gpu-st-distributed-ml-2:28289:28780 [5] NCCL INFO Init timings - ncclCommInitRank: rank 13 nranks 16 total 2.57 (kernels 0.30, alloc 1.89, bootstrap 0.04, allgathers 0.01, topo 0.06, graphs 0.02, connections 0.25, rest 0.00)
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 00/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 00/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 00/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 00/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 01/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 00/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 00/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 00/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 01/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 01/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 02/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 02/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 01/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 01/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 02/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 03/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 02/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 02/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 03/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 03/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 02/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 02/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 02/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 04/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 04/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 03/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 04/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 04/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 03/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 04/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 05/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 06/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 03/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 04/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 06/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 04/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 05/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 04/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 05/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 05/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 07/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 05/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 07/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 06/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 06/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 06/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 08/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 06/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 06/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 07/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 08/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 05/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 07/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 08/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 07/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 09/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 06/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 09/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 08/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 07/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 10/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 09/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 08/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 08/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 08/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 10/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 09/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 08/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 11/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 10/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 10/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 10/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 09/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 11/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 10/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 09/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 11/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 11/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 12/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 11/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 12/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 10/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 12/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 12/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 12/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 14/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 11/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 12/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 13/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 13/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 10/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 14/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 14/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 13/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 12/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 15/0 : 6[6] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 15/0 : 0[0] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 13/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 14/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 12/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 15/0 : 14[6] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 13/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 14/0 : 12[4] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 14/0 : 4[4] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 14/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 15/0 : 10[2] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 13/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 14/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 00/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 15/0 : 2[2] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 00/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 01/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 15/0 : 8[0] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 02/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 00/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 01/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 00/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 03/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 02/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 01/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 01/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 00/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 00/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 01/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 04/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 02/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 01/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 02/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 03/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 01/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 03/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 01/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 02/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 02/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 03/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 03/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 04/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 03/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 05/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 03/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 04/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 05/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 05/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 04/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 06/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 04/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 05/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 07/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 03/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 05/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 08/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 07/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 05/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 04/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 06/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 06/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 09/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 05/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 07/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 07/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 06/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 07/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 06/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 05/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 08/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 10/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 07/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 09/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 09/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 11/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 08/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 10/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 08/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 07/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 10/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 06/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 07/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 12/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 09/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 11/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 11/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 08/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 12/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 09/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 09/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 11/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 13/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 09/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 12/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 15/0 : 12[4] -> 15[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 13/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 10/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 13/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 12/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 08/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 09/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 11/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 10/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 14/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 13/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 11/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 12/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 14/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 14/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 13/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 15/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 10/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 15/0 : 8[0] -> 11[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 11/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 11/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 12/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 15/0 : 10[2] -> 13[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 13/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 13/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 14/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 13/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 14/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 14/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 15/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 15/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 15/0 : 1[1] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 15/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO NCCL_NET_FORCE_FLUSH set by environment to 0.
compute-gpu-st-distributed-ml-1:26243:26776 [2] NCCL INFO [Proxy Progress] Device 2 CPU core 114
compute-gpu-st-distributed-ml-1:26246:26777 [5] NCCL INFO [Proxy Progress] Device 5 CPU core 177
compute-gpu-st-distributed-ml-2:28291:28817 [7] NCCL INFO [Proxy Progress] Device 7 CPU core 153
compute-gpu-st-distributed-ml-2:28288:28818 [4] NCCL INFO [Proxy Progress] Device 4 CPU core 94
compute-gpu-st-distributed-ml-2:28284:28819 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 37
compute-gpu-st-distributed-ml-2:28289:28820 [5] NCCL INFO [Proxy Progress] Device 5 CPU core 95
compute-gpu-st-distributed-ml-2:28287:28821 [3] NCCL INFO [Proxy Progress] Device 3 CPU core 112
compute-gpu-st-distributed-ml-1:26241:26778 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 34
compute-gpu-st-distributed-ml-1:26248:26779 [7] NCCL INFO [Proxy Progress] Device 7 CPU core 59
compute-gpu-st-distributed-ml-2:28290:28822 [6] NCCL INFO [Proxy Progress] Device 6 CPU core 63
compute-gpu-st-distributed-ml-1:26245:26781 [4] NCCL INFO [Proxy Progress] Device 4 CPU core 177
compute-gpu-st-distributed-ml-1:26247:26780 [6] NCCL INFO [Proxy Progress] Device 6 CPU core 69
compute-gpu-st-distributed-ml-2:28286:28823 [2] NCCL INFO [Proxy Progress] Device 2 CPU core 114
compute-gpu-st-distributed-ml-1:26242:26782 [1] NCCL INFO [Proxy Progress] Device 1 CPU core 140
compute-gpu-st-distributed-ml-1:26244:26783 [3] NCCL INFO [Proxy Progress] Device 3 CPU core 13
compute-gpu-st-distributed-ml-2:28285:28824 [1] NCCL INFO [Proxy Progress] Device 1 CPU core 143
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 00/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 00/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 08/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 08/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 00/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 00/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Channel 08/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Channel 08/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 02/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 03/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 04/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 10/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 02/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 12/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 11/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Channel 10/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 03/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 04/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 11/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 06/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 02/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 12/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 14/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 01/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 10/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 06/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Channel 14/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 09/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 02/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 01/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Channel 10/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 05/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 09/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 13/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 01/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 05/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 13/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 04/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 07/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 09/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 05/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 12/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 03/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 01/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 15/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 04/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 09/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 11/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 07/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 12/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 03/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 13/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 15/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 05/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 00/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 00/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 07/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 11/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 00/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 13/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 00/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 15/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 00/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 07/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 00/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 15/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 01/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 01/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 06/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 01/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 01/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 14/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 06/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Channel 14/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 03/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 01/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 01/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 01/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 03/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 02/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 02/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 04/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 02/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 03/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 02/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 01/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 03/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 04/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 02/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 04/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 05/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 03/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 04/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 03/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 02/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 05/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 06/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 05/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 03/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 05/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 06/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 05/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 03/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 05/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 06/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 06/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 04/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 07/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 06/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 05/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 04/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 06/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 07/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 07/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 07/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 05/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 07/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 08/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 08/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 09/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 07/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 08/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 09/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 07/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 08/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 09/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 09/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 10/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 08/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 07/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 09/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 10/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 11/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 11/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 09/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 10/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 12/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 11/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 09/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 12/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 10/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 10/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 11/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 13/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 13/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 11/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 08/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 13/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 10/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 13/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 11/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 14/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 14/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 11/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 09/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 12/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 12/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 13/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 14/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 12/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 11/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 14/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 15/0 : 5[5] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 13/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 13/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 12/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 00/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Channel 15/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 14/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Channel 15/0 : 14[6] -> 9[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 15/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 15/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 13/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 15/0 : 3[3] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 15/0 : 7[7] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 01/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 00/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 14/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 02/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 00/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 00/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 00/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 01/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 01/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 01/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 02/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 03/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 02/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 15/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 00/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 03/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 02/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 04/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 02/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 01/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 00/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 05/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 04/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 03/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 02/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 03/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 04/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 04/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 02/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 05/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 06/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 06/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 05/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 03/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 04/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 00/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 03/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 04/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 01/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 06/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 06/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 04/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 05/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 06/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 05/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 06/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 07/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 07/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 07/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 08/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 08/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 06/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 07/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 09/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 02/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 08/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 08/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 08/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 09/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 07/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 08/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 10/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 09/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 10/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 10/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 11/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 10/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 11/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 04/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 09/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 10/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 05/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 09/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 12/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 12/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 08/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 10/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 10/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 12/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 11/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 13/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 13/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 11/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 06/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 07/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 11/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 11/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 14/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 12/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Channel 14/0 : 5[5] -> 4[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 13/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 12/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 14/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 08/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Channel 15/0 : 3[3] -> 2[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 13/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 14/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 12/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 09/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Channel 15/0 : 15[7] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 12/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Channel 15/0 : 9[1] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 10/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Channel 14/0 : 13[5] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 14/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 12/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 13/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 14/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Channel 15/0 : 7[7] -> 6[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Channel 15/0 : 11[3] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 13/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 14/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Channel 15/0 : 1[1] -> 0[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26769 [0] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-1:26242:26775 [1] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-2:28284:28812 [0] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-2:28285:28816 [1] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-2:28290:28809 [6] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-1:26243:26770 [2] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-1:26245:26774 [4] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-1:26246:26768 [5] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-2:28291:28814 [7] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-1:26247:26772 [6] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-2:28286:28810 [2] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-1:26248:26773 [7] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-1:26244:26771 [3] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-2:28287:28813 [3] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-2:28288:28811 [4] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-2:28289:28815 [5] NCCL INFO Connected all trees
compute-gpu-st-distributed-ml-1:26241:26785 [0] NCCL INFO Channel 02/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28285:28833 [1] NCCL INFO Channel 04/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26787 [2] NCCL INFO Channel 00/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26245:26786 [4] NCCL INFO Channel 06/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28286:28830 [2] NCCL INFO Channel 01/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26789 [6] NCCL INFO Channel 05/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28826 [7] NCCL INFO Channel 04/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28827 [3] NCCL INFO Channel 00/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28831 [4] NCCL INFO Channel 07/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28832 [5] NCCL INFO Channel 06/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28826 [7] NCCL INFO Channel 12/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26789 [6] NCCL INFO Channel 13/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28830 [2] NCCL INFO Channel 09/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28827 [3] NCCL INFO Channel 08/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28831 [4] NCCL INFO Channel 15/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28832 [5] NCCL INFO Channel 14/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28833 [1] NCCL INFO Channel 12/0 : 9[1] -> 14[6] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26242:26790 [1] NCCL INFO Channel 02/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26790 [1] NCCL INFO Channel 10/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28829 [0] NCCL INFO Channel 03/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28829 [0] NCCL INFO Channel 11/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26787 [2] NCCL INFO Channel 08/0 : 2[2] -> 5[5] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26241:26785 [0] NCCL INFO Channel 10/0 : 0[0] -> 3[3] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28290:28828 [6] NCCL INFO Channel 05/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28833 [1] NCCL INFO Channel 02/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28828 [6] NCCL INFO Channel 13/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28833 [1] NCCL INFO Channel 10/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26786 [4] NCCL INFO Channel 14/0 : 4[4] -> 7[7] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26789 [6] NCCL INFO Channel 04/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26247:26789 [6] NCCL INFO Channel 12/0 : 6[6] -> 1[1] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26243:26787 [2] NCCL INFO Channel 01/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26791 [5] NCCL INFO Channel 06/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26792 [7] NCCL INFO Channel 04/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26786 [4] NCCL INFO Channel 07/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26791 [5] NCCL INFO Channel 14/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26787 [2] NCCL INFO Channel 09/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26792 [7] NCCL INFO Channel 12/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26786 [4] NCCL INFO Channel 15/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26785 [0] NCCL INFO Channel 03/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26788 [3] NCCL INFO Channel 00/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26785 [0] NCCL INFO Channel 11/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28832 [5] NCCL INFO Channel 00/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28826 [7] NCCL INFO Channel 06/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-1:26244:26788 [3] NCCL INFO Channel 08/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28827 [3] NCCL INFO Channel 02/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28826 [7] NCCL INFO Channel 14/0 : 15[7] -> 12[4] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28289:28832 [5] NCCL INFO Channel 08/0 : 13[5] -> 10[2] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28287:28827 [3] NCCL INFO Channel 10/0 : 11[3] -> 8[0] via P2P/CUMEM
compute-gpu-st-distributed-ml-2:28291:28826 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-2:28290:28828 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:26241:26785 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-2:28289:28832 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:26242:26790 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:26243:26787 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:26244:26788 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:26245:26786 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-2:28286:28830 [2] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:26246:26791 [5] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-2:28287:28827 [3] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:26247:26789 [6] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-2:28288:28831 [4] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:26248:26792 [7] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-2:28284:28829 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-2:28285:28833 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO NVLS comm 0x5a26b77e7b50 headRank 7 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO NVLS comm 0x574e68045430 headRank 3 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO NVLS comm 0x603b5c4a92c0 headRank 4 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO NVLS comm 0x598025a5fac0 headRank 5 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO NVLS comm 0x5569a3b3a2b0 headRank 0 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO NVLS comm 0x6267f170ca50 headRank 2 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO NVLS comm 0x64bac1531ad0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO NVLS comm 0x635d95ab3230 headRank 6 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO NVLS comm 0x5565ccde75d0 headRank 1 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO NVLS comm 0x618dae3dc250 headRank 4 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO NVLS comm 0x57a93296c420 headRank 0 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO NVLS comm 0x642d66c73b40 headRank 6 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO NVLS comm 0x5bdbaabd65f0 headRank 5 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO NVLS comm 0x5807d129f610 headRank 3 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO NVLS comm 0x55861914a600 headRank 2 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO NVLS comm 0x59f9118853a0 headRank 7 nHeads 8 nvlsRanks 8 buffSize 4194304 nvlsPerRankSize 134217728 nvlsTotalSize 1073741824
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 00/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 00/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 00/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 01/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 00/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 00/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 00/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 00/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 01/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 01/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 02/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 01/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 01/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 02/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 01/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 01/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 03/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 02/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 03/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 03/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 02/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 02/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 02/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 02/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 04/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 03/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 04/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 04/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 03/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 05/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 04/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 03/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 03/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 05/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 05/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 05/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 04/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 05/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 06/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 04/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 06/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 04/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 06/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 06/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 05/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 07/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 05/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 07/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 06/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 06/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 07/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 07/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 07/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 08/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 07/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 06/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 08/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 07/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 08/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 09/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 09/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 08/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 08/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 09/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 08/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 08/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 10/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 10/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 11/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 09/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 09/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 10/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 11/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 09/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 09/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 11/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 10/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 10/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 12/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 11/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 10/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 12/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 10/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 12/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 11/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 11/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 13/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 13/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 12/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 13/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 11/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 13/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 12/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 14/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 12/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 14/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 13/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 14/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 14/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 12/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 13/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 15/0 : 14[6] -> 6[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 14/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 15/0 : 8[0] -> 0[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 15/0 : 11[3] -> 3[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 14/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 15/0 : 10[2] -> 2[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 13/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 00/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 00/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 15/0 : 12[4] -> 4[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 02/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 02/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 15/0 : 15[7] -> 7[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 01/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 01/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 00/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 15/0 : 9[1] -> 1[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 14/0 : 13[5] -> 5[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 03/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 03/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 00/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 02/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 01/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 04/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 00/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 04/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 00/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 04/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 01/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 03/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 05/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 02/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 01/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 05/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 01/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 05/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 06/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 02/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 06/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 03/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 04/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 06/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 06/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 02/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 07/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 03/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 07/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 04/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 05/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 07/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 03/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 08/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 07/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 06/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 08/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 05/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 06/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 10/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 10/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 04/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 09/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 07/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 09/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 07/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 08/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 11/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 05/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 11/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 10/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 12/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 08/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 08/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 12/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 09/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 08/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 12/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 11/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 13/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 09/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 13/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 10/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 09/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 09/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 13/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 14/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 14/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 11/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 12/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 14/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 10/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 10/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Channel 15/0 : 0[0] -> 8[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 14/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Channel 15/0 : 6[6] -> 14[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 12/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 13/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Channel 15/0 : 3[3] -> 11[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 11/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Channel 15/0 : 2[2] -> 10[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 11/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Channel 13/0 : 4[4] -> 12[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 14/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 12/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 14/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Channel 15/0 : 1[1] -> 9[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Channel 13/0 : 5[5] -> 13[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Channel 15/0 : 7[7] -> 15[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 00/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 02/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 00/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 00/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 00/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 02/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 00/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 00/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 01/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 03/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 01/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 03/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 01/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 01/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 01/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 01/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 02/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 04/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 04/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 04/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 02/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 04/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 02/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 02/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 05/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 03/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 05/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 05/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 05/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 03/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 03/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 03/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 06/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 06/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 06/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 04/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 06/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 06/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 06/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 04/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 07/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 07/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 07/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 05/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 05/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 07/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 07/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 07/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 08/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 10/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 08/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 08/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 08/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 08/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 10/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 08/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 09/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 11/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 09/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 09/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 09/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 09/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 11/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 09/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 10/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 10/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 12/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 12/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 10/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 12/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 12/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 10/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 11/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 11/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 13/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 13/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 11/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 13/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 11/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 13/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 14/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 12/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 14/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 14/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 12/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 14/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 14/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 14/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 15/0 : 7[7] -> 15[7] [receive] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 13/0 : 5[5] -> 13[5] [receive] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 15/0 : 0[0] -> 8[0] [receive] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 15/0 : 3[3] -> 11[3] [receive] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 13/0 : 4[4] -> 12[4] [receive] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 00/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 15/0 : 2[2] -> 10[2] [receive] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 15/0 : 1[1] -> 9[1] [receive] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 15/0 : 6[6] -> 14[6] [receive] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 00/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 00/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 00/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 00/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 01/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 00/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 01/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 00/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 01/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 01/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 01/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 02/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 02/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 01/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 02/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 02/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 01/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 02/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 03/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 03/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 03/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 02/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 02/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 03/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 03/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 03/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 04/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 04/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 04/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 04/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 04/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 03/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 04/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 04/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 06/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 05/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 05/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 05/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 05/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 05/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 05/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 05/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 07/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 06/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 06/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 06/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 06/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 07/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 06/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 06/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 08/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 07/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 07/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 07/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 08/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 07/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 07/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 08/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 09/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 08/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 08/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 08/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 09/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 09/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 08/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 09/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 09/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 10/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 09/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 10/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 10/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 10/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 09/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 10/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 11/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 11/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 10/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 11/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 11/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 11/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 11/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 10/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 12/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 12/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 12/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 12/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 12/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 12/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 12/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 11/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 13/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 14/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 13/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 13/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 13/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 13/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 13/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 13/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 14/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Channel 15/0 : 15[7] -> 7[7] [send] via NET/Libfabric/5/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 14/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 14/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Channel 15/0 : 12[4] -> 4[4] [send] via NET/Libfabric/6/GDRDMA
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Channel 14/0 : 13[5] -> 5[5] [send] via NET/Libfabric/7/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 14/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 14/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Channel 15/0 : 8[0] -> 0[0] [send] via NET/Libfabric/2/GDRDMA
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Channel 15/0 : 9[1] -> 1[1] [send] via NET/Libfabric/3/GDRDMA
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Channel 15/0 : 11[3] -> 3[3] [send] via NET/Libfabric/1/GDRDMA
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Channel 15/0 : 10[2] -> 2[2] [send] via NET/Libfabric/0/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Channel 15/0 : 14[6] -> 6[6] [send] via NET/Libfabric/4/GDRDMA
compute-gpu-st-distributed-ml-2:28290:28836 [6] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-2:28284:28835 [0] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-1:26241:26798 [0] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-2:28290:28290 [6] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26247:26796 [6] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-2:28284:28284 [0] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26241:26241 [0] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26247:26247 [6] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28288:28839 [4] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-1:26245:26794 [4] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-2:28288:28288 [4] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26245:26245 [4] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28291:28838 [7] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-1:26248:26795 [7] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-2:28291:28291 [7] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26248:26248 [7] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28289:28841 [5] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-2:28289:28289 [5] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26246:26793 [5] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-1:26246:26246 [5] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28286:28840 [2] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-2:28286:28286 [2] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26243:26799 [2] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-1:26243:26243 [2] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28287:28834 [3] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-1:26244:26800 [3] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-1:26244:26244 [3] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28287:28287 [3] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-2:28285:28837 [1] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-1:26242:26797 [1] NCCL INFO Connected NVLS tree
compute-gpu-st-distributed-ml-2:28285:28285 [1] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
compute-gpu-st-distributed-ml-1:26242:26242 [1] NCCL INFO NCCL_NVLSTREE_MAX_CHUNKSIZE set by environment to 524288.
           8             2     float     sum      -1    83.99    0.00    0.00      0    57.98    0.00    0.00      0
          16             4     float     sum      -1    61.51    0.00    0.00      0    63.83    0.00    0.00      0
          32             8     float     sum      -1    54.87    0.00    0.00      0    65.04    0.00    0.00      0
          64            16     float     sum      -1    55.33    0.00    0.00      0    64.76    0.00    0.00      0
         128            32     float     sum      -1    55.33    0.00    0.00      0    56.79    0.00    0.00      0
         256            64     float     sum      -1    59.85    0.00    0.01      0    55.99    0.00    0.01      0
         512           128     float     sum      -1    70.50    0.01    0.01      0    56.88    0.01    0.02      0
        1024           256     float     sum      -1    58.11    0.02    0.03      0    57.46    0.02    0.03      0
        2048           512     float     sum      -1    60.76    0.03    0.06      0    60.34    0.03    0.06      0
        4096          1024     float     sum      -1    68.01    0.06    0.11      0    67.76    0.06    0.11      0
        8192          2048     float     sum      -1    103.9    0.08    0.15      0    71.37    0.11    0.22      0
       16384          4096     float     sum      -1    84.80    0.19    0.36      0    72.47    0.23    0.42      0
       32768          8192     float     sum      -1    141.1    0.23    0.44      0    73.73    0.44    0.83      0
       65536         16384     float     sum      -1    96.55    0.68    1.27      0    85.44    0.77    1.44      0
      131072         32768     float     sum      -1    83.79    1.56    2.93      0    82.97    1.58    2.96      0
      262144         65536     float     sum      -1    85.51    3.07    5.75      0    84.98    3.08    5.78      0
      524288        131072     float     sum      -1    91.31    5.74   10.77      0    91.35    5.74   10.76      0
     1048576        262144     float     sum      -1    103.6   10.12   18.97      0    102.3   10.25   19.21      0
     2097152        524288     float     sum      -1    120.6   17.39   32.61      0    120.9   17.34   32.52      0
     4194304       1048576     float     sum      -1    138.9   30.20   56.62      0    137.5   30.50   57.18      0
     8388608       2097152     float     sum      -1    178.0   47.14   88.38      0    176.5   47.53   89.13      0
    16777216       4194304     float     sum      -1    357.9   46.87   87.88      0    358.8   46.76   87.67      0
    33554432       8388608     float     sum      -1    426.0   78.76  147.68      0    426.8   78.62  147.42      0
    67108864      16777216     float     sum      -1    578.9  115.92  217.35      0    538.4  124.65  233.73      0
   134217728      33554432     float     sum      -1    809.2  165.87  311.01      0    806.0  166.52  312.23      0
   268435456      67108864     float     sum      -1   1343.7  199.78  374.59      0   1376.2  195.05  365.72      0
   536870912     134217728     float     sum      -1   2534.6  211.82  397.16      0   2511.6  213.75  400.79      0
  1073741824     268435456     float     sum      -1   4585.4  234.17  439.06      0   4592.7  233.79  438.36      0
  2147483648     536870912     float     sum      -1   9064.6  236.91  444.20      0   9046.9  237.37  445.07      0
  4294967296    1073741824     float     sum      -1    17339  247.71  464.45      0    17320  247.97  464.95      0
  8589934592    2147483648     float     sum      -1    33688  254.99  478.10      0    33688  254.98  478.10      0
 17179869184    4294967296     float     sum      -1    66283  259.19  485.98      0    66294  259.15  485.90      0
compute-gpu-st-distributed-ml-1:26246:26861 [5] NCCL INFO comm 0x5a26b77e7b50 rank 5 nranks 16 cudaDev 5 busId a8000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-2:28289:28903 [5] NCCL INFO comm 0x59f9118853a0 rank 13 nranks 16 cudaDev 5 busId a8000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:26247:26864 [6] NCCL INFO comm 0x603b5c4a92c0 rank 6 nranks 16 cudaDev 6 busId b9000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:26245:26860 [4] NCCL INFO comm 0x635d95ab3230 rank 4 nranks 16 cudaDev 4 busId 97000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-2:28288:28905 [4] NCCL INFO comm 0x642d66c73b40 rank 12 nranks 16 cudaDev 4 busId 97000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:26242:26863 [1] NCCL INFO comm 0x574e68045430 rank 1 nranks 16 cudaDev 1 busId 64000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-2:28290:28904 [6] NCCL INFO comm 0x618dae3dc250 rank 14 nranks 16 cudaDev 6 busId b9000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-2:28287:28902 [3] NCCL INFO comm 0x5565ccde75d0 rank 11 nranks 16 cudaDev 3 busId 86000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-2:28284:28901 [0] NCCL INFO comm 0x6267f170ca50 rank 8 nranks 16 cudaDev 0 busId 53000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-2:28285:28898 [1] NCCL INFO comm 0x5807d129f610 rank 9 nranks 16 cudaDev 1 busId 64000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:26243:26862 [2] NCCL INFO comm 0x5569a3b3a2b0 rank 2 nranks 16 cudaDev 2 busId 75000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-2:28291:28900 [7] NCCL INFO comm 0x5bdbaabd65f0 rank 15 nranks 16 cudaDev 7 busId ca000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:26241:26859 [0] NCCL INFO comm 0x55861914a600 rank 0 nranks 16 cudaDev 0 busId 53000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-2:28286:28899 [2] NCCL INFO comm 0x57a93296c420 rank 10 nranks 16 cudaDev 2 busId 75000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:26244:26858 [3] NCCL INFO comm 0x64bac1531ad0 rank 3 nranks 16 cudaDev 3 busId 86000 - Destroy COMPLETE
compute-gpu-st-distributed-ml-1:26248:26857 [7] NCCL INFO comm 0x598025a5fac0 rank 7 nranks 16 cudaDev 7 busId ca000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 127.29 
#
# Collective test concluded: all_reduce_perf
```