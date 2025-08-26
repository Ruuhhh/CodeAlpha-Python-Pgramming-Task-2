# chatbot.py
# Author: Rutuja Wankhede
# Date: 2025-08-26
# Description: Simple rule-based chatbot for task 2

import time
import random

def chatbot():
    print("Chatbot: Hey there! Feel free to say 'hello', ask 'how are you', or say 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hello":
            responses = ["Hi!", "Hey! How’s it going?", "Hello! Nice to hear from you."]
            print("Chatbot:", random.choice(responses))

        elif user_input == "how are you":
            responses = [
                "I'm doing great, thanks for asking! How about you?",
                "I'm fine, thank you! What about you?",
                "All good here! Hope you’re doing well too."
            ]
            print("Chatbot:", random.choice(responses))

        elif user_input == "bye":
            farewells = ["Goodbye! Take care!", "See you later!", "Bye! Have a wonderful day!"]
            print("Chatbot:", random.choice(farewells))
            break

        else:
            apologies = [
                "Hmm, I didn't quite get that. Could you try saying it differently?",
                "Sorry, I’m not sure how to respond to that.",
                "Oops, I don't understand. Can you say something else?"
            ]
            print("Chatbot:", random.choice(apologies))

        # Simulate thinking time
        time.sleep(1)

if __name__ == "__main__":
    chatbot()


