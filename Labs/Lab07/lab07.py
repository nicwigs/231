def squares(initial,terms):
    sum_int = 0
    for i in range(terms):
        sum_int += initial**2
        initial += 1
    return sum_int

def cubes(initial,terms):
    sum_int = 0
    for i in range(terms):
        sum_int += initial**3
        initial += 1
    return sum_int

com = ""
com = input("Enter Command (squares or cubes): ")
while com != "exit":
    if com == "squares":
        start = int(input("Start number: "))
        terms = int(input("Number of terms: "))
        ans = squares(start,terms)
        print("Sum equals: ", ans)
    elif com == "cubes":
        start = int(input("Start number: "))
        terms = int(input("Number of terms: "))
        ans = cubes(start,terms)
        print("Sum equals: ", ans)
    else:
        print("***Invalid Choice***")
    com = input("Enter Command (squares or cubes): ")
else:
    print("Program halted normally")

    
    