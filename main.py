from fastapi import FastAPI
from pydantic import BaseModel,Field
import ollama

app=FastAPI(title="qbot")

class questionSch(BaseModel):
    q:str=Field(min_length=1)

@app.get("/")
def health():
    return{
        "status":"ok",
        "message":"server running successfully"
    }

@app.post("/ask")
def ask(question:questionSch):
    res=ollama.chat(
    model='llama3.2',
    messages=[{
        'role':"user",
        'content':question.q
    }],
    # stream=True
)
    return res["message"]["content"]
   
    # for chunk in res:
    #     return(chunk["message"]["content"],end=" ")
   