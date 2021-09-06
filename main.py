from fastapi import FastAPI

app = FastAPI()


@app.get("/status")
async def status():
    return {"message": "LibreYNAB is live!"}