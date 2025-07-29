# edu_bot.py
import random

# Define chatbot knowledge base
knowledge_base = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon"],
    "greeting_response": ["Hello! 👋 How can I help you learn today?", "Hi there! Ready to explore some topics?"],
    
    "subjects": ["math", "science", "history", "ai", "python"],
    "subject_response": {
        "math": "Math is all about numbers, logic, and problem solving. Want to learn about Algebra or Geometry?",
        "science": "Science helps us understand the world. Do you want Physics, Chemistry, or Biology?",
        "history": "History is full of stories and lessons. Want to learn about World War II or Ancient Egypt?",
        "ai": "Artificial Intelligence is the future! We can start with basic AI concepts like machine learning.",
        "python": "Python is a beginner-friendly language. Want to learn about variables, loops, or functions?"
    },

    "bye": ["bye", "goodbye", "see you", "exit"],
    "bye_response": ["Goodbye! Keep learning. 📚", "See you next time! 👋"]
}


def get_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if user_input in knowledge_base["greeting"]:
        return random.choice(knowledge_base["greeting_response"])
    
    # Subjects
    for subject in knowledge_base["subjects"]:
        if subject in user_input:
            return knowledge_base["subject_response"][subject]
    
    # Goodbye
    if user_input in knowledge_base["bye"]:
        return random.choice(knowledge_base["bye_response"])
    
    return "I'm still learning. Try asking about math, science, history, Python, or AI."


# Main chat loop
print("EduBot 🤖: Hi! I’m EduBot, your learning assistant. Ask me anything about math, science, history, AI, or Python.")
while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print(f"EduBot 🤖: {response}")
    
    if user_input.lower() in knowledge_base["bye"]:
        break
