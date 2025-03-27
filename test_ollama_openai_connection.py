
import os
from dotenv import load_dotenv
import openai

load_dotenv() # Load the .env file

client = openai.OpenAI(base_url=os.getenv("OLLAMA_ENDPOINT"), api_key="nokeyneeded")

MODEL_NAME = os.getenv("OLLAMA_MODEL")

completion = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    max_tokens=500,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful geography expert. Be brief in your answers."},
        {"role": "user", "content": "What is the population of Malta?"},
    ]
)
print(completion.choices[0].message.content)
