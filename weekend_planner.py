import cohere

# Initialize the Cohere client
co = cohere.Client('qjgBfmYonpwhjFsICmNvdVCL4idkxCaSJvt7qYMJ')  # Replace with your actual API key

print("🗓️ Weekend Planner: Let me help you plan your weekend!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Weekend Planner: Enjoy your weekend! ☀️")
        break

    try:
        # Send message to Cohere's chat model
        response = co.chat(
            message=user_input,
            model="command-r-plus",  # Or 'command-r'
            temperature=0.7,
            max_tokens=300,
        )

        print(f"\n📅 Weekend Planner:\n{response.text.strip()}\n")

    except Exception as e:
        print(f"❌ Error: {e}")
