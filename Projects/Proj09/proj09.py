from operator import itemgetter #for sorting inn  funct. "adoption_rates"
#---------------------------------------------------------------------
def open_file(crop_type) -> "fp":
   try:
       file_str = input("Enter file name for {} crop: ".format(crop_type))
       fp = open(file_str,"r")  #try to open
       return fp
   except FileNotFoundError:#if not found, say error, will return none to end
       print("File {} was not found".format(file_str))
#----------------------------------------------------------------
def add_file_entry(data_map,fp,crop_type,year_lst):
    """
    Parameters: the main data dictionary, the file pointer, the crop type and
                the year list
    adds states and their information to the dictonary according to the 
    template below
    """
    ##########################################################
    """
    data_map is formated like the following with multipile states:
    {state1:{'food':[[%1,year1],[%2,year2]],
            'non-food':[[%1,year1],[%2,year2]]},
     state2:{'food':[[%1,year1],[%2,year2]],
            'non-food':[[%1,year1],[%2,year2]]}}            
    """    
    #############################################################
    for line in fp:        
        line_lst = line.strip().split(",") #get list of info
        """
        use list comprehension to add the list of lists for the crop type 
        key for the state key in master dictonary. The if will exclude 
        years with no data. line_lst starts at 1+i since its 0 index is the
        state name, while the year_lst[0] = 2000 which is needed
        """
        try:           #is state already in dictonary?           
            data_map[line_lst[0]][crop_type] = \
            [[int(line_lst[i+1]),int(year_lst[i])] \
            for i in range(len(year_lst)) if line_lst[i+1]]                
        except KeyError: #if not add it
            data_map[line_lst[0]] = \
            {crop_type: [[int(line_lst[i+1]),int(year_lst[i])] \
            for i in range(len(year_lst)) if line_lst[i+1]]}
                
    del data_map["Other States"] #deletes "other states" since never used
#-----------------------------------------------------------------------
def read_file(data_map,crop_type) -> "crop":
    """
    Parameters: the master dictionary, and the type of crop (food or non-food)
    grabs the file pointer from funct "open_file()"
    if the fp is not None ie file was found it continues, skips the first line,
    grabs the crop name,and a list of year values and calls "add_file_entry()"
    to update the master dictionary
    return: the crop name
    """
    fp = open_file(crop_type)                               #grab file pointer
    if fp:                                                  #if it opened file      
        fp.readline()                                       #skip first header
        crop = fp.readline().strip().split()[-1]            #get name of crop
        year_lst = fp.readline().strip().split(",")[1:16]   #make year list    
        add_file_entry(data_map,fp,crop_type,year_lst)      #update dictonary
        fp.close()
        return crop                                  
#-----------------------------------------------------------------------------
def get_format_for_printing(state,rate_map) -> "format_str":
    """
    Parameters: the state for which is being printed,planting rate dictionary
    The rate dictionary contains the average planting rate for both crop types
    associated with a state. Many states dont have both crops, thus their 
    result is 'N/A' which requires a string formatting versus a floating point
    format. 
    This checks which type each field is and makes the correct format string
    Returns: correct format string
    """    
    
    if type(rate_map[state]["food"]) == float and \
    type(rate_map[state]["non-food"]) == float: #if both values floats
        format_str = "{:20} {:>16.3f} {:>16.3f}" 
    elif type(rate_map[state]["food"]) == float: #if only food crop is a float
        format_str = "{:20} {:>16.3f} {:>16}"
    else:                                     #if only non-food crop is float
        format_str = "{:20} {:>16} {:>16.3f}"
    return format_str
#----------------------------------------------------------------------------
def print_planting_rates(rate_map):
    """
    Parameters: the planting rate dictionary
    creates sorted list of the rate dictionary, this sorts it via alpahabetical
    order of the state (the key) names.
    Prints the info in the planting rates dictionary with the right format
    """
    
    print() 
    print("{:20} {:>16} {:>16}".format("State","Food Crop","Non-Food Crop")) 
    
    sorted_states_lst = sorted(rate_map) #sorted keys (state names)
    
    for state in sorted_states_lst:      #loop for each state
        format_str = get_format_for_printing(state,rate_map)
        print(format_str\
        .format(state,rate_map[state]["food"],rate_map[state]["non-food"]))        
    print("-"*80)
#---------------------------------------------------------------------------
def planting_rates(data_map) -> "rate_dict":
    """
    Parameters: master dictionary
    Takes the state name, totals a sum of percentages and divdes by the number
    of years to get the average planting rate and adds this infomation into 
    the rate dictionary with template shown below
    return: rate dictionary
    """
    ########################################
    """
    rate_map formated like the following
    {state1:{'food':%, 'non-food':%},
     state2:{'food':%, 'non-food':%}}    
    """
    #################################################
    rate_map = {}                                #initialize dict
    for state in data_map:                       #for each state in master dict
        rate_map[state] = {}        #initialize a key and value for that state
        for crop_type in data_map[state]:           #for each crop type      
            rate_sum = 0                            #initalize the sum to 0
            for year in data_map[state][crop_type]:#for each list in list of %              
                rate_sum += int(year[0])           #add the % to sum
            average = rate_sum / len(data_map[state][crop_type])
            rate_map[state][crop_type] = average      #add average to rate dict
        """    
        averages only added for the crop types the state has
        if the state is missing a key(food, non-food) add it with value "N/A"
        """
        if "food" not in rate_map[state]: 
            rate_map[state]["food"] = "N/A"
        elif "non-food" not in rate_map[state]:
            rate_map[state]["non-food"] = "N/A"
            
    return rate_map
#-----------------------------------------------------------------------
def print_adoption_rates(adopt_lst,crop,crop_type):
    """
    Parameters: adoption rates lst, the crop name, and crop type
    Sorts the list, so it prints smallest to largest rate of adoption
    Prints data in correct format from the list    
    """
    print("Percent max_adoption rate for {} crop.".format(crop_type))
    print()
    print("Crop: ",crop)
    print()
    print("{:20} {:>16} {:>16} {:>16}"\
    .format("State","Rate","Min-Year","Max-Year"))
    print()
    adopt_lst.sort(reverse = True)  #sort list(smallest to largest adoption rates)
    
    for state in adopt_lst:
        print("{:20} {:>+16.3f} {:>16} {:>16}"\
        .format(state[1],state[0],state[2],state[3]))
    
    print("-"*80)

#-------------------------------------------------------------------------
def adoption_rates(data_map,crop_type) -> "adopt_lst":
    """
    Parameters: master dictionary and crop type
    Using master dictionary, for each state it finds the maximum and minimum
    % and their corresponding years, using the formula given it calculates the
    max-adoption rate
    adds the info into a list with format template below
    returns: the adoption list
    """
    ##################################################
    """
    adopt_lst formated like the following
        [[rate,state,min_year,max_year],
         [rate2,state2,min_year2,max_year2]]     
    """
    ############################################
    adopt_lst = [] #intialize list
    for state in data_map:   
        #if the state doesnt have the crop type specified, nothing is added   
        if crop_type in data_map[state]:  
            """
            these two sorts get it so percent is lowest to highest, and
            if there is a tie in percents the left most value will have the
            the lowest year
            """
            year_sort_lst = \
            sorted(data_map[state][crop_type],key=itemgetter(1)) #sort by year
            percent_sort_lst = sorted(year_sort_lst, key = itemgetter(0))#by %  
            #grabs info for minimum percent
            min_percent = percent_sort_lst[0][0]
            min_year = percent_sort_lst[0][1] 
            """
            A reverse sort allows the percents to be largest at left, while
            keeping the years low to high for tied percent
            """
            percent_sort_lst = \
            sorted(year_sort_lst, key = itemgetter(0),reverse = True) #by %      
            #grabs info for maximum percent
            max_percent = percent_sort_lst[0][0]
            max_year = percent_sort_lst[0][1]
            """
            the formula requires the the knowledge of which year is the 
            largest. Note:max_year is associated with max_percent not the 
            biggest/most current year
            """
            if max_year > min_year:                
                rate = (max_percent - min_percent)/(max_year - min_year)
            else: #switch places of variables
                rate = (min_percent - max_percent)/(min_year - max_year)
                
            adopt_lst.append([rate,state,min_year,max_year])            
           
    return adopt_lst
#-----------------------------------------------------------------------------          
def main():
    """
    checks to make sure both files are found, if so continues with the program
    updates the master map if the file is found
    creates the planting rates map from funct "planting_rates" and prints it
    Creates food and non-food adoption rate lists from funct "adoption_rates"
    prints both of these lists in correct format
    """
    master_map = {} #initalize master dictionary
    
    f_crop = read_file(master_map,"food")
    if f_crop:   #will be none if file not found ie. program quit if not found
        nf_crop = read_file(master_map,"non-food")      
        if nf_crop: #if non-food file not found, quit
        
            planting_rates_map = planting_rates(master_map)           
            food_adopt_rates_lst = adoption_rates(master_map,"food")
            non_food_adopt_rates_lst = adoption_rates(master_map,"non-food")
            
            print_planting_rates(planting_rates_map)    
            print_adoption_rates(food_adopt_rates_lst,f_crop,"food")
            print_adoption_rates(non_food_adopt_rates_lst,nf_crop,"non-food")
#----------------------------------------------------------------------------
main()