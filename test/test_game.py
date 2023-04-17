from app.game.exeptions import GameTypeFileError
from app.game.start import verify_start
from app.game.utils import open_json_to_dict
import pytest

from app.settings import PLAYER_1

def test_get_info_player_from_json():
    result = open_json_to_dict('../app/data/json_1_arnaldor.json')
#   assert type(result) == dict
    assert "player1" in result.keys()
    
def test_file_type_error():
    with pytest.raises(GameTypeFileError):
        result = open_json_to_dict('app/data/json_1_arnaldor.txt')

def test_star():
    result = open_json_to_dict('../app/data/json_1_arnaldor.json')
    data = verify_start(result)
    assert data == PLAYER_1