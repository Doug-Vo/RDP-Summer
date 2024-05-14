import openai
import requests
import os

# Use environment variable for the API key
openai.api_key = os.getenv('OPENAI_API_KEY')

extra_prompt = ("Help me create a symbolic pictures showing the story of: ")

inputPath = "journal/journal_2.txt"

def generate_additional_prompts(base_prompt):
    additional_prompts_1 = ""
    additional_prompts_2 = ""
    try:
        message = (f"Here's my input:\n{base_prompt}\n,"
                   f"Create a another variation of the prompt for image generation ")

        # Create a chat completion
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )

        # Extract the AI's response
        if 'choices' in response and len(response['choices']) > 0:
            choice = response['choices'][0]
            if 'message' in choice:
                additional_prompts_1 = choice['message']['content']
                print("Prompt: " + additional_prompts_1)
            else:
                print("No message in the choice.")
        else:
            print("No choices in the response.")
    except Exception as e:
        print("An error occurred:", e)

    try:
        message = (f"Here's my input:\n{base_prompt}\n,"
                   f"Create a another variation of the prompt with a different perspective"
                   f" for image generation ")

        # Create a chat completion
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )

        # Extract the AI's response
        if 'choices' in response and len(response['choices']) > 0:
            choice = response['choices'][0]
            if 'message' in choice:
                additional_prompts_2 = choice['message']['content']
                print("Prompt: " + additional_prompts_2)
            else:
                print("No message in the choice.")
        else:
            print("No choices in the response.")
    except Exception as e:
        print("An error occurred:", e)


    return [
        additional_prompts_1,
        additional_prompts_2
    ]
def chat_with_openai(input_content):
    img_prompt = ""
    try:
        message = (f"Here's my input:\n{input_content}\n"
                   f"\nPlease provide a one sentence summary and filter out any. "
                   f"Adjust the language to ensure it is respectful, cautious and filter out any"
                   f" representations of mental health ")

        # Create a chat completion
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )

        # Extract the AI's response
        if 'choices' in response and len(response['choices']) > 0:
            choice = response['choices'][0]
            if 'message' in choice:
                img_prompt = choice['message']['content']
                print("Prompt: " + img_prompt)
            else:
                print("No message in the choice.")
        else:
            print("No choices in the response.")
    except Exception as e:
        print("An error occurred:", e)
    return img_prompt

def create_and_save_image(prompt, filename):
    try:
        # Construct the full prompt including the extra context
        full_prompt = extra_prompt + prompt
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
            print(f"Image saved successfully at {filename}\n")
        else:
            print("Failed to download the image. Status Code:", image_response.status_code)
    except Exception as e:
        print("An error occurred during image generation:", e)



# Main program logic
if __name__ == "__main__":
    img_prompt = ""
    print("\n=================== Creating a base Prompt ===================\n")
    try:
        with open(inputPath, 'r', encoding= 'utf-8') as file:
            content = file.read()
            img_prompt = chat_with_openai(content)
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")



    if img_prompt:
        base_image_path = "generated image/base_image.png"
        create_and_save_image(img_prompt, base_image_path)


        print("\n=================== Creating additional Prompt ===================\n")
        additional_prompts = generate_additional_prompts(img_prompt)

        for i, prompt in enumerate(additional_prompts, start=1):
            create_and_save_image(prompt, f"generated image/variation_{i}.png")


    else:
        print("No image prompt was generated.")

