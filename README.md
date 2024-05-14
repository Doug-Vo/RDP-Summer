
# <center> Research Development Project </center>
## Duc Vo
### May 2025
***

# Image Generation with OpenAI's DALL-E

This project uses OpenAI's GPT-4 and DALL-E models to generate symbolic images based on the themes extracted from a provided text file. The script ensures that the generated images do not contain any text, words, or human faces.

## Requirements

- Python 3.7 or later
- OpenAI API key
- Requests library

## Installation

**Install the required packages:**
   ```sh
   pip install openai requests
   ```

## Setup

1. **Set up the OpenAI API key:**
   Ensure your OpenAI API key is set as an environment variable. You can set it in your terminal session or add it to your shell profile file (e.g., `.bashrc`, `.zshrc`):
   ```sh
   export OPENAI_API_KEY='your-api-key-here'
   ```

2. **Place the input file:**
   Ensure that your input text file (`journal_2.txt`) is located in the `journal/` directory. The file should contain the content you want to summarize and generate images from.


The script will:
1. Read the content from the `journal/journal_2.txt` file.
2. Summarize the content into three separate sentences.
3. Generate three distinct images based on each summary sentence, ensuring no text, words, or human faces are included.
4. Save the generated images in the `generated image/` directory.

## Script Overview

The script consists of the following functions:
- `chat_with_openai(input_content)`: Sends the input content to OpenAI's GPT-4 to summarize it into three sentences.
- `create_and_save_image(prompt, filename)`: Uses DALL-E to generate an image based on the given prompt and saves the image to the specified filename.


### Generated Images

The images will be saved in the `generated image/` directory with filenames 
   - `image_1.png`
   - `image_2.png`
   - `image_3.png`

## Troubleshooting

- **File Not Found Error**: Ensure that the `journal_2.txt` file exists in the `journal/` directory.
- **API Key Error**: Verify that your OpenAI API key is correctly set as an environment variable.

