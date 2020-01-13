# board = [zeile, spalte]




def find_drops ( board):
    result = {}
    for z in range(0,7):
        for s in range(0,6):
            if board [z,s] != 0:
                result[z] = s -1 
    return result
#
# 5 moegliche dimensionen auf leerfelder prüfen
# 
def rate_drop_by_empty (board,  zeile, spalte )
   rating = 0
   # oben
   if zeile == 0:
       oben = True
   # links   
   if spalte == 0:
        links = True
   # rechts   
   if spalte == 7:
        rechts = True
   for case in range(0,4):
       if case == 0 and not links and board [zeile, spalte-1] == 0 :
           rating = rating +1;
       if case == 1 and  not links and not oben and board [zeile -1, spalte-1] == 0 :
           rating = rating +1;
       if case == 2 and  not oben and board [zeile -1, spalte] == 0 :
           rating = rating +1;
       if case == 3 and not rechts and not oben and board [zeile -1 , spalte +1] == 0 :
           rating = rating +1;
        if case == 4 and not rechts and board [zeile + 1 , spalte + 1 ] == 0 :
           rating = rating +1;
  
   return rating 

#
# 5 moegliche dimensionen auf neighbour prüfen
# 
def rate_drop_by_neighbour (board,  zeile, spalte , myid )
   rating = 0
   otherrating = 0
   # oben
   if zeile == 0:
       oben = True
   # links   
   if spalte == 0:
        links = True
   # rechts   
   if spalte == 7:
        rechts = True
   for case in range(0,4):
       if case == 0 and not links 
            if board [zeile, spalte-1] == myid :
                rating = rating +1
            else if board [zeile, spalte-1] != 0 :
                otherrating = otherrating +1
       if case == 1 and  not links and not oben 
            if board [zeile -1, spalte-1] == myid :
                    rating = rating +1;
            else if board [zeile -1, spalte-1] != 0 :
              otherrating = otherrating +1
       if case == 2 and  not oben and 
            if board [zeile -1, spalte] == myid :
                rating = rating +1;
            else if board [zeile -1, spalte] != 0 :
                      otherrating = otherrating +1
       if case == 3 and not rechts and not oben and 
            if board [zeile -1 , spalte +1] == myid :
                rating = rating +1;
            else if board [zeile -1 , spalte +1] != 0 :
                      otherrating = otherrating +1
        if case == 4 and not rechts and 
            if board [zeile + 1 , spalte + 1 ] == myid :
                rating = rating +1;
            else if board [zeile + 1 , spalte + 1 ] != 0 :
                       otherrating = otherrating +1
   return rating + otherrating  

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
         myrates[key] = rate_drop_by_empty (board , key, element) +  rate_drop_by_neighbour(board , key, element, myid)
    #  find best for us

    return keywithmaxval(myrates)
