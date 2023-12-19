outdated

1. pip install -r requirements.txt



torchrun main.py

för 13b:
    torchrun --nproc_per_node 2 main.py



[error thread](https://github.com/facebookresearch/llama/issues/415)



Måste köras inifrån ```src```