import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_bot():
    print("Welcome to the CLI Chatbot! Type 'exit' to quit.\n")
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Generate response using OpenAI GPT
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            bot_response = response['choices'][0]['message']['content']
            print(f"Bot: {bot_response}\n")
        except openai.error.AuthenticationError:
            print("Error: Invalid OpenAI API key. Please check your .env file.")
            break
        except openai.error.RateLimitError:
            print("Error: Rate limit exceeded. Please try again later.")
            break
        except openai.error.APIConnectionError:
            print("Error: Failed to connect to OpenAI API. Check your internet connection.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    chat_with_bot()