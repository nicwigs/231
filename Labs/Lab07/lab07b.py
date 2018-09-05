def squares():
    sum_int = 0
    initial = int(input("Start number: "))
    terms = int(input("Number of terms: "))        
    for i in range(terms):
        sum_int += initial**2
        initial += 1
    print("Sum equals: ", sum_int)  

def cubes(initial,terms):
    sum_int = 0
    initial = int(input("Start number: "))
    terms = int(input("Number of terms: "))                
    for i in range(terms):
        sum_int += initial**3
        initial += 1
    print("Sum equals: ", sum_int)
#--------------------------------------------------------------
com = ""
com = input("Enter Command (squares or cubes): ")
while com != "exit":
    if com == "squares":
        squares()
    elif com == "cubes":
        cubes()
    else:
        print("***Invalid Choice***")
    com = input("Enter Command (squares or cubes): ")
else:
    print("Program halted normally")

    
    