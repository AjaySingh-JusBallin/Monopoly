
import random
import string

from app.players import create_player, PLAYER_COLORS

rooms = {}


def generate_room_code():
    characters = string.ascii_uppercase + string.digits

    while True:
        code = ''.join(random.choices(characters, k=6))

        if code not in rooms:
            return code


def get_available_color(room):
    used_colors = [player["color"] for player in room["players"]]

    for color in PLAYER_COLORS:
        if color not in used_colors:
            return color

    return None


def create_room(player_name):
    room_code = generate_room_code()

    color = PLAYER_COLORS[0]
    player = create_player(player_name, color)

    rooms[room_code] = {
        "players": [player],
        "max_players": 4,
        "status": "waiting"
    }

    return room_code


def join_room(room_code, player_name):
    room_code = room_code.upper()

    if room_code not in rooms:
        return {"error": "Room does not exist!"}

    room = rooms[room_code]

    if len(room["players"]) >= room["max_players"]:
        return {"error": "Room is full!"}

    if room["status"] != "waiting":
        return {"error": "Game has already started!"}

    for player in room["players"]:
        if player["name"].lower() == player_name.lower():
            return {"error": "Player already exists!"}

    color = get_available_color(room)

    if color is None:
        return {"error": "No colors available!"}

    player = create_player(player_name, color)

    room["players"].append(player)

    return {
        "message": "Joined room successfully!",
        "room_code": room_code,
        "players": room["players"]
    }
