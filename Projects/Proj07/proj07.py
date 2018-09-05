def open_file():
    """
    Parameter:None
    prompts for year. Check whether the year is 1990 <= x <= 2014 
    Open data file ‘yearXXXX.txt’, where XXXX is the year. 
    Return: file pointer and year for data
    """
    yr_str = ""     #year string
    #fp = file pointer
    while True:
        yr_str = input("Enter a year where 1990 <= year <= 2014: ")
        try:             #see if the year is between desired boundaries   
            if int(yr_str) >= 1990 and int(yr_str) <=2014:                
                fp = open(("year" + yr_str + ".txt"), "r") #try opening file
                break        #if can open, leave loop
            else: #display error message if not in range
                print("Value not in range. Please try again")
        except ValueError: #display error message if not an integer
            print("Input must be an integer. Please try again")
        except FileNotFoundError: #display error message if file not found
            print("File not found. Please try again")
    return fp,int(yr_str)
#-----------------------------------------------------------------------
def change_type(lst):
    """
    Parameters: list
    makes each element their desired type
    (float if contains ".", int if number w/out ".")
    Returns: changed list 
    """
    for i in range(len(lst)):   #for each element in list
        lst[i] = lst[i].replace(",","") #get rid of all commas
        try: #if it can be converted directly to an int, its an int
            lst[i] = int(lst[i])
        except ValueError: #if it counldnt convert it is a str or float
            try:   #if it can convert to a float, its a float
                lst[i] = float(lst[i])
            except ValueError: #if couldnt convert to a float, its a string
                pass           #then dont change anything 
    if type(lst[2]) == str: #for the case that it says "and over" @ last line
        lst[2] = float("inf")  #make "over", the upper bound, infinity
    return lst
#----------------------------------------------------------------------------
def read_file():
    """
    Calls open_file() to get file pointer and year
    Calls change_type() to change file values to their respecitve types
    Returns: a list of data from file via open_file() and the year
    """
    """
    Data list entries:
    0 -bottom.....1-dash......2-top......3-#people
    4 - cummulative # in this and below.......5- cumulative %
    6-combined income.........7-average income
    """
    yr_int = 0      #year int
    data_list = []   #data list    
    open_file_tup = open_file()
    fp = open_file_tup[0]       #grab file pointer from open_file()
    yr_int = open_file_tup[1]   #grab year from open_file()
    fp.readline()             #read through title
    fp.readline()             #read through headers
    for line in fp:           #for each line
        line_list = line.split() #Create list for individual line      
        data_list.append(change_type(line_list)) #call change_type to make
        #elements in list to desired types, ie ints & floats
    fp.close()  #done using the file, close it
    return yr_int,data_list
#-------------------------------------------------------------------------
def get_range(data_list,percent):
    """
    Parameters:list of data,a percent 
    Returns: salary range for the data line whose cumulative % 
        is greater than or equal to the percent parameter, the cumulative % 
        value (Column 5) and the average income (Column 7).
    """
    for element in data_list:
        if element[5] >= percent:#if the cumulative % is >= than inputed %
           return [element[0],element[2]],element[5],element[7] #return
#-----------------------------------------------------------------------
def get_percent(data_list,income):
    """
    Parameters:list of data,an income 
    Returns: for the data line that the specified income is in the income 
        range (Columns 0 and 2), returns income range (Columns 0 and 2), 
        the cumulative % (Column 5) and the average income (Column 7)
    """    
    for element in data_list:  
        if element[0] <= income <= element[2]: #if income in range of bounds
           return [element[0],element[2]],element[5],element[7] #return
#-----------------------------------------------------------------------
def find_average(data_list):
    """
    Parameter: list of data
    Returns: Average salary
    """
    sum_int = 0   #income total sum
    avg = 0       #average salary
    for element in data_list:
        sum_int += element[6]  #get total sum of salaries
    avg = sum_int/data_list[len(data_list)-1][4] #divide total sum by total 
                                                 #people
    #total people is found by the cum. people in the last income range
    return avg
#------------------------------------------------------------------------
def find_median_range(data_list):
    """
    Parameter: data list
    Find the cumulative %s that are directly greater and less than 50%
    Calls get_range() to find the upper range %
    Return: Upper bound %, location in list of upper bound % (int),
            Lower bound %, location in list of lower bound % (int),
    """
    per_up_int = 0        #percent 1 value, upper bound (above 50%)
    per_lo_int = 0        #percent 2 value, lower bound (below 50%)
    loc_up_int = -1       #location of upper bound of range  
    loc_lo_int = 0        #location of lower bound of range
    
    per_up_int = get_range(data_list,50)[1] #find upper bound percentage using
                                            #get_range()
    for element in data_list:             #for list in data list
        loc_up_int += 1                   #keep track of location in list
        if element[5] == per_up_int:#find location in list of percent found 
                                    #from get_range()
            loc_lo_int = loc_up_int -1 #the lower bound location will be 1 less
                        #than the location of the upper bound in the list
            per_lo_int = data_list[loc_lo_int][5] #using the lower bound 
                                            #location find the lower bound %
            break #Once everything is found, leave the loop
    return per_up_int,loc_up_int,per_lo_int,loc_lo_int
#------------------------------------------------------------------------  
def find_median(data_list):
    """
    Parameter: list of data
    Algorithm:find the data line whose cumulative % is closest to 50% and 
    return its average income.
    If both data lines are equally close, return either one
    Calls find_median_range() to get locations and values of %s closest to 50
    Returns: Median income
    """    
    median_int = 0      #value of median salary
    range_tup = find_median_range(data_list) #grab percents and locations 
                                            #of bounds    
    if abs(50-range_tup[0]) < abs(50-range_tup[2]):#if upper bound closer to 50
       median_int = data_list[range_tup[1]][7] #median salary is upper bound
    else:
       median_int = data_list[range_tup[3]][7] #median sal is lower bound
    return median_int
#-----------------------------------------------------------------------
import pylab

def do_plot(x_vals,y_vals,year):
    """
    Plot x_vals vs. y_vals where each is a list of numbers of the same length.
    """
    pylab.xlabel('Income')                                       #x axis label
    pylab.ylabel('Cumulative Percent')                           #y axis label
    pylab.title("Cumulative Percent for Income in " + str(year)) #title
    pylab.plot(x_vals,y_vals)                                    #plot
    pylab.show()                                                 #show plot
#--------------------------------------------------------------------------
def ready_plot(data_list,year):
    """
    Parameters: list of data, year
    Takes first 40 values of average income (Column 0) and cumulative %
    (column 5) from the data list. Calls do_plot() to plot the values
    Return: None
    """
    x_vals = [data_list[x][0] for x in range(40)] #1st 40 lower bound income
    y_vals = [data_list[x][5] for x in range(40)] #their respective cum. %
    do_plot(x_vals,y_vals,year)                   #call plotting function
#--------------------------------------------------------------------------  
def print_header(data_list,year):
    """
    Parameters: list of data, year
    Prints the year title, average and median income for the year
    Average and median found by calling find_average() and find_median()
    Return: None
    """
    print("For the year", year,": ") #print year
    #Find average for year
    print("The average income was ${:<12,.2f}".format(find_average(data_list)))
    #Find median data
    print("The median income was ${:<12,.2f}".format(find_median(data_list)))
#-----------------------------------------------------------------------------
def prompt_range(data_list):
    """
    Perameters: list of data
    prompt for percent, find associated income, print
    Return: None
    """
    percent = 0 #percent inputed    
    lower_bound_int = 0 #lower bound of salary associtated with input %
    try:
        percent = float(input("Enter a percent: ")) #grab desired %
        lower_bound_int = get_range(data_list,percent)[0][0] #find income
        print("{:4.2f}% of incomes are below ${:<12,.2f}"\
        .format(percent,lower_bound_int)) #print
    except ValueError: #if int not entered, if percent cant be turned to int
        print("Invalid percent value entered") #say invalid
#--------------------------------------------------------------------------
def prompt_percent(data_list):
    """
    Perameters: list of data
    prompt for income, find associated %, print
    Return None
    """
    income = 0 #income inputed
    percent_flt = 0 #top percent associated with given salary
    try:
        income = float(input("Enter an income: ")) #grab desired income
        percent_flt = get_percent(data_list, income)[1] #find %
        print("An income of ${:<12,.2f} is in the top {:4.2f}% of incomes"\
        .format(income,percent_flt)) #print
    except ValueError: #if income cant be turned to int
        print("Invalid income value entered") #say invalid
#---------------------------------------------------------------------------
def loop_options(data_list):
    """
    Parameter: list of data
    Runs through loop prompting for possible options ie. r,p,"", 
    calls respective functions    
    Return: None
    """
    input_str = "" #input via user    
    #print choices
    input_str = \
    input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    while input_str != "":          #while enter somthing    
        if input_str == "r":        #if range
            prompt_range(data_list)
        elif input_str == "p":      #if percent
            prompt_percent(data_list)
        else:                       #if not an acceptable input
            print("Invalid command")#say invalid command
        #re-prompt user
        input_str = \
        input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
#--------------------------------------------------------------------------        
def main():
    """
    Parameters:None    
    Calls print_header() to print year, average and median income
    Calls ready_plot() to plot the data
    Calls loop_options() to continue to prompt for user commands
    Return: None
    """
    read_tup = read_file()
    year = read_tup[0] #grab inputted year from read_file()
    data_list = read_tup[1] #grab data list from file
   
    print_header(data_list,year) #print header, average and median average 
    ready_plot(data_list,year) #plot the data from the list from file
    loop_options(data_list) #keep prompting for user options, calls option
    #functions to do desired tasks
#-------------------------------------------------------------------------
main()
    

    