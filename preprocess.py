import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def clean_review(review):
    # Remove HTML tags
    review = re.sub(r'<.*?>', '', review)
    
    # Remove special characters and numbers
    review = re.sub(r'[^a-zA-Z]', ' ', review)
    
    # Tokenize the review
    tokens = nltk.word_tokenize(review)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # Join tokens back to a single string
    cleaned_review = ' '.join(tokens)
    
    return cleaned_review
