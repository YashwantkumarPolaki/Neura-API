from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

# Your secret API key (you’ll use this inside GPT later)
API_KEY = "neura-secret-key-123"

@app.get("/")
def home():
    return {"message": "Neura API is running securely!"}

@app.post("/generate-code")
async def generate_code(request: Request):
    # Check API key
    headers = request.headers
    if headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    body = await request.json()
    language = body.get("language")
    task = body.get("task")

    # Simulate AI code generation
    return {
        "code": f"# Auto-generated code in {language}\n# Task: {task}\nprint('Hello from Neura!')"
    }
