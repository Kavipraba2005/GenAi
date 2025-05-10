import cohere

# Initialize Cohere client with your API key
co = cohere.Client('qjgBfmYonpwhjFsICmNvdVCL4idkxCaSJvt7qYMJ')  # Replace with your real key

# Loop for interactive shopping conversation
print("🛒 Shopping Assistant: Ask me anything about products, deals, or suggestions!")
while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Shopping Assistant: Happy shopping! 🛍️")
        break

    try:
        response = co.chat(
            message=user_input,
            model='command-r-plus'  # Or 'command-r'
        )
        print(f"\n🛍️ Shopping Assistant:\n{response.text.strip()}")
    except Exception as e:
        print(f"❌ Error: {e}")
