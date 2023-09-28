# plamo-webui
WebUI container demo of Preferred Networks PLaMo-13B

プリファードネットワークさんの大規模言語モデル(LLM) PLaMo-13Bが公開されていたので簡単にgradioで動くコンテナを作ってみました。
I created container to run Preferred Networks' PLaMo-13B, a large-scale language model (LLM), with gradio. 
https://tech.preferred.jp/ja/blog/llm-plamo/

NGCのhttps://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch を使っています。

動作確認はNVIDIA A100 80GB PCIeで行いました。50GBほどGPUメモリを必要とするようです。
The operation was checked with NVIDIA A100 80GB PCIe, it seems to need about 50GB GPU memory.

# build
```
docker build . -t plamo-webui
```
# run
```
docker run plamo-webui
```
or
```
# デーモン動作
docker run --rm -d --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -p 7860:7860 plamo-webui
```

access http://localhost:7860/

# example

![plamo-13b-2](https://github.com/JunzoKamahara/plamo-webui/assets/106800851/a2f49b9d-99ae-4f9d-bc3e-853ac70cc337)
