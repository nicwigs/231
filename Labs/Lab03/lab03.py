command_str,start_int, terms_int = "",0,0

command_str = str(input("Enter 'squares', 'cubes' or 'exit':"))

while command_str != "exit":
    
    count_int = 0 #keep track of what term you are on
    sum_int = 0   
    current_int = 0
    
    if command_str == "squares":
        
        start_int = int(input("Enter inital integer for sum of squares:"))
        terms_int = int(input("Enter number of terms for sum of squares:"))
        
        current_int = start_int #intial value 
        print("Sum =", end = " ") # inital print
        
        while count_int < terms_int: #loop until number of terms is reached
           
           sum_int += current_int**2 #square
           current_int += 1 #update current int
           count_int += 1  #update count
           
           #To make output look good 
           if count_int == terms_int:
               print(current_int-1, "^2", end=" ")
           else:    
               print(current_int-1, "^2 +", end=" ")
           
        print("=", sum_int)
    #Same as above except change 'squares' to 'cubes' and 2 to 3       
    elif command_str == "cubes":
        
        start_int = int(input("Enter inital integer for sum of cubes:"))
        terms_int = int(input("Enter number of terms for sum of cubes:"))
        
        current_int = start_int #intial value
        print("Sum =", end = " ") # inital print
             
        while count_int < terms_int: #loop until number of terms is reached
           sum_int += current_int**3 #cube
           current_int += 1  #update current int
           count_int += 1   #update count
                      
           #To make output look good 
           if count_int == terms_int:
               print(current_int-1, "^3", end=" ")
           else:    
               print(current_int-1, "^3 +", end=" ")
           
        print("=", sum_int)
        
    else:
        print("***Invalid Choice***")
        
    command_str = str(input("Enter 'squares', 'cubes' or 'exit':")) #reprompt question
                
