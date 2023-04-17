from app.movements.base import Special
from app.movements.constants import RemoyukenCombination, RemoyukenEnergy, SpecialsNames, TaladokenCombination, TaladokenEnergy
from app.settings import PLAYER_1, PLAYER_2


class Taladoken(Special):
    
    def __init__(self, fighter) -> None:
        if fighter == PLAYER_1:
            self.combination = TaladokenCombination.PLAYER1_COMBINATION.value
            self.energy = TaladokenEnergy.PLAYER1_COMBINATION.value
            self.name = SpecialsNames.TALADOKEN.value
        if fighter == PLAYER_2:
            self.combination = TaladokenCombination.PLAYER2_COMBINATION.value
            self.energy = TaladokenEnergy.PLAYER2_COMBINATION.value
            self.name =SpecialsNames.TALADOKEN.value

class Remoyuken(Special):
    
    def __init__(self, fighter) -> None:
        if fighter == PLAYER_1:
            self.combination = RemoyukenCombination.PLAYER1_COMBINATION.value
            self.energy = RemoyukenEnergy.PLAYER1_COMBINATION.value
            self.name = SpecialsNames.REMOYUKEN.value
        if fighter == PLAYER_2:
            self.combination = RemoyukenCombination.PLAYER2_COMBINATION.value
            self.energy = RemoyukenEnergy.PLAYER2_COMBINATION.value
            self.name =SpecialsNames.REMOYUKEN.value