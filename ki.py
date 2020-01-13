# board = [zeile, spalte]




def find_drops ( board):
    result = {}
    for s in range(0,7):
        for z in range(0,6):
            if board [z][s] != 0:
                result[s] = z -1
                break
            elif z == 5:
                result[s] = z
                break
    return result
#
# 5 moegliche dimensionen auf leerfelder prüfen
# 
def rate_drop (board,  spalte, zeile ):
    rating = 0
    oben = False
    links = False
    rechts = False
    # oben
    if zeile == 0:
        oben = True
    # links   
    if spalte == 0:
        links = True
    # rechts   
    if spalte == 6:
        rechts = True
    if oben and board[zeile][spalte] != 0:
        return 0
    for case in range(0,4):
        if case == 0 and not links and board [zeile][spalte-1] == 0 :
            rating = rating +1;
        if case == 1 and  not links and not oben and board [zeile -1][spalte-1] == 0 :
            rating = rating +1;
        if case == 2 and  not oben and board [zeile -1][spalte] == 0 :
            rating = rating +1;
        if case == 3 and not rechts and not oben and board [zeile -1][spalte +1] == 0 :
            rating = rating +1;
        if case == 4 and not rechts and board [zeile + 1][spalte + 1 ] == 0 :
            rating = rating +1;
  
    return rating 

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def calculate_drop ( board , myid):
    possible_drops = find_drops( board)
    myrates = {}
    # calculate rates
    for key, element in possible_drops.items():
         myrates[key] = rate_drop (board , key, element)
    print(myrates.values())
    #  find best for us

    return keywithmaxval(myrates)
