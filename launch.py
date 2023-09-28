import torch, transformers
import gradio as gr
model_name='pfnet/plamo-13b'
device = 0 if torch.cuda.is_available() else -1
pipeline = transformers.pipeline(
    "text-generation", model=model_name, trust_remote_code=True, device=device
)
def inference(data):
    output =  pipeline(data, max_new_tokens=32)
    return output[0]['generated_text']
demo = gr.Interface(
    fn=inference,
    inputs=gr.Textbox(lines=3, placeholder="プロンプト"),
        outputs=["text"],
        allow_flagging='never'
    )
if __name__ == "__main__":
    demo.queue().launch(server_name="0.0.0.0")
