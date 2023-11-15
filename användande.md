
1. pip install -r requirements.txt
2. export PATH='/home/niels/.local/bin'



torchrun main.py

för 13b:
    torchrun --nproc_per_node 2 main.py



[error thread](https://github.com/facebookresearch/llama/issues/415)