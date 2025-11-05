from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

API_KEY = os.getenv("NEURA_API_KEY", "neura-secret-key-123")

# ✅ Define the input format using a Pydantic model
class CodeRequest(BaseModel):
    language: str
    task: str

@app.get("/")
def home():
    return {"message": "Neura API is running securely!"}

@app.post("/generate-code")
async def generate_code(request: CodeRequest, headers: Request):
    api_key = headers.headers.get("x-api-key")
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "code": f"# Auto-generated code in {request.language}\n# Task: {request.task}\nprint('Hello from Neura!')"
    }
