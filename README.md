# Text-Generator-Valhalla-Model
This application use Valhalla model by hugging face to generate text based on the prompt enter by user.
# Valhalla Text Generator

This is a text generation application that uses the GPT-Neo model (as a substitute for Valhalla) to generate creative text based on user prompts.

## Features

- Interactive web interface using Gradio
- Adjustable text generation parameters
- Example prompts to get you started
- Real-time text generation

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python valhalla_app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://127.0.0.1:7860)

3. Enter your prompt in the text box and adjust the parameters:
   - Maximum Length: Controls how long the generated text will be
   - Temperature: Controls the creativity of the generation (higher values = more creative)

4. Click "Submit" to generate text

## Parameters

- **Prompt**: The starting text that will be used to generate the continuation
- **Maximum Length**: The maximum number of tokens in the generated text (50-500)
- **Temperature**: Controls randomness in the generation (0.1-1.0)
  - Lower values (e.g., 0.3) make the output more focused and deterministic
  - Higher values (e.g., 0.8) make the output more diverse and creative

## Note

The first time you run the application, it will download the model which might take some time depending on your internet connection. 
PS:- The file size might suprise you :>>>
