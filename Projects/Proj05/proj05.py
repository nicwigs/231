#####################################################################
#Computer Project 05 - US Occupations and Salaries, Data finding
#While True
#    try-except to prompt for file and check if exists
#    if no error - break loop 
#    if error - prompt again
#prompt for keyword
#Print header
#Read data file header
#loop through each line
#    if occupation classified as detailed
#        store name of occupation
#        if keyword is in the occupation
#            try 
#                storing salary as float
#                See if salary is a min or max
#                add one to keyword count and add salary to total sum
#                print salary and occupation in their spots in table
#            except ValueError    (aka salary was a *)
#                dont add to count or salary, add to na count
#                print with * under salary column 
#if no results with valid salaries were found                     (cnt_int == 0)
#    if only one result was found, with salary "*"          (na_int == 1)
#        print no salary avaible for occupation found
#    if multiple results were found, but ALL had salary "*" (na_int > 1)
#        print no salaries avaible for occupations found
#    if absolutly no results were found (na_int == 0)
#        print key word not found
#elif one result found                                      (cnt_int == 1)
#    print 1 found, and average salary
#elif many results found                                    (cnt_int > 1)
#    print max,min,how many found, and average of them all
#####################################################################
file_str = ""    #Name of file inputed when prompted
#f_data          #File requested
title_str = ""   #Occupation name string
key_str = ""     #Key word string
sal_flt = 0      #salary value
cnt_int = 0      #count on keyword finds
min_int = 10e20  #wage minimum
max_int = -1     #wage maximum
sum_int = 0      #sum of wages for average
max_str = ""     #Occupation correlated with max salary
min_str = ""     #Occupation correlated with min salary
avg_int = 0      #averages of salaries
na_int = 0       #(Not Available)count number of occupations with "*" 
                   #incase the only occpuations found are those 
                   #with "*" i.e keyword = dancers. Without this it would
                   #Print "keyword not found"
#----------------------------------------------------------------
while True:                                 #Try-except for file finding
    file_str = input("Enter a file name: ") #enter a file name
    try:
        f_data = open(file_str, "r")
        break                              #if found, leave
    except FileNotFoundError:              #ask again if file not found
        print(file_str,": File not found. Try again")  
 #----------------------------------------------------------------       
key_str = input("Enter an occupational key word: ").lower() #input keyword
print("{:10s}{:20s}".format("Salary","Occupation")) #print header
f_data.readline()                                   #read text header
#----------------------------------------------------------------------
for line in f_data:                                 #Loop through lines
    if line[120:133].lower().strip() == "detailed": #if considered detailed
        title_str = line[10:120].strip()            #grab title of occup.
        if key_str in title_str.lower():            #if keyword in title
            try:
                sal_flt = float(line[172:185].strip())#convert salary to float
                if sal_flt > max_int:      #set max to salary if sal. greater
                    max_int = sal_flt
                    max_str = title_str    #store corresponding title of max
                if sal_flt < min_int:      #set min to salary if sal. smaller
                    min_int = sal_flt
                    min_str = title_str    #store corresponding title of min
                sum_int += sal_flt         #add to sum to calculate average
                cnt_int += 1               #add for keyword finds
                print("{:1s}{:7,.0f}  {:110s}".format("$",sal_flt,title_str))
            except ValueError:          #if cant convert to float ie "*"
                print("{:1s}{:^7s}  {:110s}".\
                format("$",line[172:185].strip(),title_str))
                na_int += 1 #count how many "*" salaries
                            #Does NOT add to sum or cnt variables
#-----------------------------------------------------------------------
if cnt_int == 0: #AKA NO results found OR all results found have "*" salary
    if na_int == 1:  #one result found, has "*" salary
        print("{}Occupation found has no salary available".format("\n"))
    elif na_int > 1: #more than one result but all found have "*" salary
        print("{}Occupations found have no salaries available".format("\n"))
    else: #Absolutely NO results found
        print("{:1s}{:^7s}  {:110s}".\
        format("$","*","None Found"))#Under Occ.Print within table'none found'
        print("{}Key word not found".format("\n"))  #state keyword not found 
        
elif cnt_int == 1: #ONE result found
    print("{}Across".format("\n"), cnt_int, \
    "occupation the average salary was ${:,.0f}".format(sal_flt))
    
else: #More than one result found
    avg_int = sum_int/cnt_int                                      #find avg
    print("\n{}{:7,.0f} {}".format("Max: $",max_int,max_str))      #Print Max
    print("{}{:7,.0f} {}".format("Min: $",min_int,min_str))        #Print Min
    print("{}Across".format("\n"), cnt_int, \
    "occupations the average salary was ${:,.0f}".format(avg_int)) #Print Avg
                                                                   #and count
   
     