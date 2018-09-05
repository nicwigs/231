# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:25:24 2016

@author: wolfem
"""

#PROJECT 9

#project should take two files, make a dictionary together, take the averages
#and the max-adoption rates and print them into a nice neat format

def input_func ():
    '''
    function for inputing
    '''
    while True:
        food_input = input("Input filename for food crop: ") #input
        dict1 = {}  #making a food_crop dictionary
        try:
            data = open(food_input) #opens it
            data.readline() 
            temp_dict = data.readline().split()
            final_dict = temp_dict.pop() #getting rid of the last column
            data.readline()
            
            for line in data:
                line_list = line.strip().split(",") #gets rid of the commas
                
                #dict1.update({line_list[0]:line_list[1:final_dict]}) #ERROR HERE
                dict1.update({line_list[0]:line_list[1:]})
                #print(food_dict)
        except FileNotFoundError:
            print("Filename not found")
       # print("dict1: ",dict1)
        #non_food_input = ("Input filename for non-food crop: ") #input
        non_food_input = input("Input filename for non-food crop: ") #input
        dict2 = {} #making a non-food_crop dictionary
        try:
            non_fdata = open(non_food_input) #opens it
            non_fdata.readline()
            temp_dict = non_fdata.readline().split()
            final_dict = temp_dict.pop() #gets rid of last column
            #print("final dict",final_dict)
            non_fdata.readline()
            for line in non_fdata:
                line_list = line.strip().split(",") #gets rid of the commas
                #print(line_list)
                #dict2.update({line_list[0]:line_list[1:final_dict]}) #ERROR HERE
                dict2.update({line_list[0]:line_list[1:]})
                #print(non_food_dict)

        except FileNotFoundError:
            print("Filename not found")
        #print("dict2: ",dict2)  
        #print("going to leave")
        break    
    
    main(dict1, dict2)
    #printing()
    data.close()
    non_fdata.close()
    
def sort_func(dict1, dict2):
    '''
    puts the keys together and sorts it
    '''    
    #print("in sort func")
    lst = [] 
    for i in dict1:
        if i != "Other States" and i != "other states":
            #if i isnt other states then add it to the list and sort
            lst.append(i)
            lst.sort()
    for i in dict2:
        if i != "Other States" and i != "other states" and i not in lst:
            #if i isnt other states then add it to the list and sort
            lst.append(i)
            lst.sort()
    #print("list in sort func",lst)
    return lst

def find_average(lst):
    '''
    finds the average of that data
    '''
    #print("in find average")
    tot_avg = 0
    denominator = 0
    #print("find average list", lst)
    lst.pop()
    for i in lst:
        if i != "": #if it isn't empty
            tot_avg += float(i) #tot_avg = i
            denominator += 1 #adds one to the denominator
    final_tot_avg = float(tot_avg/denominator) #total divded by denominator
    return final_tot_avg

def max_func(dict1):
    #print("in max_func")
    '''
    finds the max-adoptiong rate and displays it correctly
    '''
    holder = 0
    list1 = [] #year list
    max_list = [] 
    max_val = 0
    min_val = 100000 #some big number
    max_year = 0
    min_year = 100000 #some big number
    rate = 0
    while holder < 15:
        list1.append(2000+holder)
        holder += 1
    #print(list1) 
    #print(dict1)
    for i in dict1:
       # print(i)
        max_val = 0
        min_val = 100000 #some big number
        max_year = 0
        min_year = 100000 #some big number
        if i != "Other States" and i != "other states":
            holder = 0 #place holder for year
            #print(dict1[i])
            for x in dict1[i]:
                holder += 1
                if x != "": #if it isn't empty
                    #x = int(x.strip())
                    val_holder = int(x)
                    if val_holder > max_val: #seeing if it is a max
                        max_val = int(x)
                        max_year = int(list1[holder - 1])
                        #print("max val",max_val)
                       # print("max year",max_year)
                    if val_holder < min_val: #seeing if it is a min
                        min_val = int(val_holder)
                        min_year = int(list1[holder - 1])
                       # print("min val",min_val)
                        #print("min year",min_year)
            rate = ((max_val - min_val)/(max_year-min_year)) #calculating rate
            #max_list = [rate, i, min_year, max_year]
            max_list.append([rate, i, min_year, max_year])
           # print("max final lst", max_list)
    max_list.sort(reverse = True) #Reverses the order of the list
    #print("max final lst", max_list)
    return max_list
      
def main(dict1,dict2):
    '''
    main function
    '''    
    lst = sort_func(dict1,dict2) #calls the sort functiong
    holder = 0 #holds spot
    print("{:15}{:15}{:15}".format("State", "Food Crop", "Non-Food Crop"))
    while holder < len(lst):
        if lst[holder] in dict1:
            food_avg = find_average(dict1[lst[holder]]) #calling average func
        if lst[holder] in dict2:
            non_food_avg = find_average(dict2[lst[holder]]) #calls average func
            
        if lst[holder] in dict1 and lst[holder] in dict2: 
            #if its in both dict1 and dict2
            food_avg = str("{:>16.3f}".format(food_avg)) #formatting
            non_food_avg = str("{:>16.3f}".format(non_food_avg)) #formatting
            print("{:15}{:15}{:15}".format(lst[holder], food_avg, non_food_avg))
        elif lst[holder] in dict1 and lst[holder] not in dict2:
            #if its in dict1 and not dict2
            food_avg = str("{:>16.3f}".format(food_avg))
            
            print("{:15}{:15}{:>15}".format(lst[holder], food_avg, "N/A"))
        elif lst[holder] in dict2 and lst[holder] not in dict1:
            #if its in dict2 and not dict1
            non_food_avg = str("{:>16.3f}".format(non_food_avg))
            
            print("{:15}{:>15}{:15}".format(lst[holder], "N/A", non_food_avg))
        holder += 1
    printing(dict1,dict2) #calls the printing function below
        
def printing(dict1,dict2):
    print("in printing")
    '''
    function used for printing
    '''
    print("Percent max_adoption rate for food crop.")
    print("Crop: Corn")
    food_list = max_func(dict1)
    non_food_list = max_func(dict2)
    print("{:15}{:15}{:15}{:15}".format("State","Rate","Min-Year","Max-Year"))
    for line in food_list:
        fin_line = float(line[0])
        if fin_line > 0:
            final_rate = ("{:>16.3f}".format(fin_line))
            print("{:15}{:15}{:15}{:15}".format(line[1],final_rate,line[2],line[3]))
        if fin_line < 0:
            final_rate = ("{:>16.3f}".format(fin_line))
            print("{:15}{:15}{:15}{:15}".format(line[1],final_rate,line[2],line[3]))
            
    print("Percent max_adoption rate for non-food crop.")
    print("Crop: Cotton")
    print("{:15}{:15}{:15}{:15}".format("State","Rate","Min-Year","Max-Year"))
    for line in non_food_list:
        fin_line = float(line[0])
        if fin_line > 0:
            final_rate = ("{:>16.3f}".format(fin_line))
            print("{:15}{:15}{:15}{:15}".format(line[1],final_rate,line[2],line[3]))
        if fin_line < 0:
            final_rate = ("{:>16.3f}".format(fin_line))
            print("{:15}{:15}{:15}{:15}".format(line[1],final_rate,line[2],line[3]))
  

#MAIN()
#calls it all 
dict1 = {} #food dictionary
dict2 = {} #non-food dictionary        
input_func()
