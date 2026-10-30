
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from app.rooms import create_room, join_room, rooms

app = FastAPI(title="Monopoly Online")

class RoomRequest(BaseModel):
    player_name: str

class JoinRoomRequest(BaseModel):
    room_code: str
    player_name: str


@app.get("/")
def home():
    return {"message": "Monopoly server is running!"}

@app.post("/create-room")
def create_new_room(request: RoomRequest):
    
    room_code = create_room(request.player_name)

    return {
        "message": "Room created successfully!",
        "room_code": room_code,
        "room": rooms[room_code]
    }

@app.post("/join-room")
def join_existing_room(request: JoinRoomRequest):

    result = join_room(
        request.room_code,
        request.player_name
    )

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result