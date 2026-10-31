import uuid

PLAYER_COLORS = ["red", "blue", "green", "yellow"]


def create_player(player_name, color):
    return {
        "id": str(uuid.uuid4()),
        "name": player_name,
        "color": color,
        "money": 1500,
        "position": 0,
        "properties": [],
        "in_jail": False,
        "jail_turns": 0,
        "is_bankrupt": False
    }