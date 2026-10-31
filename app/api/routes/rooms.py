from fastapi import APIRouter, HTTPException

from app.rooms.manager import create_room, join_room, rooms
from app.schemas.rooms import RoomRequest, JoinRoomRequest, StartGameRequest

router = APIRouter()





@router.post("/create-room")
def create_new_room(request: RoomRequest):

    room_code = create_room(request.player_name)

    return {
        "message": "Room created successfully!",
        "room_code": room_code,
        "room": rooms[room_code]
    }


@router.post("/join-room")
def join_existing_room(request: JoinRoomRequest):

    result = join_room(
        request.room_code,
        request.player_name
    )

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result

@router.get("/room/{room_code}")
def get_room(room_code: str):
    room_code = room_code.upper()

    if room_code not in rooms:
        raise HTTPException(status_code=404, detail="Room does not exist!")

    room = rooms[room_code]

    return {
        "room_code": room_code,
        "players": room["players"],
        "status": room["status"]
    }


@router.post("/start-game/{room_code}")
def start_game(room_code: str, request: StartGameRequest):
    room_code = room_code.upper()

    if room_code not in rooms:
        raise HTTPException(status_code=404, detail="Room does not exist!")

    room = rooms[room_code]

    if request.player_id != room["host_id"]:
        raise HTTPException(status_code=403, detail="Only the host can start the game!")

    if room["status"] != "waiting":
        raise HTTPException(status_code=400, detail="Game has already started!")

    room["status"] = "playing"

    return {
        "message": "Game started successfully!",
        "room_code": room_code,
        "status": room["status"]
    }