from app.agent.core import run_agent



def main():
    print("AI Agent Started (type 'exit' to quit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = run_agent(user_input)
        print("Agent:", response)


if __name__ == "__main__":
    main()