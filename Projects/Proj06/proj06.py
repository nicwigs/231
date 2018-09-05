def rotate(s):
    """
    Parameter s: string to rotate
    return: new string by rotating string one char to right
    """
    s = s[-1] + s[:-1]       #take last char, add to front
    return s
#--------------------------------------------------------------------------
def is_transpose(s1, s2):
    """
    Parameters s1, s2: two strings to check if transposable
    continually rotates string s1 by calling rotate()
    return: True if s1 is ever equal to s2, False otherwise
    """  
    #NOTE: all variable are STRINGS
    
    rot = ""               #string that goes through rotations of s1
    rot = rotate(s1)       #set rot string to the first rotate of s1
    while rot != s1:       #Loops only once entirely through s1    
        if rot == s2:      #if strings are equal: break           
            break   
        rot = rotate(rot)  #update s1 by another rotation
    else:                  #if gets through all possibilites but none equal
        return False       #then return false
    return True            #if equal - true. This is from the break statement
#---------------------------------------------------------------------------
def get_transposability_zero(num):
    """
    Parameter num: number to see if any multiples are transposible
    prepends a leading zero to number
    checks if number is transposable by multiplying by 2->9 by 
    calling is_transpose()
    if number is transposable, print number, multiplier & multiple 
    return: None
    """
    #NOTE: Unless specified ALL variables are INTS
    lier = 0                                  #multiplier
    ple = 0                                   #multiple
    num_str = ""                              #STRING of number        
    
    for lier in range(2,10):                  #range of multipliers
        ple = lier * num                      #multiply num by multiplier
        num_str = str(num)                    #convert num to string          
        num_str = "0" + num_str               #append 0 to beginning          
        if is_transpose(num_str,str(ple)):
            print("{:>10s} {} {} {} {:<10d}".\
            format(num_str,"*",lier,"=",ple)) #if yes - print
#--------------------------------------------------------------------------
def get_transposability(num):
    """
    Parameter num: number to see if any multiples are transposible
    checks if number is transposable by multiplying by 2->9 by 
    calling is_transpose()
    if number is transposable, print number, multiplier & multiple 
    return: None
    """
    #NOTE: ALL variables are INTS
    lier = 0                                 #multiplier
    ple = 0                                  #multiple
    
    for lier in range(2,10):                 #range of multipliers
        ple = lier * num                     #multiply num by multiplier        
        if is_transpose(str(num),str(ple)): #if num & multiple are transposible
            print("{:10d} {} {} {} {:<10d}".\
            format(num,"*",lier,"=",ple))     #if yes - print
#--------------------------------------------------------------------------
def open_file():
    """
    prompt the user for the name of the input file
    If unable to open that file, prompts again.
    return: file object
    """
    file_str = ""                                 #inputed file name
    while True:
        file_str = input("Enter a file name:  ")  #ask for file name
        try:
            fp = open(file_str)     #set file pointer
            break                   #if file found, leave loop
        except FileNotFoundError:   #if file not found, loop again, re-asking
            print("Unable to Open File")
    return fp
#--------------------------------------------------------------------------
def process_file(): 
    """
    calls open file
    extracts start and end values from file
    calls get_transposability and get_transposability_zero for all values 
    from start to end  
    return: None
    """
    start = 0  #range start value recieved from file
    end = 0    #range end value recieved from file    
 
    fdata = open_file()                       #get file pointer from open_file
    fdata.readline()                          #read header file
    for line in fdata:
        start = int(line[:line.find(" ")].strip())    #store start value
        end = int(line[line.find(" "):].strip())      #store end value
        
    print("\n Transposed numbers from",start,"to",end,"\n")  #format 
    
    for i in range(start,end+1):     #through given range(Inclusive via Piazza)                      
            get_transposability_zero(i)        
            get_transposability(i) 
#-------------------------------------------------------------------------
##############################################################
#Computer Project 06 - Integer Transposabilty checker
#Given a file with a range of integers the program will check for each number
    #in the range if that number and one of its multiples (2 through 9) are
    #in fact transposible. If they are transposible, the program will print
    #the number, multiplier, and multiple
#the program body following calls process_file() which calls other functions 
    #via the code,and explict descriptions can be found on each 
    #function header description
#########################################################################
process_file()   #Run the program