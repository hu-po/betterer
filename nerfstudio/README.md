Trying to get Nerfstudio to work on my Linux Machine

```
export CUDA_HOME="/usr/local/cuda-11.8"
export LD_LIBRARY_PATH="/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH"
export PATH="/usr/local/cuda-11.8/bin:$PATH"
```

```
rm -rf ~/dev/tiny-cuda-nn/
cd ~/dev/
git clone --recursive https://github.com/nvlabs/tiny-cuda-nn
cd tiny-cuda-nn/
CUDA_ARCHITECTURES=61 cmake . -B build
cd bindings/torch
python setup.py install
```

```
rm -rf ~/dev/nerfstudio
cd ~/dev/
git clone git@github.com:nerfstudio-project/nerfstudio.git
cd nerfstudio
pip install --upgrade pip setuptools
pip install -e .
docker build --build-arg CUDA_ARCHITECTURES=61 --tag nerfstudio-61 -f Dockerfile .
```

```
docker run --gpus all \
            -v /home/tren/data:/workspace/ \
            -v /home/tren/.cache/:/home/user/.cache/ \
            -p 7007:7007 \
            --rm \
            -it \
            --shm-size=12gb \
            nerfstudio-61
```

```
 ns-train tensorf --data ~/data/nerfstudio/poster
```