from fastapi import FastAPI
from random import choice
import uvicorn

app = FastAPI()

# 1. Health check
@app.get("/health")
async def health():
    return {"status": "ok"}

# 2. Home API
@app.get("/home_api")
async def home_api():
    return {"message": "Welcome to the Home API!"}

# 3. Fun fact endpoint
@app.get("/fun_fact")
async def fun_fact():
    facts = [
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries aren't.",
        "A group of flamingos is called a flamboyance.",
        "Honey never spoils.",
        "Cows have best friends and get stressed when separated."
    ]
    return {"fun_fact": choice(facts)}

# Run the app if executed directly
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
