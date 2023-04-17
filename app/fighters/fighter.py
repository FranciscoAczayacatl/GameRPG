from typing import List
from app.movements.base import Special
from app.movements.constants import Attacks
from app.movements.utils import replace_values_string
from app.settings import BASSIC_ATTACK_ENERGY, PLAYER_ENERGY

class Fighter:
    def __init__(self, name, specials:List[Special]) -> None:
        self.name = name
        self.specials = specials
        self.energy = PLAYER_ENERGY

    def get_moves(self, move):
        special = self.__move_is_special(move)
        if special:
            return special
        result_move = replace_values_string(move)
        if Attacks.P.value in result_move or Attacks.K.value in result_move:
            return {
                "name": result_move,
                "energy": BASSIC_ATTACK_ENERGY
            }
        return  {
            "name": result_move,
            "energy": 0
        }
    
    def __move_is_special(self, combination):
        for special in self.specials:
            special_info = special(self.name)
            if special_info.combination == combination:
                return {
                    "name": special_info.name,
                    "energy": special_info.energy
                }
        return None