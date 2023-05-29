#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import joblib

# Load model
model = joblib.load('hate_speech_detector.joblib')

# Function to process input
def preprocess_text(text):
    # Initialize lemmatizer, stemmer and TweetTokenizer
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    tweet_tokenizer = TweetTokenizer()

    # Define stopwords
    stop_words = set(stopwords.words('english'))

    # Remove 'RT' as it refer to a re-tweet in the tweeet and is non important for our model
    stop_words.update(['RT', 'I'])

    # Tokenize the text
    word_tokens = tweet_tokenizer.tokenize(text)

    # Lemmatize the tokens, stem the tokens, remove stopwords and non-alphabetic tokens
    processed_tokens = [stemmer.stem(lemmatizer.lemmatize(w)) for w in word_tokens if w not in stop_words and w.isalpha()]

    # Join the tokens back into a single string and return it
    return ' '.join(processed_tokens)

# Streamlit code
st.title("Hate Speech Detector")

user_input = st.text_input("Enter the text you want to analyze:")

if st.button("Analyze"):
    # Preprocess the input
    processed_input = preprocess_text(user_input)

    # Make the prediction
    prediction = model.predict([processed_input])

    if prediction[0] == 0: 
        st.write("This text is likely to be offensive.")
    elif prediction[0] == 1:
        st.write("This text is likely to be hate speech.")
    else:
        st.write("This text is neither hate speech nor offensive.")


# In[ ]:




