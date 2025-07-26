# chatbot.py

print("Hello! I'm ChatBot. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! How can I help you today?")
    elif user_input == "how are you":
        print("Bot: I'm just a bunch of code, but I'm doing great!")
    elif user_input == "what is your name":
        print("Bot: I'm a simple rule-based chatbot.")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    elif user_input == "exit":
        print("Bot: Exiting... Thank you!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")

