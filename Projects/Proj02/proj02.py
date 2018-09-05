############################################################################
#   Computer Project 2 - Turtle Drawing Shapes Using Loops - Control Ch 2    
# Alrogrithm
#  prompt for first integer
#  prompt for second integer
#  if correct input requirements
#     if second integer == 2
#       loop while first integer > 10
#           Set up random colors
#           Start filling
#           Draw figure associated with second integer
#           End fill
#           Change first integer by factor
#     if second integer == 1
#       loop while first integer > 10
#           Set up random colors
#           Start filling
#           Draw figure associated with second integer
#           End fill
#           Change first integer by factor
#    Close drawing device
#  if wrong input send error message
############################################################################
import turtle,random,time
length,shape = 0,0

length = int(input("Enter a length (greater than 10 please): "))
shape = int(input("Enter '1' for squares, '2' for circles: "))

if length > 10 and ( shape == 2 or shape == 1):
    
    if shape == 2: #Circle
        while length >= 10:
            # Set up random coloring
            (r,g,b) = (random.random(), random.random(), random.random())
            turtle.pencolor(r,g,b)
            turtle.fillcolor(r,g,b)  # turn on color filling
            turtle.begin_fill() 
                    
            turtle.circle(length)  # draw the circle
                 
            turtle.end_fill()   # complete color filling
            length -= 7   

    elif shape == 1: #Square
         while length >= 10:
             # Set up random coloring
             (r,g,b) = (random.random(), random.random(), random.random())
             turtle.pencolor(r,g,b)
             turtle.fillcolor(r,g,b)  # turn on color filling
             turtle.begin_fill() 
            
             for q in range(4):
                 turtle.forward(length)  # draw the square
                 turtle.left(90)
                            
             turtle.end_fill()   # complete color filling
             length -= 7 
    # let the figure be displayed for 5 seconds before it disappears
    time.sleep(5)
    turtle.bye()
         
elif shape != 1 and shape != 2: #if wrong shape input
    print()
    print("Error: possible options were 1 or 2, not ", shape) 
    if length <= 10:
        print("Error: length must be greater than 10, ", length, "is not greater than 10")
else: #if wrong length input
    print()    
    print("Error: length must be greater than 10, ", length, "is not greater than 10")
    

