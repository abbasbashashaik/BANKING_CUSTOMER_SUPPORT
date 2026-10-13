import ollama
from google.adk import Agent

# res=ollama.generate(
#     model='llama3.2',
#     prompt="what is python?"
# )
# print(res["response"])


# agent=Agent(
#     name="QAbot",
#     description="you are a trained agent which can be capable of answering the user queries in a simple and understandable way.",
#     model='llama3.2'
# )


res=ollama.chat(
    model='llama3.2',
    messages=[{
        'role':"system",
        'content':"what is python? explain in 10 points"
    }],
    stream=True
)
for chunk in res:
    print(chunk["message"]["content"],end=" ")
print()