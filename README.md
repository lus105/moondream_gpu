# 🌔 moondream

A tiny vision language model that kicks ass and runs anywhere.
Original repo: https://github.com/vikhyat/moondream

- - - - 

This repository contains detailed instructions and modifications for running moondream model in windows environment with gpu support.

#### Environment setup (conda)
```bash
# clone project
git clone https://github.com/lus105/moondream_gpu
# change directory
cd moondream_gpu
# update conda
conda update -n base conda
# create conda environment
conda create --name moondream_gpu python=3.11
# activate conda environment
conda activate moondream_gpu
# install pytorch with cuda support
pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 --index-url https://download.pytorch.org/whl/cu121
# install rest of dependancies
pip install -r requirements.txt
```

#### Model download
```bash
# run from root directory
python models/model_download.py
```

#### Run inference (pytorch)
```bash
# open and run notebook
notebooks/inference_torch.ipynb
```

#### Run inference (onnx)
```bash
# open and run notebook
notebooks/inference_onnx.ipynb
```

#### Start local inference server (onnx)
```bash
# run from root
python clients/python/moondream/cli.py serve --model "path/to/moondream-2b-int8.mf"
```