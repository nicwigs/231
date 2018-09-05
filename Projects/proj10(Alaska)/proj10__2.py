
import cards   # This line is required
#--------------------------------------------------------------------------
RULES = '''
Alaska Card Game:
     Foundation: Columns are numbered 1, 2, 3, 4
                 Built up by rank and by suit from Ace to King.
                 The top card may be moved.
     Tableau: Columns are numbered 1,2,3,4,5,6,7
              Built up or down by rank and by suit.
              The top card may be moved.
              Complete or partial face-up piles may be moved.
              An empty spot may be filled with a King or a pile starting with a King.
     To win, all cards must be in the Foundation.'''

MENU = '''
Input options:
    F x y : Move card from Tableau column x to Foundation y.
    T x y c: Move pile of length c >= 1 from Tableau column x to Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game
'''
#---------------------------------------------------------------------------
def valid_move(c1,c2):
    '''return True if suits are the same and ranks differ by 1; 
    c1 & c2 are cards.'''
    move = False #boolean, True if valid move
    move = c1.suit() == c2.suit() and abs(c1.rank()-c2.rank()) == 1
    if not move:
        if c1.suit() != c2.suit():
            print("Error: Invalid move: Wrong suits")
        else:
            print("Error: Invalid move: Rank {} & {} not 1 away"\
            .format(c1.rank(),c2.rank()))
    return move
#--------------------------------------------------------------------------
def check_flip(tableau,x):
    """
    Given the tableau and the column the card was removed from, it checks
    to make sure the last card in the column is face up
    """
    if len(tableau[x-1]):        
        if not tableau[x-1][-1].is_face_up():
            tableau[x-1][-1].flip_card()
#---------------------------------------------------------------------------
def valid_tableau(tableau,x,y,c):
    check = False                       #initalize bool
    index = len(tableau[x-1])-c
    #before setting the card in col adding to make sure not empty
    if len(tableau[y-1]) == 0: 
        c1 = []
    else:
        c1 = tableau[y-1][-1]
    #in error checking, already made sure there is a card to take    
    c2 = tableau[x-1][index]
    
    if not c1:
        if c2.rank() == 13:
            check = True
    else:        
        check = valid_move(c1,c2)
    return check
#------------------------------------------------------------------------
def valid_foundation(tableau,foundation,x,y):
    check = False
    c1 = foundation[y-1][-1]
    c2 = tableau[x-1][-1]
    if c1 == "":
        if c2.rank() == 1:            
            check = True
        else:
            print("Error: Invalid move: empty foundation only accepts aces")
    else:
        check = valid_move(c1,c2)
    return check
#-------------------------------------------------------------------------
def tableau_move(tableau,x,y,c):
    '''Move pile of length c >= 1 from Tableau column x to Tableau column y.'''    
       
    if valid_tableau(tableau,x,y,c):
        tableau[y-1].extend(tableau[x-1][len(tableau[x-1])-c:])
        for i in range(c):
            tableau[x-1].pop()  
            
    check_flip(tableau,x)
#--------------------------------------------------------------------------
def foundation_move(tableau,foundation,x,y):
    '''Move card from Tableau x to Foundation y.
       Return True if successful'''    
        
    if valid_foundation(tableau,foundation,x,y):
        foundation[y-1].append(tableau[x-1].pop())
        
    check_flip(tableau,x)
        
#-----------------------------------------------------------------------------
def win(tableau,foundation):
    '''Return True if the game is won. Detects by making sure each foundation
    pile has a king'''
    if foundation[0][-1] == "" or foundation[1][-1] == "" or \
    foundation[2][-1] == "" or foundation[3][-1] == "":
        return False
    else:        
        return foundation[0][-1].rank() ==  foundation[1][-1].rank() == \
        foundation[2][-1].rank() == foundation[3][-1].rank() == 13
#-----------------------------------------------------------------------------   
def init_game():
    '''Initialize and return the tableau, and foundation.
       - foundation is a list of 4 empty lists
       - tableau is a list of 7 lists
       - deck is shuffled and then all cards dealt to the tableau'''
    foundation = [[""],[""],[""],[""]]
    tableau = [[],[],[],[],[],[],[]]
    
    deck = cards.Deck()
    deck.shuffle()
    
    tableau[0] = [deck.deal()]              #column 0
    for c in range(1,7):                    #column 1-6
        for r in range(c+5):                #column 1 = 6 cards,2 = 7
            tableau[c].append(deck.deal())  #add to right column
    
    for col in range(1,7):                  #hides cards, flips back over
        for i in range(len(tableau[col])-5):
            tableau[col][i].flip_card()            
    
    return tableau, foundation
#----------------------------------------------------------------------------    
def display_game(tableau,foundation):    
    '''Display foundation with tableau below.
       Format as described in specifications.'''

    print("="*40)
    print("{:>5s}{:>5s}{:>5s}{:>5s}".format(str(foundation[0][-1]),\
    str(foundation[1][-1]), str(foundation[2][-1]),str(foundation[3][-1])))
    print("-"*40)
   
    maxx = 0                    #find the largest column
    for col in tableau:
        if len(col) > maxx:
            maxx = len(col)   
    
    for c in range(maxx): 
        print_lst = []
        for i in range(7):
            try: #try appending works if col len >= c
                print_lst.append(str(tableau[i][c]))
            except IndexError: #if column not longest, add blank space
                print_lst.append("  ")
        print("{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}".format\
        (print_lst[0],print_lst[1],print_lst[2],print_lst[3],print_lst[4]\
        ,print_lst[5],print_lst[6]))  
#---------------------------------------------------------------------
def start():
    print(RULES)      
    tableau,foundation = init_game()
    display_game(tableau, foundation)
    print(MENU)
    return tableau,foundation
#-----------------------------------------------------------------------
def e1(choice,NUM):
    if len(choice) != NUM:          
        print("Incorrect number of arguments")
        return False
    return True
#---------------------------------------------------------------------------
def e2(choice,TUP):
    for i in range(1,len(choice)):              #are all ints?
        try:
            choice[i] = int(choice[i])
        except ValueError:
            print("Incorrect type of arguments, {} must be type int"\
            .format(TUP[i]))
            return False
    return True
#---------------------------------------------------------------------------
def e3(num,TUP):
    if not 0 < num < 8:             #check if possible tableau column
        print("Value out of range: {} must be between 1 -> 7 inclusive"\
        .format(TUP[1]))
        return False
    return True
#-----------------------------------------------------------------------
def e4(choice,TUP):        
    if not 0 < choice[2] < 5:             #check if possible foundation column
        print("Value out of range: {} must be between 1 -> 4 inclusive"\
        .format(TUP[2]))
        return False
    return True
#--------------------------------------------------------------------------- 
def e5(choice,TUP,tableau):
    if choice[3] < 1:                   #check if possible card number
            print("Value out of range: {} must be positive"\
            .format(TUP[3]))
            return False
            
    count = 0
    for card in tableau[choice[1]-1]:
        if card.is_face_up():
            count +=1
            
    if choice[3] > count:
        print("Value out of range:{} selected was {}..."\
        .format(TUP[3],choice[3]))
        print("                   {} is only {}".format(TUP[3],count))
        return False
        
    return True
#---------------------------------------------------------------------------
def e6(choice,TUP,tableau):
    if not tableau[choice[1]-1]:
        print("Value out of range:{} {} was selected for a card but its empty"\
        .format(TUP[1],choice[1]))
        return False
    return True
#---------------------------------------------------------------------------              
def error_check(choice,tableau):
    if choice[0].upper() == "F":
        TUP = (3,"Tableau column 'x'","Foundation column 'y'")
    else:
        TUP = (4,"Tableau column 'x'","Tableau column 'y'","Number of cards 'c'")
    """
    For readability error functions were not given descriptive names:
    e1: Checks number of arguments
    e2: Checks type of arguments
    e3: Checks that the tableau column number is within range 1-7
    e4: Checks that the foundation column number is within range 1-4
    e5: Checks that the number of cards wished to move is at least 1 and less
        than or eqaul to the amount of flipped up cards in the take column
    e6:Checks that the take column for the foundation has at least one card
       to remove.
      c1-6 corespond to the errors,False if error occurs
    """    
    c1 = c2= c3 = c4 = c5 = c6 = True 
    
    c1= e1(choice,TUP[0])                          #argument count
    if c1:        
        c2 = e2(choice,TUP)                        #agrument type
        if c2:                    
            c3 = e3(choice[1],TUP)                 #tab. take column in range
            if c3:             
                if TUP[0] == 3:                    #foundation only
                    c4 = e4(choice,TUP)            #foundation column in range    
                    c6 = e6(choice,TUP,tableau)    #check take column             
                if TUP[0] == 4:                    #Tableau only
                    c3 = e3(choice[2],TUP)         #tab. place column in range
                    c5 = e5(choice,TUP,tableau)    #check card number
            
    return c1 and c2 and c3 and c4 and c6 and c5      
#--------------------------------------------------------------------------
def main(): 
    
    tableau,foundation = start()
    choice = input("Enter a choice: ").split()
    
    while choice[0].lower() != 'q':  #fix when push enter
    
        if choice[0].upper() == "F":
            if error_check(choice,tableau):
                foundation_move(tableau,foundation,choice[1],choice[2])
                
        elif choice[0].upper() == "T":
            if error_check(choice,tableau):
                tableau_move(tableau,choice[1],choice[2],choice[3])     
                
        elif choice[0].upper() == "R":
            tableau,foundation = start()
            
        elif choice[0].upper() == "H":
            print(MENU)
            
        else:
            print("Incorrect Command")
        if win(tableau,foundation):
            print("You won!")
            break
        else:
            display_game(tableau, foundation)
            choice = input("Enter a choice: ").split()
#------------------------------------------------------------------------
main()
