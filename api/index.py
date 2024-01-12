from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def status():
    return {"messge": "OK from uvicorn server FastAPI"}

@app.get("/status")
def next_app():
    return {"message": " Hello  from  Next and Fast-API"}
