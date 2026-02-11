import streamlit as st
import pandas as pd
import requests
import json

# Load dataset
df = pd.read_csv("data/dataset.csv")
summary = df.groupby("product")["sales"].sum().to_dict()

st.title("AI Data Analyst Agent - Version 2")

# User input
user_question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if not user_question.strip():
        st.warning("Please enter a question first!")
    else:
        # Create prompt for Ollama
        prompt = f"""
You are a data analyst AI.
Here is the sales data summary:
{summary}

Answer the question:
{user_question}
"""
        try:
            response = requests.post(
                "http://ollama:11434/api/generate",  # Ollama container name
                json={
                    "model": "gemma:2b",
                    "prompt": prompt,
                    "stream": False
                },
                timeout=30
            )
            result = response.json()
            st.subheader(" AI Response:")
            st.write(result.get("response", "No response from model."))
        except Exception as e:
            st.error(f"Error communicating with Ollama: {e}")
