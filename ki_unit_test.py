from ki import calculate_drop
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)

def init_board():
    playboard = []
    for i in range(0,6):
        playboard.append([0,0,0,0,0,0,0])
    return playboard

def player_won(board):
    in_a_row = [0, 0]
    # horizontal check
    for i in range(0,6):
        in_a_row = [0, 0]
        for j in range(0,7):
            if board[i][j] != 0:
                in_a_row[board[i][j]-1] += 1
            else:
                in_a_row = [0,0]
            if [d for d in in_a_row if d == 4]:
                return [k for k in range(0,2) if in_a_row[k] == 4][0]+1
    # vertical check
    for j in range(0,7):
        in_a_row = [0, 0]
        for i in range(0,6):
            if board[i][j] != 0:
                in_a_row[board[i][j]-1] += 1
            else:
                in_a_row = [0,0]
            if [d for d in in_a_row if d == 4]:
                return [k for k in range(0,2) if in_a_row[k] == 4][0]+1
    # left bottom to right top
    for s in range(-2, 3):
        in_a_row = [0,0]
        for a in range(0,6):
            if s+a < 0 or s+a >= 7:
                continue
            if board[5-a][s+a] != 0:
                in_a_row[board[5-a][s+a]-1] += 1
            else:
                in_a_row = [0,0]
            if [d for d in in_a_row if d == 4]:
                return [k for k in range(0,2) if in_a_row[k] == 4][0]+1
    # right bottom to left top
    for s in range(3, 9):
        in_a_row = [0,0]
        for a in range(0,6):
            if s+a < 0 or s+a >= 7:
                continue
            if board[5-a][s+a] != 0:
                in_a_row[board[5-a][s+a]-1] += 1
            else:
                in_a_row = [0,0]
            if [d for d in in_a_row if d == 4]:
                return [k for k in range(0,2) if in_a_row[k] == 4][0]+1
    return 0

def turn(board, position, player):
    for i in range(0,6):
        if i+1 >= 6 or board[i+1][position] != 0:
            board[i][position] = player
            return

def test():
    board = init_board()
    while player_won(board) == 0:
        turn = calculate_drop(board, 1)
    pp.pprint(board)
    #print(player_won(board))

if __name__ == "__main__":
    test()

