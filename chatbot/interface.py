import gradio as gr
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

def greet(text):
    result = generator(text, max_length=50, num_return_sequences=1)
    return result[0]["generated_text"]  


examples = [
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere cover 40%"]
]

app = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=5, label="Text"),
    outputs=gr.Textbox(label='Text'),
    examples=examples 
)

# Lanza la aplicación
app.launch()
