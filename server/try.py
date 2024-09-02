import ollama

print("Ollama started !!")

def chat_with_ollama():
    print("Chat with Ollama! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending the chat.")
            break

        # Generate a response from Ollama
        try:
            response = ollama.chat(
                model="llama3.1",
                messages=[
                    {
                        'role': 'user',
                        'content': user_input,
                    },
                ]
            )
            # Print the generated scene
            print("\nSummary\n", response['message']['content'])
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_ollama()
