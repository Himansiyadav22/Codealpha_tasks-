import random
import datetime

def show_help():
    print("--- AVAILABLE COMMANDS ---")
    print("hello")
    print("how are you")
    print("bye")
    print("joke")
    print("motivation")
    print("cube")
    print("help")
    print("--------------------------")

def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer go to the doctor? It caught a virus."
    ]
    print(random.choice(jokes))

def motivation():
    quotes = [
        "Education is the key of success.",
        "Believe in yourself."
    ]
    print(random.choice(quotes))

def cube_number():
    n = int(input("Enter a number: "))
    print(f"Cube of {n} is {n**3}")

print("--------------------------")
print("   WELCOME TO SMART CHATBOT")
print("--------------------------")
print("Type 'help' to see commands.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        responses = ["Hello!", "Hi there!", "Nice to meet you!", "Greetings!"]
        print("Bot: " + random.choice(responses))

    elif user == "how are you":
        responses = ["I am fine.", "Doing great!", "All good!"]
        print("Bot: " + random.choice(responses))

    elif user == "joke":
        tell_joke()

    elif user == "motivation":
        motivation()

    elif user == "cube":
        cube_number()

    elif user == "help":
        show_help()

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")
        