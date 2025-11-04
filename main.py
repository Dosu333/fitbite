from agent import get_response


def main():
    print("Welcome to the Restaurant Assistant Chatbot!")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Thank you for visiting! Goodbye!")
            break

        response = get_response(user_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()
