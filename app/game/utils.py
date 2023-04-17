import json

from game.exeptions import GameTypeFileError

def open_json_to_dict(path: str) -> dict: 
    """
    converts json to dict
    Arguments:
        path: str: Path to file
    Returns:
        data: dict: Info from player
    """
    if path.endswith(".json"):
        with open(path, 'r') as info_player:
            data = json.load(info_player)
            return data
    raise GameTypeFileError()