from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)
    return summary[0]['summary_text']  # or however you want to extract the summary

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    output = gr.Textbox(label="Summary")
    btn = gr.Button("Summarize")
    
    btn.click(fn=predict, inputs=textbox, outputs=output)

demo.launch(share=True)
