# board = [zeile, spalte]




def find_drops ( board):
    result = {}
    for z in range(0,7):
        for s in range(0,6):
            if board [z,s] != 0:
                result[z] = s -1 
    return result

 def calculate_drop ( board , myid):
    possible_drops = find_drops( board)

    return drop
