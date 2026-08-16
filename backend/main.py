from fastapi import FastAPI

app = FastAPI(title="TouchStone API")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "TouchStone backend is alive 🚀"
    }