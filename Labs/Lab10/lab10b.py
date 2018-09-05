def open_file():
    in_file1 = open("data1.txt","r")
    in_file2 = open("data2.txt","r")
    score_dict = {}
    read_file(in_file1,score_dict)
    read_file(in_file2,score_dict)
    sort(score_dict)    
    print_file(sort(score_dict))
#-------------------------------------------------------------------
def read_file(file,score_dict):    
   file.readline()
   for line in file:        
        name_lst = line.split()
        name_lst[1] = int(name_lst[1])
        add_name(score_dict,name_lst)
#---------------------------------------------------------------------        
def add_name(score_dict, name_lst):
    try:
        score_dict[name_lst[0]] += name_lst[1]
    except KeyError:
        score_dict[name_lst[0]] = name_lst[1]
#-------------------------------------------------------------------------        
def print_file(score_lst):
    print("{:6s}{:6s}".format("Name","Total"))
    for person in score_lst:
        print("{:6s}{:<6d}".format(person[0], person[1])) 
#-------------------------------------------------------------------------        
def sort(score_dict):
     score_lst = []
     for name,score in score_dict.items():
         score_lst.append((name,score))
     sort_lst = sorted(score_lst)
     return(sort_lst)
#--------------------------------------------------------------------------
open_file()
        
    