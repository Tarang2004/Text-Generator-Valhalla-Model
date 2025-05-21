import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model():
    # Load the Valhalla model and tokenizer
    model_name = "EleutherAI/gpt-neo-2.7B"  # Using GPT-Neo as Valhalla is not publicly available
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def generate_text(prompt, max_length=100, temperature=0.7):
    model, tokenizer = load_model()
    
    # Encode the prompt
    inputs = tokenizer(prompt, return_tensors="pt", padding=True)
    
    # Generate text
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=max_length,
            temperature=temperature,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True
        )
    
    # Decode and return the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(label="Enter your prompt", lines=3),
        gr.Slider(minimum=50, maximum=500, value=100, label="Maximum Length"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.7, label="Temperature")
    ],
    outputs=gr.Textbox(label="Generated Text", lines=10),
    title="Valhalla Text Generator",
    description="Generate creative text using the Valhalla model. Enter a prompt and adjust the parameters to control the generation.",
    examples=[
        ["Once upon a time in a magical forest", 150, 0.7],
        ["In a world where technology has advanced beyond imagination", 200, 0.8],
        ["The ancient warrior stood at the edge of the cliff", 100, 0.6]
    ]
)

if __name__ == "__main__":
    iface.launch() 