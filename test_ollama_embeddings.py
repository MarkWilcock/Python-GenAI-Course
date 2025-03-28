# pip install ollama

import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the input text
input_text = "This is a sample sentence to embed."

# Generate the embedding
response = client.embeddings(model='nomic-embed-text', prompt=input_text)

# Extract and print the embedding vector
embedding = response['embedding']
print("Embedding:", embedding)

""" 
import requests

url = "http://localhost:11434/api/embeddings"
data = {
    "model": "nomic-embed-text",
    "prompt": "This is a sample sentence to embed."
}

response = requests.post(url, json=data)

if response.ok:
    embedding = response.json()["embedding"]
    print("Embedding:", embedding)
else:
    print("Error:", response.status_code, response.text)
 """

