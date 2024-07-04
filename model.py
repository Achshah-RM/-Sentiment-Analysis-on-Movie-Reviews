import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import LSTM, Bidirectional 

# Define max_len used for padding
max_len = 100

# Load the LSTM model
model_path = 'lstm_model.h5'
lstm_model = load_model(model_path, custom_objects={"LSTM": LSTM, "Bidirectional": Bidirectional})

# Load the tokenizer
tokenizer_path = 'tokenizer.pkl'
with open(tokenizer_path, 'rb') as handle:
    tokenizer = pickle.load(handle)

