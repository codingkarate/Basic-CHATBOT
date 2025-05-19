import nltk
import spacy
from nltk.tokenize import word_tokenize
import random

# Load English tokenizer and tagger from spaCy
nlp = spacy.load("en_core_web_sm")

# Predefined responses (rule-based for simplicity)
responses = {
    "greeting": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you?"],
    "how_are_you": ["I'm doing great, thanks for asking!", "I'm just a bot, but I'm doing fine!"],
    "weather": ["The weather is always perfect in the cloud!", "Sunny with a chance of code."],
    "name": ["You can call me ChatBot!", "I’m your friendly chatbot."],
    "goodbye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure I understand. Can you rephrase?", "Interesting! Tell me more."]
}

# Simple intent matcher using spaCy
def get_intent(user_input):
    doc = nlp(user_input.lower())

    if any(token.lemma_ in ['hi', 'hello', 'hey'] for token in doc):
        return "greeting"
    elif "how" in user_input and "you" in user_input:
        return "how_are_you"
    elif "weather" in user_input:
        return "weather"
    elif "your name" in user_input or "who are you" in user_input:
        return "name"
    elif any(token.lemma_ in ['bye', 'goodbye', 'see you'] for token in doc):
        return "goodbye"
    else:
        return "default"