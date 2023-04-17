import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.game.start import verify_start
from app.game.utils import open_json_to_dict
from app.fighters.fighter import Fighter
from app.settings import PLAYER_1, PLAYER_2
from app.movements.specials import Remoyuken, Taladoken
from app.movements.utils import merge_info

def start_play(path):
    data = open_json_to_dict(path)
    start_player = verify_start(data)
    fighter_start =Fighter(start_player, [Remoyuken,Taladoken])

    if start_player == PLAYER_1:
        fighter_second = Fighter(PLAYER_2, [Remoyuken,Taladoken])
    else:
        fighter_second(PLAYER_1, [Remoyuken,Taladoken])
    
    moves_player_1 = {
        'player': PLAYER_1,
        'moves': merge_info(
            data['player1']['golpes'], data['player1']['moviminetos']
        )
    }
    moves_player_2 = {
        'player': PLAYER_2,
        'moves': merge_info(
            data['player2']['golpes'], data['player2']['moviminetos']
        )
    }

    players_move = [moves_player_1,moves_player_2]
    for player in players_move:
        if player['player'] == fighter_start.name:
            start_player_moves = player['moves']
        if player['player'] == fighter_start.name:
            second_player_moves = player['moves']

    while fighter_start.energy >0 and fighter_second.energy > 0:
        for start_move in start_player_moves:
            for second_move in second_player_moves:
                pass 
            move_initial = fighter_start.get_moves(start_move)
            print(f'la vida de {fighter_start.name} es {fighter_start.energy}')
            print(fighter_start.name, 'hace ', move_initial['name'], f" e inflige {move_initial['energy']} daño")
            print('')

            fighter_second.energy = fighter_second.energy - move_initial['energy']
            if fighter_start.energy == 0 :
                print(fighter_second.name,  f"ha ganado y le quedan {fighter_second.energy}")
            move_second = fighter_second.get_moves(second_move)
            print(f'la vida de {fighter_second.name} es {fighter_second.energy}')
            print(fighter_second.name, 'hace ', move_second['name'], f" e inflige {move_second['energy']} daño")
            print('')
            fighter_start.energy = fighter_start.energy - move_second['energy']
            if fighter_second.energy == 0 :
                print(fighter_start.name,  f"ha ganado y le quedan {fighter_start.energy}")
        

start_play("data/json_1_arnaldor.json")