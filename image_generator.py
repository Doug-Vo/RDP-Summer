import openai
import requests
import os

# Use environment variable for the API key
openai.api_key = os.getenv('OPENAI_API_KEY')

extra_prompt = ("Help me create symbolic images that can convey this story: \n")

no_text_instruction = "\n. Make sure to USE NO TEXTS, WORDS, OR HUMAN FACES"

inputPath = "journal/journal_2.txt"

def chat_with_openai(input_content):
    try:
        message = (f"Here's my input:\n{input_content}\n"
                   f"Please summarize this content into three separate sentences that capture the key themes. "
                   f" Make sure to not delve to deep into any mental health or sensitive issues"
                   f" adjust the language to be light and family friendly around these subjects. "
                   "Each summary should be suitable for generating a distinct image.")

        # Create a chat completion
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )

        # Extract the AI's responses
        if 'choices' in response and len(response['choices']) > 0:
            choice = response['choices'][0]
            if 'message' in choice:
                summaries = choice['message']['content'].split('\n')  # Assuming each sentence is on a new line
                return summaries[:3]  # Ensure only three summaries are returned
            else:
                print("No message in the choice.")
        else:
            print("No choices in the response.")
    except Exception as e:
        print("An error occurred:", e)
    return []

def create_and_save_image(prompt, filename):
    try:
        # Construct the full prompt including the extra context
        full_prompt = extra_prompt + prompt + no_text_instruction
        print(prompt)
        response = openai.Image.create(
            prompt=full_prompt,
            n=1,
            size="1024x1024"
        )

        image_data = response['data'][0]
        image_url = image_data['url']
        print("Image URL:", image_url)

        # Download and save the image
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(image_response.content)
            print(f"Image saved successfully at {filename}")
        else:
            print("Failed to download the image. Status Code:", image_response.status_code)
    except Exception as e:
        print("An error occurred during image generation:", e)

# Main program logic
if __name__ == "__main__":
    print("\n=================== Creating Prompts ===================\n")
    try:
        with open(inputPath, 'r', encoding='utf-8') as file:
            content = file.read()
            summaries = chat_with_openai(content)
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    if summaries:
        for i, summary in enumerate(summaries, start=1):
            image_path = f"generated image/image_{i}.png"
            create_and_save_image(summary, image_path)
    else:
        print("No image prompts were generated.")
