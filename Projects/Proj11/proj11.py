import turtle
import time
import math
import random


def drawShape(shape,side):
    """
    Parameters: shape value and side length
    Sets up turtle with random colors
    draws correct shape according to the shape number
    """
    #Setting turtle up
    (r,g,b) = (random.random(), random.random(), random.random())
    turtle.pencolor(r,g,b)
    turtle.fillcolor(r,g,b)
    turtle.begin_fill()

    #Start drawing    
    turtle.down()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)

    if shape == 1: #straight line
        turtle.left(135)
        turtle.forward(math.sqrt(2*side*side))
        
    elif shape == 2: #steps
        turtle.left(90)
        for i in range(1,3):
            #Alternate between vertical and horizontal lines
            turtle.forward(side/2) #horizontal
            turtle.left(90)
            turtle.forward(side/2) #vertical
            turtle.right(90)
        
    elif shape == 3: #unbroken step
        turtle.left(90)
        turtle.forward(side/4)
        turtle.left(45)
        #Calculate length of hypotenuse
        turtle.forward(math.sqrt(9*side*side/8))
        turtle.left(45)
        turtle.forward(side/4)
        
    elif shape == 4: #convex quartercircle
        turtle.left(90)
        turtle.circle(side,90)
    
    elif shape == 5: #concave quartercircle
        turtle.left(180)
        #Negative radius changes turtle direction
        turtle.circle(-side,90)
        
    #******************CODE MODIFICATIONS START HERE**************************
    
    elif shape == 6: #inflection point
        turtle.left(90)                 #start in direction of top
        turtle.circle(side/2,90)        #start circle
        turtle.circle(-side/2,90)       #flip concavity
    
    elif shape == 7:  #Glory to God
        turtle.left(90)                 #top
        turtle.forward(side)
        
        turtle.left(90)                 #left outer block
        turtle.forward(side/4)
        
        for i in range (1,3):           #left side top of cross
            turtle.left(90)
            turtle.forward(side/4)
        for i in range (1,3):           #right top of cross
            turtle.right(90)
            turtle.forward(side/4)
        
        turtle.left(90)                 #right side of cross
        turtle.forward(side/4)
        
        for i in range(1,3):            #right side bottom of cross
            turtle.right(90)
            turtle.forward(side/4)
        
        turtle.left(90)                 #right lower of cross
        turtle.forward(2*side/5)
        turtle.right(90)                #bottom of cross
        turtle.forward(side/4)
        turtle.right(90)                #left lower of cross
        turtle.forward(2*side/5)
        turtle.left(90)                 #left side bottom of cross
        turtle.forward(side/4)
        turtle.left(90)                 #left outer block back to beginning
        turtle.forward(side/2)
        
    elif shape == 8: #The mixing bowl
        turtle.left(90)                 #top of bowl stand
        turtle.forward(side)
        turtle.left(90)                 #short side down stand face
        turtle.forward(side/3)
        turtle.circle(side/3,180)       #create bowl   
        turtle.forward(-side/2)         #inside edge of bowl stand
        turtle.left(90)                 #top of base edge of stand
        turtle.forward(2*side/3)
        turtle.left(90)                 #side of base edge of stand
        turtle.forward(1*side/6)
        
    elif shape == 9: #The Boot
        turtle.left(90)                 #top
        turtle.forward(side/2)
        turtle.left(90)                 #down leg of boot
        turtle.forward(3*side/4)
        turtle.circle(-side/4,-180)     #circular toe for boot
        turtle.left(180)                #side of boot
        turtle.forward(side/4)
    
    else: # shape == 0: #Inward Jigsaw puzzle piece
        turtle.left(90)                 #Top
        turtle.forward(side)
        turtle.left(90)                 #short side
        turtle.forward(side/3)
        turtle.left(90)                 #into the piece, upper edge
        turtle.forward(side/3)
        turtle.circle(-side/6,180)      #half circle inside
        turtle.forward(side/3)          #get out of piece
        turtle.left(90)                 #other short side, connecting shape
        turtle.forward(side/3)
    
    #********************CODE MODIFICATIONS END HERE**************************
    
    turtle.end_fill()
    turtle.up()
    turtle.setpos(0,0)
    turtle.seth(0)
 #-----------------------------------------------------------------------------   
def getHash(value):
    """
    Parameters:a two character value
    hash value is the remainder of the digits added together divided by 10
    return hash corresponding to value
    """
    summ = int(value[0]) + int(value[1])    
    return summ % 10   
#-----------------------------------------------------------------------------
def drawQ1(identifier,side):
    """
    Parameters identifier and side.
    Positions turtle, calculate hash for the digits corresponding to Q1
    and Calls drawShape with hash and side
    """
    turtle.goto(-side, 0)                    #postion turtle
    drawShape(getHash(identifier[0:2]),side) #grab hash from digits 1&2 & draw
#-----------------------------------------------------------------------------
def drawQ2(identifier,side):
    """
    Parameters identifier and side.
    Positions turtle, calculate hash for the digits corresponding to Q2
    and Calls drawShape with hash and side
    """
    turtle.goto(0,-side)                     #postion turtle
    turtle.seth(90)                          #proper rotation of shape
    drawShape(getHash(identifier[2:4]),side) #grab hash from digits 3&4 & draw
#-----------------------------------------------------------------------------
def drawQ3(identifier,side):
    """
    Parameters identifier and side.
    Positions turtle, calculate hash for the digits corresponding to Q3
    and Calls drawShape with hash and side
    """
    turtle.goto(side,0)                       #postion turtle
    turtle.seth(180)                          #proper rotation of the shape
    drawShape(getHash(identifier[4:6]),side)  #grab hash from digits 5*6 & draw
#-----------------------------------------------------------------------------
def drawQ4(identifier,side):
    """
    Parameters identifier and side.
    Positions turtle, calculate hash for the digits corresponding to Q4
    and Calls drawShape with hash and side
    """
    turtle.goto(0,side)                      #postion turtle
    turtle.seth(270)                         #proper rotation of the shape
    drawShape(getHash(identifier[6:8]),side) #grab hash from digits 7&8 & draw            
#----------------------------------------------------------------------------
def getSide():    
    """
    Prompts user for side length, continues to ask until give a valid entry
    i.e and integer greater than 0
    """
    while True:    
        side=input("Please enter the total length of the figure: ")
        try: 
            if 0 >= int(side): #if negative -- error
                print("Side length must be a positive number")
            else:
                return int(side)
        except ValueError: #if cant convert to int -- error
            print("Side length must be an integer")
#----------------------------------------------------------------------------
def getID():     
    """
    Prompts user for ID
    Makes sure there is 8 characters after the first & that they are digits
    Returns the 8 digit string from inputed ID
    """
    while True:        
        identifier=\
        input("Please enter MSU ID (including the starting letter): ")
        
        if identifier[0].isalpha():    #make sure they include starting letter        
            identifier = identifier[1:]           #gets rid of starting letter
            
            if len(identifier.strip()) == 8:     #check only 8 digits
                if identifier.isnumeric():         #if all values were digits
                    return identifier            #return 8 digit string via ID
                else:
                    print("ID must have 8 digits")
            else:
                print("ID must have 9 characters,including a starting letter")
        else:
            print("ID must include the starting letter")
#----------------------------------------------------------------------------
"""
-----------Project 11 Turtle Shapes-----------
Grabs side length and ID digits, sets up turtle, calls draw functions to 
draw each quadrant, shows the image, then closes the turtle window
"""
            
side = getSide()                #grab side length
identifier = getID()            #grab ID digits

turtle.colormode(1.0)
turtle.speed(0)
                                #below draws each quadrant 
drawQ1(identifier,side/2)       
drawQ2(identifier,side/2)
drawQ3(identifier,side/2)
drawQ4(identifier,side/2)

time.sleep(20)                  #holds image
turtle.bye()                    #shut down turtle

