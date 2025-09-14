import streamlit as st
import pandas as pd
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# ----------------------
# Must be first Streamlit command
# ----------------------
st.set_page_config(page_title="Motivational Quote Chatbot", page_icon="💡")

# ----------------------
# Suppress Hugging Face warnings
# ----------------------
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# ----------------------
# Load dataset & model
# ----------------------
@st.cache_data(show_spinner=True)
def load_data_and_embeddings():
    dataset = load_dataset("asuender/motivational-quotes", "quotes")
    df = pd.DataFrame(dataset['train'])[["quote", "author"]]
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    if os.path.exists("quote_embeddings.npy"):
        quote_embeddings = np.load("quote_embeddings.npy")
    else:
        quote_embeddings = model.encode(df['quote'].tolist(), show_progress_bar=True)
        np.save("quote_embeddings.npy", quote_embeddings)
    
    return df, model, quote_embeddings

df, model, quote_embeddings = load_data_and_embeddings()

# ----------------------
# Function to get top N quotes
# ----------------------
def get_top_quotes(user_input, top_n=5):
    input_emb = model.encode([user_input])
    similarities = cosine_similarity(input_emb, quote_embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:top_n]
    return df.iloc[top_indices]

# ----------------------
# Streamlit UI
# ----------------------
st.title("💡 Personalized Motivational Quote Chatbot")
st.write("Type your mood, feeling, or topic to get motivational quotes!")

user_input = st.text_input("How are you feeling today?")

if user_input:
    top_quotes = get_top_quotes(user_input)
    st.subheader("Here are your personalized quotes:")
    for idx, row in top_quotes.iterrows():
        st.write(f"> {row['quote']} — *{row['author']}*")
