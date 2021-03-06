import requests
import json
import os
from pprint import PrettyPrinter

from ki import calculate_drop

pp = PrettyPrinter(indent=2)

player_number = os.environ['PLAYER_NUMBER']
#http://connect-4-api-dev1-connect4.apps.cluster-sva-7909.sva-7909.example.opentlc.com
board_host =os.environ['BOARD_HOST_URL']


def play():
    board_matrix, current_player = get_status()
    while(True):
        while(board_matrix):
            if current_player == player_number:
                new_turn_position = calculate_drop(board_matrix, player_number)
                make_turn(new_turn_position)
            board_matrix, current_player = get_status()
        board_matrix, current_player = get_status()


def make_turn(row_number):
    r = requests.post(board_host +"/turn",
                        data=json.dumps({"turn": "player_"+str(player_number), "position": row_number}), headers={'content-type': 'application/json'})
    print(r)

def get_status():
    r = requests.get(board_host+"/board")
    if r.json()["status"] != "running":
        return None, None
    board = []
    for i in range(0,6):
        board.append(r.json()["field"][i*7:(i*7)+7])
    #pp.pprint(board)
    return board, int(r.json()["turn"][len("player_"):])

if __name__ == "__main__":
    play()
