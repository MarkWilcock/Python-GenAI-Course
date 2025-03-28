# https://learn.microsoft.com/en-gb/answers/questions/2240877/sample-python-chat-code-error-seems-not-able-to-fi
import os
from openai import AzureOpenAI

from dotenv import load_dotenv
load_dotenv(override=True) # Load the .env file

azure_endpoint = os.getenv("AZURE_ENDPOINT_BASE")
azure_key =  os.getenv("AZURE_KEY")
deployment = "gpt-4o-mini"
#api_version = "2024-10-21"
api_version = "2024-12-01-preview"
print("\nazure endpoint", azure_endpoint, "\nazure key", azure_key, "\napi version", api_version, "\n\n\n")

try:
    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=azure_endpoint,
        api_key=azure_key,
    )
except Exception as e:
    print("failed", e)

print("connected !\n\n\n", client)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Answer questions briefly.",
        },
        {
            "role": "user",
            "content": "I am going to Valetta, what should I see?",
        }
    ],
    model="gpt-4o-mini"
)

print(response.choices[0].message.content)