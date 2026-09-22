from fastapi import FastAPI

app = FastAPI(title="SpendWise API")

@app.get("/")
def home():
    return {"message": "SpendWise backend is up and running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}