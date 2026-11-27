"""Phase 2: ask the model to call a tool (without executing it yet)."""

import json

import requests 

from phase1_chat import MODEL, OLLAMA_URL

LIST_DIRECTORY_TOOL = {
    "type" : "function",
    "function" : {
        "name" : "list_directory",
        "description" : "List the files and the folders inside the user's computer.",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "path" : {
                    "type" :"string",
                    "description" : "Absolute path of the directpry to list. e.g. C:\\Users\\HP\\Desktop",
                },
            },
            "required" :["path"],
        },
    },
}

def chat_with_tools(messages : list[dict], tools : list[dict]) -> dict :
    """Send the conversation and the available tools; return the assistant message. """
    payload = {
        "model" : MODEL,
        "messages" : messages,
        "tools" :tools,
        "stream" : False,
        "think" : False,
        "options" : {"temperature" : 0},
    }
    response = requests.post(OLLAMA_URL, json = payload, timeout = 120)
    response.raise_for_status()

    return response.json()["message"]


if __name__ == "__main__":
    questions = [
        "Quels fichiers y a-t-il dans C:\\Users\\HP\\Desktop ?",
        "Écris un haïku sur la pluie.",
    ]
    for question in questions : 
        messages = [{"role" : "user" , "content" : question}]
        answer = chat_with_tools(messages, [LIST_DIRECTORY_TOOL])
        print("QUESTION : ",question)
        print(json.dumps(answer, indent =2, ensure_ascii=False))
        print("-" * 40)