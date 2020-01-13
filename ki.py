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
def rate_drop (board,  zeile, spalte )
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


 def calculate_drop ( board , myid):
    possible_drops = find_drops( board)
    myrates = {}
    # calculate rates
    for key, element in possible_drops.items():
         myrates[key] = rate_drop (board , key, element, myid)
    #  find best for us
         
    return drop
