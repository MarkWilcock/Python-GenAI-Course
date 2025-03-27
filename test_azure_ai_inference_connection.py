import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage
from dotenv import load_dotenv

load_dotenv(override=True)

azure_endpoint = os.getenv("AZURE_ENDPOINT")
azure_key =  os.getenv("AZURE_KEY")
model_name = "gpt-4o-mini"

client = ChatCompletionsClient(
    endpoint=azure_endpoint,
    credential=AzureKeyCredential(azure_key),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="I am going to Malta, what should I see?")
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=model_name
)

print(response.choices[0].message.content)