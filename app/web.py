from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app.agent.core import run_agent

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
def home():
    with open("app/static/index.html", "r", encoding="utf-8") as file:
        return file.read()


@app.post("/chat")
def chat(request: ChatRequest):
    response = run_agent(request.message)
    return {"response": response}