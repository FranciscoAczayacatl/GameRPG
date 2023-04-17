from app.movements.exeptions import MovesError, AttascksError
from app.movements.specials import Remoyuken, Taladoken
from app.movements.utils import merge_info, replace_values_string, verify_moves
from app.settings import PLAYER_1, PLAYER_2
from app.game.utils import open_json_to_dict
import pytest

def test_replace_instructions():
    result = open_json_to_dict('../app/data/json_1_arnaldor.json')
    movements = result["player1"]["moviminetos"]
    result = replace_values_string(movements[0])
    assert result == 'DERECHA'

def test_special_name_taladoken():
    special = Taladoken(
        PLAYER_2
    )
    assert special.combination == "ASAP"

def test_special_name_remoyuken():
    special = Remoyuken(
        PLAYER_2
    )
    assert special.combination == "SAK"

def test_error_moves():
    with pytest.raises(MovesError):
        result = verify_moves('ASDSADADSKDSASS')

def test_errors_basic_attack():
        with pytest.raises(AttascksError):
            result = verify_moves('PP')

def test_merge_info():
     result = merge_info(["ASA", "DA"], ["P"])
     assert result[0] == "ASAP"
