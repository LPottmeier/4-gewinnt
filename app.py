import requests
import json
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2)

def play():
    board_matrix = get_board()

def make_turn(row_number):
    r = requests.post("http://connect-4-api-dev1-connect4.apps.cluster-sva-7909.sva-7909.example.opentlc.com/turn")

def get_board():
    r = requests.post("http://connect-4-api-dev1-connect4.apps.cluster-sva-7909.sva-7909.example.opentlc.com/board")
    pp.pprint(r)


if __name__ == "__main__":
    play()
