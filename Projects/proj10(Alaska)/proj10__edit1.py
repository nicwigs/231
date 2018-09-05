
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
    """ Given the tableau and the column the card(s) was removed from, it 
    checks to make sure the last card in the column is face up"""
    
    if len(tableau[x-1]):        
        if not tableau[x-1][-1].is_face_up():
            tableau[x-1][-1].flip_card()
#---------------------------------------------------------------------------
def valid_tableau(tableau,x,y,c):
    """Given the tableau, the take column, destination column, and number of 
    cards sets the first card in the moving stack and makes sure it is a king 
    if the destination column is empty, if the destination column is not empty, 
    valid_move() is used to return wether it is valid or not
    returns if move is valid"""
    
    check = False                       #initalize bool
    index = len(tableau[x-1])-c    
    c2 = tableau[x-1][index] #error funct already made sure there is a card 
    
    if not tableau[y-1]:  #before setting the card in col, make sure not empty       
        if c2.rank() == 13: #if empty, valid if moving card is King
            check = True
    else:                 #if not special case, use general function
        c1 = tableau[y-1][-1]
        check = valid_move(c1,c2)
    return check
    """
    c2 = tableau[x-1][index] #error funct already made sure there is a card   
    
    if not c1:#empty tableau recieving col move valid if moving card is king
        if c2.rank() == 13:
            check = True
    else:                        #if not a special case,use general function
        check = valid_move(c1,c2)
    return check
    """
#------------------------------------------------------------------------
def valid_foundation(tableau,foundation,x,y):    
    """Given the tableau,foundation, and their respective columns
    Assigns the cards to compare, if the foundation column is empty, it makes
    sure the moving card is an ace. If not empty, calls valid_move to check
    Returns if the move is valid"""
    
    check = False
    c1 = foundation[y-1][-1]
    c2 = tableau[x-1][-1]
    if c1 == "":        #foundation empty move valid if moving card is ace
        if c2.rank() == 1:            
            check = True
        else:
            print("Error: Invalid move: empty foundation only accepts aces")
    else:                   #if not a special case,use general function
        check = valid_move(c1,c2)
    return check
#-------------------------------------------------------------------------
def tableau_move(tableau,x,y,c):
    '''Move pile of length c >= 1 from Tableau column x to Tableau column y.'''   
       
    if valid_tableau(tableau,x,y,c):                        #check if valid
        tableau[y-1].extend(tableau[x-1][len(tableau[x-1])-c:]) #add stack to y
        for i in range(c): #removes the moved stack from column x if valid
            tableau[x-1].pop()  
            
    check_flip(tableau,x) #checks that at least one card is face up in col x
#--------------------------------------------------------------------------
def foundation_move(tableau,foundation,x,y):
    '''Move card from Tableau x to Foundation y.'''    
        
    if valid_foundation(tableau,foundation,x,y):            #check if valid
        foundation[y-1].append(tableau[x-1].pop())          #moves card
        
    check_flip(tableau,x) #checks that at least one card is face up in col x
        
#-----------------------------------------------------------------------------
def win(tableau,foundation):
    '''Return True if the game is won. Detects by making sure each foundation
    pile has a king'''
    
    if foundation[0][-1] == "" or foundation[1][-1] == "" or \
    foundation[2][-1] == "" or foundation[3][-1] == "": 
        return False #dont check for king if any are empty
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
    
    deck = cards.Deck()                     #create deck
    deck.shuffle()
    
    tableau[0] = [deck.deal()]              #column 0
    for c in range(1,7):                    #column 1-6
        for r in range(c+5):                #column 1 = 6 cards,2 = 7
            tableau[c].append(deck.deal())  #add to correct column
    
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
   
    maxx = 0                       #find the largest column, set equal to maxx
    for col in tableau:
        if len(col) > maxx:
            maxx = len(col)   
    
    for c in range(maxx):        #go through as many times as the max col len
        print_lst = []           #list for each row that is printed
        for i in range(7):       #go through each column
            try:                 #try appending, works if col len >= c
                print_lst.append(str(tableau[i][c]))
            except IndexError:   #if column not longest, add blank space
                print_lst.append("  ")
        print("{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}".format\
        (print_lst[0],print_lst[1],print_lst[2],print_lst[3],print_lst[4]\
        ,print_lst[5],print_lst[6]))  
#---------------------------------------------------------------------
def start():
    """Runs through set up of the game """
    
    print(RULES)      
    tableau,foundation = init_game()
    display_game(tableau, foundation)
    print(MENU)
    return tableau,foundation
#-----------------------------------------------------------------------
def e1(choice,num):
    """Given their input list and the allowed number of arguments
    Checks that the right number of arguments were given for their 
    corresponding function.
    Returns False if error"""
    
    if len(choice) != num:          
        print("Incorrect number of arguments")
        return False
    return True
#---------------------------------------------------------------------------
def e2(choice,tup):
    """Given their input list and the tup,a tuple of expected info
    corresponding to the two commands (f&t)
    checks that the input contains the right type
    Returns False if error"""
    
    for i in range(1,len(choice)):              
        try:
            choice[i] = int(choice[i])          #are all ints?
        except ValueError:                      #if not int, return False
            print("Incorrect type of arguments, {} must be type int"\
            .format(tup[i]))
            return False
    return True
#---------------------------------------------------------------------------
def e3(num,tup):
    """Given the column number inputed and the tup,a tuple of expected
    info corresponding to the two commands (f&t) 
    checks to make sure the desired column is a possible column in tableau
    Return False if error"""
    
    if not 0 < num < 8:             #check if possible tableau column
        print("Value out of range: {} must be between 1 -> 7 inclusive"\
        .format(tup[1]))
        return False
    return True
#-----------------------------------------------------------------------
def e4(num,tup):     
    """Given the column number inputed and the tup,a tuple of expected
    info corresponding to the two commands (f&t) 
    Checks to make sure the desired column is a possible column in foundation
    Return False if error """
    
    if not 0 < num < 5:             #check if possible foundation column
        print("Value out of range: {} must be between 1 -> 4 inclusive"\
        .format(tup[2]))
        return False
    return True
#--------------------------------------------------------------------------- 
def e5(choice,tup,tableau):
    """Given their input list and the constant tup,a tuple of expected info
    corresponding to the two commands (f&t), and the tableau
    Checks that the card number is greater than 0 and less than or equal to
    the number of faced up cards in the column
    Returns False if error"""
    
    if choice[3] < 1:                   #check if possible card number
            print("Value out of range: {} must be positive"\
            .format(tup[3]))
            return False
            
    count = 0
    for card in tableau[choice[1]-1]:
        if card.is_face_up():        #counts number of possible cards to move
            count +=1
            
    if choice[3] > count:#desired card number greater than whats face up, error
        print("Value out of range:{} selected was {}..."\
        .format(tup[3],choice[3]))
        print("                   {} is only {}".format(tup[3],count))
        return False
        
    return True
#---------------------------------------------------------------------------
def e6(choice,tup,tableau):
    """Given their input list and the constant tup,a tuple of expected info
    corresponding to the two commands (f&t) and tableau
    checks that the input contains the right type
    Returns False if error"""    
    
    if not tableau[choice[1]-1]:
        print("Value out of range:{} {} was selected for a card but its empty"\
        .format(tup[1],choice[1]))
        return False
    return True
#---------------------------------------------------------------------------              
def error_check(choice,tableau):
    """Given their input as a list, and the tableau
    Assigns a tup that contains information about each function
    this was added to be able to overlap functions for each command
    Then calls all error functions to check for errors, will display error 
    messages
    Returns False if error"""
    
    if choice[0].upper() == "F":
        tup = (3,"Tableau column 'x'","Foundation column 'y'")
    else:
        tup = \
        (4,"Tableau column 'x'","Tableau column 'y'","Number of cards 'c'")
        
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
    
    c1= e1(choice,tup[0])                          #argument count
    if c1:        
        c2 = e2(choice,tup)                        #agrument type
        if c2:                    
            c3 = e3(choice[1],tup)                 #tab. take column in range
            if c3:             
                if tup[0] == 3:                    #foundation only
                    c4 = e4(choice[2],tup)         #foundation column in range    
                    c6 = e6(choice,tup,tableau)    #check take column             
                if tup[0] == 4:                    #Tableau only
                    c3 = e3(choice[2],tup)         #tab. place column in range
                    c5 = e5(choice,tup,tableau)    #check card number
            
    return c1 and c2 and c3 and c4 and c6 and c5      
#--------------------------------------------------------------------------
def main(): 
    """Calls all functions
    calls start to deal and grab tableau and foundation
    asks for input, error checking is called before foundation and tableau
    move is called
    loops until quit or winner"""
    
    tableau,foundation = start()
    choice = input("Enter a choice: ").split()
    
    while choice[0].lower() != 'q' :  
    
        if choice[0].upper() == "F":
            if error_check(choice,tableau):          #if not errors
                foundation_move(tableau,foundation,choice[1],choice[2])
                
        elif choice[0].upper() == "T":           
            if error_check(choice,tableau):          #if not errors
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
