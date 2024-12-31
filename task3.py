# Import necessary libraries
import spacy # type: ignore
from nltk.tokenize import word_tokenize # type: ignore
from nltk.corpus import stopwords # type: ignore
import string
import nltk
nltk.download('punkt_tab')

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Predefined responses (rule-based)
responses = {

    "greet": "Hello! How can I assist you today?",
    "bye": "Goodbye! Have a great day!",
    "name": "I am an AI chatbot created to assist you with your queries.",
    "age": "I'm timeless, as I'm just a piece of code!",
    "poetry":"Khudi ko kar buland itna ke har taqdeer se pehle\nKhuda bande se khud pooche, bata teri raza kya hai",
    "Thanks":"It Was a pleasure assisting you.",
    "default":"I'm sorry, I didn't understand that. Could you please rephrase?"
}

# Function to preprocess user input
def preprocess_input(user_input):
    # Tokenization and lowercasing
    tokens = word_tokenize(user_input.lower())
    # Removing punctuation and stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return tokens

# Function to determine intent based on keywords
def get_intent(preprocessed_tokens):
    if any(word in preprocessed_tokens for word in ["hello", "hi", "hey"]):
        return "greet"
    elif any(word in preprocessed_tokens for word in ["bye", "goodbye", "see you"]):
        return "bye"
    elif any(word in preprocessed_tokens for word in ["name", "who are you"]):
        return "name"
    elif any(word in preprocessed_tokens for word in ["age", "old"]):
        return "age"
    elif any(word in preprocessed_tokens for word in ["Thanks"]):
        return "Thanks"
    elif any(word in preprocessed_tokens for word in ["poetry", "iqbal"]):
        return "poetry"
    else:
        return "default"

# Main chatbot function
def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # Preprocess user input
        preprocessed_tokens = preprocess_input(user_input)
        
        # Determine intent
        intent = get_intent(preprocessed_tokens)
        
        # Fetch response based on intent
        response = responses.get(intent, responses["default"])
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    import nltk # type: ignore
    nltk.download("punkt")
    nltk.download("stopwords")
    chatbot()