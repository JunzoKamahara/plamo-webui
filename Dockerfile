FROM nvcr.io/nvidia/pytorch:23.09-py3
COPY launch.py /workspace/
RUN pip install transformers sentencepiece gradio

EXPOSE 7860

CMD ["python","/workspace/launch.py"]
