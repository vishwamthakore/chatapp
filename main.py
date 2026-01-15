from fastapi import FastAPI
import uvicorn
from auth.routes import router as auth_router

app = FastAPI()

@app.get("/")
def home():
    return {
        "data" : "home"
    }

app.include_router(auth_router, prefix="/auth")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
