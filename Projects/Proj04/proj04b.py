##################################################
#Computer Project 04 - string/text manipulation
#Print menu and ask for inital input
#While loop, while the input is not equal to quit
#  if loading
#    ask for string
#    take first word, put it in current, take the rest into Last
#    print
#  if menu
#    print
#  if next
#    put current into before
#    take first word in last, put it in current, take the rest into Last
#    print
#  if previous
#    put current into last
#    take last word in before, put as current
#    put the rest in before
#    print
#  if insert
#    ask for inserted word
#    add to before
#    print
#  if replace
#    ask for replace word
#    set current to replace
#    print
#  if erase
#    erase current
#    replace current with either last or before
#    print
#  if cut
#    save current
#    replace current baised of erase function
#    print
#  if paste
#    add cut word to before
#    print
#############################################################################
MENU = '''
--------------------------------------
Commands available:
    'n': Move to Next word
    'p': Move to Previous word
    'i': Insert a word
    'e': Erase current word
    'r': Replace current word
    'c': Cut word, move to copy buffer
    'v': Paste word from copy buffer to before current word
    'l': Load a string
--------------------------------------
'''
loaded = ""
before = ""
current = ""
last = ""
command = ""
insert = ""
replace = ""
cut = ""
#Note: all of the variables are string
print(MENU)
command= input("Enter a command ('h' for menu; 'q' to quit): ").lower()

while command != "q":                               #if not quit
#---------------------------------------------------------------------------                           
    if command == "l":                              #Load command
        loaded = input("Enter string to load: ")
        before = ""
        if not loaded.find(" ") +1:              #is only one word?
            current = loaded                      #if yes- set word to current
            last = ""                             #and last to empty
        else:                                     #if multiple words
            current = loaded[:loaded.find(" ")]   #current gets first word
            last = loaded[loaded.find(" ") + 1:]  #last gets the rest
        print("[{}] [{}] [{}]".format(before, current, last))
#---------------------------------------------------------------------------   
    elif command == "h":                       #menu print
        print(MENU)
        print("[{}] [{}] [{}]".format(before, current, last))
#---------------------------------------------------------------------------        
    elif command == "n":                       #Next command
        if current:                            #only do if current not empty
            if not before:                     #is before nothing
                before = current               #if yes - no space needed
            else:                                 
                before = before + " " + current#before has something, need " "        
        if not last.find(" ")+1:               #is last one word or empty?
            current = last                     #if yes - make current = last, 
            last = ""                          #and last empty
        else:                                  #is last multiple words?
            current = last[0:last.find(" ")]   #if yes section using spaces
            last = last[last.find(" ") + 1:]   #note:not grabbing space
        print("[{}] [{}] [{}]".format(before, current, last))
#---------------------------------------------------------------------------       
    elif command == "p":                      #Previous command
        if current:                           #only do if current not empty
            if not last:                      #is last nothing
                last = current                #if yes - no space needed
            else:                                 
                last = current + " " + last   #last has something, need " "        
        if not before.rfind(" ")+1:           #is before one word or empty?
            current = before                  #if yes - make current = before,
            before = ""                       #and make before empty
        else:                                 #is before multiple words?
            current = before[before.rfind(" ")+1:]#if yes section using spaces
            before = before[:before.rfind(" ")]
        print("[{}] [{}] [{}]".format(before, current, last)) 
#---------------------------------------------------------------------------         
    elif command == "i":                      #insert command
        insert = input("Input your word to insert: ") 
        if not before:                        #if before is empty
            before = insert                   #no space needed
        else:                                          
            before = before + " " + insert   #need space if before not empty
        print("[{}] [{}] [{}]".format(before, current, last))
#---------------------------------------------------------------------------         
    elif command == "r":                              #replace command
        replace = input("Input your word to replace current word: ")
        current = replace
        print("[{}] [{}] [{}]".format(before, current, last))
#--------------------------------------------------------------------------- 
    elif command == "e":        
        if current:                           #Dont erase if there is nothing
            if last:                          #is last empty?           
               if not last.find(" ")+1:       #if not - is last one word?
                   current = last             #if yes - make current = last, 
                   last = ""                  #and last empty
               else:                         #if not - is last multiple words?
                   current = last[0:last.find(" ")]#if yes section using spaces
                   last = last[last.find(" ") + 1:]#note:not grabbing space
            elif before:                            #is before empty?
                if not before.rfind(" ")+1:     #if not - is before one word?
                   current = before           #if yes - make current = before,
                   before = ""                #and make before empty
                else:                      #if not - is before multiple words?
                   current = before[before.rfind(" ")+1:]#if yes section //
                   before = before[:before.rfind(" ")]   #Using Spaces
            else:                          #if both last and before are empty
                current = ""                             #just erase current
        print("[{}] [{}] [{}]".format(before, current, last))
#---------------------------------------------------------------------------       
    elif command == "c":                   #Dont cut if there is nothing
        cut = current                      #save current - then do erase code
        if current:        
            if last:                              #is last empty?           
               if not last.find(" ")+1:           #if not - is last one word?
                   current = last               #if yes - make current = last, 
                   last = ""                      #and last empty
               else:                        #if not - is last multiple words?
                   current = last[0:last.find(" ")]#if yes section using spaces
                   last = last[last.find(" ") + 1:] #note:not grabbing space
            elif before:                           #is before empty?
                if not before.rfind(" ")+1:   #if not - is before one word?
                   current = before          #if yes - make current = before,
                   before = ""               #and make before empty
                else:                      #if not - is before multiple words?
                   current = before[before.rfind(" ")+1:]#if yes section//
                   before = before[:before.rfind(" ")]   #using spaces
            else:                           #if both last and before are empty
                current = ""                #just erase current
        print("[{}] [{}] [{}]".format(before, current, last))
#---------------------------------------------------------------------------     
    elif command == "v":                          
        if cut:                       #make sure not trying to paste nothing
            if not before:            #if before is empty
                before = cut          #no space needed
            else:                                          
                before = before + " " + cut    #need space if before not empty
        cut = ""
        print("[{}] [{}] [{}]".format(before, current, last))
#---------------------------------------------------------------------------    
    else:
        print("invalid input")
    
    command = input("Enter a command ('h' for menu; 'q' to quit): ").lower()
