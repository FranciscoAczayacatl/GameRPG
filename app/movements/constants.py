from enum import Enum


class Moves(Enum):
    W = "ARRIBA"
    S = "ABAJO"
    A = "IZQUIERDA"
    D = "DERECHA"

class Attacks(Enum):
    P = "GOlPE"
    K = "PATADA"

class TaladokenCombination(Enum):
    PLAYER1_COMBINATION = "DSDP"
    PLAYER2_COMBINATION = "ASAP"

class TaladokenEnergy(Enum):
    PLAYER1_COMBINATION = 3
    PLAYER2_COMBINATION = 2

class SpecialsNames(Enum):
    TALADOKEN = "Taladoken"
    REMOYUKEN = "Remoyuken"

class RemoyukenCombination(Enum):
    PLAYER1_COMBINATION = "SDK"
    PLAYER2_COMBINATION = "SAK"

class RemoyukenEnergy(Enum):
    PLAYER1_COMBINATION = 3
    PLAYER2_COMBINATION = 2

MOVES_ERROR_CODE = 678
MOVES_ERROR_MSG = 'Los movimientos no pueden ser mas de 5'
ATTASCKS_ERROR_CODE = 679
ATTASCKS_ERROR_MSJ = 'Solo puede haber un golpe'

ERROR_MESSAGES = {
    MOVES_ERROR_CODE: MOVES_ERROR_MSG,
    ATTASCKS_ERROR_CODE: ATTASCKS_ERROR_MSJ
}
