"""phase 1 : send a chat request to the local Ollama server."""
import requests 

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3.5:2b-q4_K_M"



def chat(messages: list[dict]) -> dict:
    """Send the conversation to Ollama and return the assistant message. """
    payload = {
        "model" : MODEL,
        "messages" : messages,
        "stream" : False,
        "think" : False,
        "options" : {"temperature" : 0},
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()
    return response.json()["message"]

if __name__ == "__main__":
    history = [{"role" :"user", "content" : "Écris un haïku sur la pluie."}]
    answer = chat(history)
    print(answer["content"])
