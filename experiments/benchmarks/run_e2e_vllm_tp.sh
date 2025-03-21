# Copyright (c) 2024 Microsoft
# Licensed under The MIT License [see LICENSE for details]

# Load data
wget https://raw.githubusercontent.com/FranxYao/chain-of-thought-hub/main/gsm8k/lib_prompt/prompt_hardest.txt

VLLM_WORKER_MULTIPROC_METHOD=spawn python experiments/benchmarks/benchmark_e2e_vllm_tp.py \
    --attn_type minference \
    --context_window 100_000 \
    --tensor_parallel_size 4
