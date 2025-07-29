import streamlit as st
import openai
import os
import nltk
from nltk.stem import WordNetLemmatizer

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

# Lesson content
lessons = {
    "python": {
        "text": "Python is a beginner-friendly programming language used in many areas like web development and AI.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
        "video": "https://www.youtube.com/watch?v=rfscVS0vtbw"
    },
    "ai": {
        "text": "Artificial Intelligence enables machines to learn and make decisions.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/17/Artificial_intelligence_icon.svg",
        "video": "https://www.youtube.com/watch?v=2ePf9rue1Ao"
    },
    "math": {
        "text": "Mathematics is the study of numbers, shapes, and patterns.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Mathematics.svg/1200px-Mathematics.svg.png",
        "video": "https://www.youtube.com/watch?v=1fp1Rms4Q5c"
    }
}

intents = {
    "python": ["python", "coding", "programming"],
    "ai": ["ai", "artificial", "intelligence", "machine", "learning"],
    "math": ["math", "algebra", "geometry", "calculus"]
}

def preprocess(text):
    words = nltk.word_tokenize(text.lower())
    return [lemmatizer.lemmatize(w) for w in words]

def get_intent(user_input):
    tokens = preprocess(user_input)
    for intent, keywords in intents.items():
        if any(word in tokens for word in keywords):
            return intent
    return None

def gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful and friendly educational chatbot."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7,
    )
    return response.choices[0].message.content

# UI section
st.set_page_config(page_title="EduBot", page_icon="📚")
st.title("📚 EduBot - Educational Chatbot")
st.markdown("**Created by Moira Nsovo Ngobeni**")
st.markdown("An educational chatbot to help you learn Python, AI, and Math.")
st.markdown("---")

user_input = st.text_input("Ask me about Python, AI, or Math:")

if user_input:
    intent = get_intent(user_input)
    
    if intent in lessons:
        lesson = lessons[intent]
        st.subheader(f"Lesson: {intent.capitalize()}")
        st.write(lesson["text"])
        st.image(lesson["image"], width=200)
        st.video(lesson["video"])

    st.markdown("---")
    if st.checkbox("💬 Ask GPT for a detailed answer"):
        answer = gpt_response(user_input)
        st.markdown(f"**GPT EduBot says:**  {answer}")
    else:
        st.write("Try checking the box above to get smart GPT-powered answers!")
