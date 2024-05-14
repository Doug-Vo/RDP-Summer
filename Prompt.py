import openai

# Set your API key here
openai.api_key = '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'

def chat_with_openai(message):
    try:
        # Create a chat completion
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the model version, e.g., "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )

        # Debug: Print the raw response to understand what is received
        print("Full response:", response)

        # Print the AI's response
        if 'choices' in response and len(response['choices']) > 0:
            choice = response['choices'][0]
            if 'message' in choice:
                msg = choice['message']
                if msg['role'] == 'assistant':
                    print("Assistant:", msg['content'])
            else:
                print("No message in the choice.")
        else:
            print("No choices in the response.")

    except Exception as e:
        print("An error occurred:", e)

# Example usage
chat_with_openai("How long of a prompt can I give you")
