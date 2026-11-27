"""Phase 1: prove that the model has no memory between requests """
from phase1_chat import chat

#Test1 : two separate requests, no shared history

chat([{"role":"user", "content":"Je m'appelle Ange. Retiens bien mon prénom."}])
answer = chat([{"role":"user", "content" : "Comment je m'appelle?"}])
print("WITHOUT history:", answer["content"])
print("-" *  40)

#Test 2: same questions, but we resend the whole conversation
history = [{"role" : "user","content" : "Je m'appelle Ange. Retiens bien mon prénom."}]
first_answer = chat(history)
history.append(first_answer)
history.append({"role" : "user", "content": "comment je m'appelle ?"})
answer = chat(history)
print("WITH history:", answer["content"])
print("-" * 40)

#Show what was actually sent to the model in test 2
for message in history:
    print(f"[{message['role']}]{message['content']}")