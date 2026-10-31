from pydantic import BaseModel


class RoomRequest(BaseModel):
    player_name: str


class JoinRoomRequest(BaseModel):
    room_code: str
    player_name: str

class StartGameRequest(BaseModel):
    player_id: str