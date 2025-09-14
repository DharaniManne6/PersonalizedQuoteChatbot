# 🗨️ PersonalizedQuoteChatbot
A simple Streamlit web app that provides personalized motivational quotes based on how you feel.
It uses NLP (Sentence Transformers) to match your mood with relevant motivational quotes from a Hugging Face dataset.

## 🚀 Features
- Accepts user input about mood or feelings
- Finds the most relevant motivational quotes
- Runs as a Streamlit web app
- Uses embeddings for fast performance

## 🔎 Tools and Libraries Used

| Tool/Library                                   | Why it’s used                                                          |
| ---------------------------------------------- | ---------------------------------------------------------------------- |
| **Python 3.10+**                               | Core programming language                                              |
| **Streamlit**                                  | To create an interactive, browser-based chatbot UI                     |
| **Hugging Face Datasets**                      | For loading the `motivational-quotes` dataset easily                   |
| **Sentence Transformers** (`all-MiniLM-L6-v2`) | To convert quotes & user input into embeddings for semantic similarity |
| **scikit-learn**                               | For cosine similarity calculation                                      |
| **NumPy & Pandas**                             | Efficient data handling & storage                                      |
| **.npy Embedding Cache**                       | Speeds up app by saving precomputed embeddings                         |


## ⚡ Why These Choices

- Streamlit → Simple & fast for creating interactive ML apps
- Sentence Transformers → Pretrained embeddings handle semantic meaning better than keyword search
- Cosine Similarity → Quick & effective way to find closest quotes
- .npy Cache → Saves computation time, making the app much faster on subsequent runs

## 🙌 Acknowledgements

- Dataset: [asuender/motivational-quotes](https://huggingface.co/datasets/asuender/motivational-quotes)  
- Embeddings: [Sentence Transformers](https://www.sbert.net/)  
- Framework: [Streamlit](https://streamlit.io/)

## ✅ Conclusion

This **Personalized Motivational Quote Chatbot** demonstrates how **NLP and sentence embeddings** can be used to provide meaningful, personalized content to users.  

By leveraging **Hugging Face datasets**, **Sentence Transformers**, and **Streamlit**, this project provides a fast, interactive, and user-friendly experience.  

It can be easily extended with:
- More categories of quotes  
- A richer dataset  
- Deployment to the web for public access  

This project showcases the power of combining **machine learning** with **real-time applications**, and serves as a solid foundation for further experimentation in **NLP-based recommendation systems**.
