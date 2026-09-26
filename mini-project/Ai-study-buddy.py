

import datetime

hour = datetime.datetime.now().hour

def greet_user():
    if 5 <= hour < 12:
        print("Good morning! I'm your AI study buddy 🤖. How can I assist you today?")
    elif 12 <= hour < 18:
        print("Good afternoon! I'm your AI study buddy 🤖. How can I assist you today?")
    else:
        print("Good evening! I'm your AI study buddy 🤖. How can I assist you today?")

greet_user()
print("You can talk to me. Type 'bye' anytime to exit.\n")

responses = {

"hello": "Hi there! How can I help you today?",
"hi": "Hi there! How can I help you today?",
"who are you": "I’m your AI Study Buddy.",
"how are you": "I’m just code, but I feel great when you run me!",
"motivate me": "Keep going! Every bug you fix makes you a bettercoder.",
"python": "Python is powerful — it can do AI, automation, and much more!",
"sad": "Don’t worry! Even code breaks sometimes, but it always runs again.",
"happy": "That’s great to hear! Keep that positive energy going🎉",
"time": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
"bye": "Goodbye! Keep learning and keep smiling."

}

def get_response(user_input):
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    return "I’m not sure how to respond to that. Can you ask something else?"

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("AI 🤖: " + responses["bye"])
        break
    response = get_response(user_input)
    print("AI 🤖: " + response)

