from fastapi import FastAPI

from app.api.routes.rooms import router as rooms_router

app = FastAPI(title="Monopoly Online")


@app.get("/")
def home():
    return {"message": "Monopoly server is running!"}


app.include_router(rooms_router)