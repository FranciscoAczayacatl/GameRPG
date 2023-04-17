from app.fighters.fighter import Fighter
from app.movements.specials import Taladoken, Remoyuken
from app.settings import PLAYER_1


def test_special_fighter():
    tony = Fighter(PLAYER_1, [Taladoken, Remoyuken])
    result = tony.get_moves("SDK")
    assert result["name"] == "Remoyuken"

def test_only_moves():
    tony = Fighter(PLAYER_1, [Taladoken, Remoyuken])
    result = tony.get_moves("ASWD")
    assert result["name"] == 'IZQUIERDA-ABAJO-ARRIBA-DERECHA'
    assert result["energy"] == 0

def test_basic_attack():
    tony = Fighter(PLAYER_1, [Taladoken, Remoyuken])
    result = tony.get_moves("ASWDK")
    assert result["name"] == 'IZQUIERDA-ABAJO-ARRIBA-DERECHA-PATADA'
    assert result["energy"] == 1