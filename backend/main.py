from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Reply in 2–3 lines only."},
        {"role": "user", "content": req.message}
    ]
    response = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-nano-8b-v1",
        messages=messages,
        temperature=0.7,
        max_tokens=100
    )
    return {"response": response.choices[0].message.content}
