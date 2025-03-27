import requests

def chat_with_llama2():
    print("Simple Chat with Llama2 locally on Ollama. Type 'quit' or 'exit' to stop.")
    
    while True:
        user_input = input("User: ")
        if user_input.strip().lower() in ["quit", "exit"]:
            break
        
        # JSON payload to Ollama
        payload = {
            "prompt": user_input,
            "model": "llama3.2:1b",
            "stream": False
        }
        
        try:
            response = requests.post("http://localhost:11434/api/generate", json=payload)
            response.raise_for_status()  # Raise an error if request failed
            # Ollama by default returns plain text or JSON with the generated text
            print(response.json().get("response", ""))
        except requests.exceptions.RequestException as e:
            print("Error communicating with Ollama:", e)
            break

if __name__ == "__main__":
    chat_with_llama2()
