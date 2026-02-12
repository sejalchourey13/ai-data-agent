import pandas as pd
import requests
import json

# Load dataset
df = pd.read_csv("data/dataset.csv")

# Basic analysis
summary = df.groupby("Category")["Sales"].sum().to_dict()

user_question = "Which product is performing best and why?"

prompt = f"""
You are a data analyst AI.
Here is the sales data summary:
{summary}

Answer the question:
{user_question}
"""

# Call Ollama API
response = requests.post(
    "http://ollama:11434/api/generate",
    json={
        # "model": "gemma:2b",
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()
print("\n AI Response:\n")
print(result["response"])
