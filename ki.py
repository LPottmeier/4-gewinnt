# board = [zeile, spalte]




def find_drops ( board):
    result = {}
    for s in range(0,7):
        for z in range(0,6):
            if z<5 and board[z][s] == 0 and board[z+1][s] != 0:
                result[s] = z
                break
            elif z == 5 and board[z][s] == 0:
                result[s] = z
                break
    #        if board [z][s] != 0 and z > 0:
    #            result[s] = z -1
    #            break
    #        elif z == 5:
    #            result[s] = z
    #            break
    print("possible drops: "+str(result))
    return result
#
# 5 moegliche dimensionen auf leerfelder prüfen
# 

def rate_drop (board,  spalte, zeile ):
    #print("Rate drop: ["+str(zeile)+","+str(spalte)+"]")
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
        print(" -> 0")
        return 0
    for case in range(0,4):
        if case == 0 and not links and board [zeile][spalte-1] == 0 :
            rating = rating +1
        if case == 1 and  not links and not oben and board [zeile -1][spalte-1] == 0 :
            rating = rating +1
        if case == 2 and  not oben and board [zeile -1][spalte] == 0 :
            rating = rating +1
        if case == 3 and not rechts and not oben and board [zeile -1][spalte +1] == 0 :
            rating = rating +1
        if case == 4 and not rechts and board [zeile][spalte + 1 ] == 0 :
            rating = rating +1;

  
    #print(" -> "+str(rating))
    return rating 


def rate_neighbour (board,  spalte, zeile, myid ):
   rating = 0
   oben = False
   links = False
   rechts = False
   unten = False
   # oben
   if zeile == 0:
       oben = True
    # unten
   if zeile == 5:
       unten = True
   # links   
   if spalte == 0:
        links = True
   # rechts   
   if spalte == 6:
        rechts = True
   for case in range(0,6):
       if case == 0 and not links and board [zeile][spalte-1] == myid :
           rating = rating +1
       if case == 1 and  not links and not oben and board [zeile -1][spalte-1] == myid :
           rating = rating +1
       if case == 2 and  not oben and board [zeile -1][spalte]  == myid :
           rating = rating +1
       if case == 3 and not rechts and not oben and board [zeile -1][spalte +1] == myid :
           rating = rating +1
       if case == 4 and not rechts and board [zeile ][spalte + 1 ]  == myid :
           rating = rating +1
       if case == 5 and not unten and not rechts and board [zeile - 1][spalte + 1 ]  == myid:
           rating = rating +1
       if case == 6 and not unten and board [zeile - 1][spalte  ]  == myid :
           rating = rating +1
       if case == 7 and not unten and not links and board [zeile - 1 ][spalte - 1 ]  == myid :
           rating = rating +1
  
  
   return rating 

def rate_enemy (board,  spalte, zeile, myid ):
   rating = 0
   oben = False
   links = False
   rechts = False
   unten = False
   # oben
   if zeile == 0:
       oben = True
    # unten
   if zeile == 5:
       unten = True
   # links   
   if spalte == 0:
        links = True
   # rechts   
   if spalte == 6:
        rechts = True
   for case in range(0,6):
       if case == 0 and not links and board [zeile][spalte-1] != myid :
           rating = rating +1
       if case == 1 and  not links and not oben and board [zeile -1][spalte-1] != myid :
           rating = rating +1
       if case == 2 and  not oben and board [zeile -1][spalte]  != myid :
           rating = rating +1
       if case == 3 and not rechts and not oben and board [zeile -1][spalte +1] != myid :
           rating = rating +1
       if case == 4 and not rechts and board [zeile ][spalte + 1 ]  != myid :
           rating = rating +1
       if case == 5 and not unten and not rechts and board [zeile - 1][spalte + 1 ]  != myid:
           rating = rating +1
       if case == 6 and not unten and board [zeile - 1][spalte  ]  != myid :
           rating = rating +1
       if case == 7 and not unten and not links and board [zeile - 1 ][spalte - 1 ]  != myid :
           rating = rating +1
  
  
   return rating 



def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))] if len(v)!= 0 else None

def calculate_drop ( board , myid):
    possible_drops = find_drops( board)
    myrates = {}
    neighbour_rates = {}
    enemy_rates = {}
    result = {}
    # calculate rates
    for key, element in possible_drops.items():

        
         myrates[key] = rate_drop (board , key, element) 
         neighbour_rates[key] = rate_neighbour(board , key, element, myid)  
         enemy_rates[key] = rate_enemy(board , key, element, myid)  
         result[key] =  myrates[key] +   neighbour_rates[key] +   enemy_rates[key]
    #print(myrates.values())
    #print(neighbour_rates.values())
    
    print(result.values())
    
    #  find best for us
    spalte = keywithmaxval(result)
    zeile = possible_drops[spalte]

    return zeile * 7 + spalte
