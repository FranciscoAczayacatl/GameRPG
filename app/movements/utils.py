from app.movements.constants import Attacks, Moves
from app.movements.exeptions import AttascksError, MovesError
import itertools


def replace_values_string(info_str: str) -> str:
    info_str = info_str.upper()
    new_str = []
    instructons = {
        "W": Moves.W.value,
        "S": Moves.S.value,
        "A": Moves.A.value,
        "D": Moves.D.value,
        "P": Attacks.P.value,
        "K": Attacks.K.value
    }
    for c in info_str:
        new_str.append(instructons[c])
    return "-".join(new_str)

def verify_moves(move):
    if Attacks.K.value not in move and Attacks.P.value not in move:
        if len(move)>5:
            raise MovesError()

    if move.count(Attacks.K.name) > 1 or move.count(Attacks.P.name) > 1:
        raise AttascksError()
    return move

def merge_info(golpes, movimientos):
    result = []

    for x, y in itertools.zip_longest(movimientos, golpes):
        text = ""
        if x:
          text = text + x
        if y:
            text = text + y
        result.append(text)
    return result
