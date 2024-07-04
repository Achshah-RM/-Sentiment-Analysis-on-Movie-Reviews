import re
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from model import lstm_model, tokenizer, max_len
from preprocess import clean_review

def analyze_review(review):
    review_cleaned = clean_review(review)
    review_seq = tokenizer.texts_to_sequences([review_cleaned])
    review_pad = pad_sequences(review_seq, maxlen=max_len)
    prediction = lstm_model.predict(review_pad)
    return "Positive" if prediction[0][0] > 0.5 else "Negative"
