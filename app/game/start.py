from app.settings import PLAYER_1, PLAYER_2

def verify_start(data):
    player_1_moves = "".join(data['player1']["moviminetos"])
    player_2_moves = "".join(data['player2']["moviminetos"])
    player_1_golpe = "".join(data['player1']["golpes"])
    player_2_golpe = "".join(data['player2']["golpes"])

    player_1_total = player_1_moves + player_1_golpe
    player_2_total = player_2_moves + player_2_golpe

    if len(player_1_total) > len(player_2_total):
        return PLAYER_2
    
    elif len(player_1_total) == len(player_2_total):
        
        if len(player_1_moves) > len(player_2_moves):
            return PLAYER_2
        
        if len(player_1_moves) == len(player_2_moves):
            
            if len(player_1_golpe)> len(player_2_golpe):
                return PLAYER_2
            
            else:
                return PLAYER_1
        else:
            return PLAYER_1
    else :
        return PLAYER_1