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

command = input("Enter a command ('h' for menu; 'q' to quit): ")

while command != "q":                             #if not quit
    if command == "l":                            #Load command
        loaded = input("Enter string to load: ")
        before = ""
        if loaded.find(" ") == -1:                #is only one word?
            current = loaded                          #if yes- set word to current
            last = ""                                 #and last to empty
        else:                                     #if multiple words
            current = loaded[:loaded.find(" ")]      #current gets first word
            last = loaded[loaded.find(" ") + 1:]     #last gets the rest
        print("[{}] [{}] [{}]".format(before, current, last))
     
    elif command == "h":                          #menu print
        print(MENU)
        
    elif command == "n":                          #Next command
        if current != "":                         #only do if current not empty
            if before == "":                          #is before nothing
                before = current                      #if yes - no space needed
            else:                                 
                before = before + " " + current       #before has something, need " "
        if last == "":                            #is last empty?
            current = ""                              #if yes - make current empty
        elif last.find(" ") == -1:                #is last one word?
            current = last                            #if yes - make current = last, 
            last = ""                                 #and last empty
        else:                                     #is last multiple words?
            current = last[0:last.find(" ")]          #if yes section using spaces
            last = last[last.find(" ") + 1:]          #note:not grabbing space
        print("[{}] [{}] [{}]".format(before, current, last))
        
    elif command == "p":                           #Previous command
        if current != "":                          #only do if current not empty
            if last == "":                         #is last nothing
                last = current                         #if yes - no space needed
            else:                                 
                last = current + " " + last            #last has something, need " "
        if before == "":                           #is before empty?
            current = ""                               #if yes - make current empty
        elif before.rfind(" ") == -1:              #is before one word?
            current = before                           #if yes - make current = before,
            before = ""                                #and make before empty
        else:                                      #is before multiple words?
            current = before[before.rfind(" ")+1:]     #if yes section using spaces
            before = before[:before.rfind(" ")]
        print("[{}] [{}] [{}]".format(before, current, last)) 
        
    elif command == "i":                            #insert command
        insert = input("Input your word to insert: ") 
        if before == "":                            #if before is empty
            before = insert                         #no space needed
        else:                                          
            before = before + " " + insert          #need space if before not empty
        print("[{}] [{}] [{}]".format(before, current, last))
        
    elif command == "r":                             #replace command
        replace = input("Input your word to replace current word: ")
        current = replace
        print("[{}] [{}] [{}]".format(before, current, last))

    elif command == "e":        
        if last != "":                             #is last empty?           
           if last.find(" ") == -1:                #if not - is last one word?
               current = last                            #if yes - make current = last, 
               last = ""                                 #and last empty
           else:                                    #if not - is last multiple words?
               current = last[0:last.find(" ")]          #if yes section using spaces
               last = last[last.find(" ") + 1:]          #note:not grabbing space
        elif before != "":                          #is before empty
           if before.rfind(" ") == -1:              #if not - is before one word?
               current = before                           #if yes - make current = before,
               before = ""                                #and make before empty
           else:                                      #if not - is before multiple words?
               current = before[before.rfind(" ")+1:]     #if yes section using spaces
               before = before[:before.rfind(" ")] 
        else:                                         #if both last and before are empty
            current = ""                              #just erase current
        print("[{}] [{}] [{}]".format(before, current, last))
      
    elif command == "c":
        cut = current                              #save current - then do erase code
        if last != "":                             #is last empty?           
           if last.find(" ") == -1:                #if not - is last one word?
               current = last                            #if yes - make current = last, 
               last = ""                                 #and last empty
           else:                                    #if not - is last multiple words?
               current = last[0:last.find(" ")]          #if yes section using spaces
               last = last[last.find(" ") + 1:]          #note:not grabbing space
        elif before != "":                          #is before empty
           if before.rfind(" ") == -1:              #if not - is before one word?
               current = before                           #if yes - make current = before,
               before = ""                                #and make before empty
           else:                                      #if not - is before multiple words?
               current = before[before.rfind(" ")+1:]     #if yes section using spaces
               before = before[:before.rfind(" ")] 
        else:                                         #if both last and before are empty
            current = ""                              #just erase current
        print("[{}] [{}] [{}]".format(before, current, last))
    
    elif command == "v":                          
        if before == "":                            #if before is empty
            before = cut                         #no space needed
        else:                                          
            before = before + " " + cut         #need space if before not empty
        cut = ""
        print("[{}] [{}] [{}]".format(before, current, last))
    else:
        print("invalid input")
    
    command = input("Enter a command ('h' for menu; 'q' to quit): ")