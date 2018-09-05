
import requests
from bs4 import BeautifulSoup
#-----------------------------------------------------------------------
def grab_netid(lst,payload) -> "netid" :
    """
    Parameters: list of info and correct payload used to get info
    Finds the net id
    if name was used to search and the net id cannot be found, it prints an
    exception and returns a net id of 0
    Returns: net id 
    """
    payload,mail_id = payload,lst[5]      
       
    if "nid" in payload:                     #if given the net id, grab it
        net_id = payload["nid"]
    elif mail_id:     #if there is an email that was grabbed online,get net id
        net_id = mail_id[:mail_id.find("@")] #Grab NetID 
    else:                        #if no net id, cant add to dict, note it       
        print ("-" * 50)
        #if no net id, the only info that us known is the name via the users 
        #search, thus grab it from their search ie. the payload
        lst[0] = payload["lst"] + ", " + payload["fst"]  #name from search
        print("[ - ] No Net ID found: {} was not added to dictionary"\
        .format(lst[0]))
        print ("-" * 50)      
        net_id = 0 #return 0 if none found
    return net_id
#-------------------------------------------------------------------
def find_name(lst,net_id):
    """
    Parameter: List of info and net id
    Sometimes when searching if name cannot be found in the system it will
    print this case    
    """
    if not lst[0]: #if no name, searched using net id, but none found            
        print ("-" * 50)
        print("[ - ] No results found for {}".format(net_id))    
        print ("-" * 50)
#--------------------------------------------------------------------------
def missing_areas(lst):
    """
    Parameter: List of info
    title, status, and major already grab their descriptors via the web
    if these arnt avilable they return "", below fixes this to show
    whats missing 
    """
    if not lst[6]: #if title is blank, show descriptor 
        lst[6] = "Title: "
    if not lst[7]: #if status is blank, show descriptor 
        lst[7] = "Status: "
    if not lst[8]: #if major is blank, show descriptor 
        lst[8] = "Major: " 

#---------------------------------------------------------------------
def query_MSU_online_database(D,payload):
    '''Parameters: dictonary and payload
       Scrape one name (specified in payload) from MSU's People web page;
       updates the dictonary D dictionary with NetID as the key.'''    
    try:    
        '''
        This function is called for each student. It begins by posting
        payload (NetID or Firstname, Lastname) to the MSU people database.
        '''
        primary_URL = "https://search.msu.edu/people/"
        response = requests.post(primary_URL, data=payload, timeout=30)
        soup = BeautifulSoup(response.content, "lxml")        
        '''This little part below is very important. We need to grab the UID
        of each student and then contruct a link using this UID. 
        This secondary link will contain the private details we are looking for.
        To understand why we need to do this, query the MSU people database 
        manually and observe the creation of the link containing the UID that 
        we are required to click before student's private details are shown to us.
        '''
        uid = ""
        for uid in soup.find_all('li',{'class':'name'}):
            if uid.a:    
                uid = uid.a.get("href")
        secondary_URL = 'https://search.msu.edu/people/' + uid   
        response = requests.get(secondary_URL)
        soup = BeautifulSoup(response.content, "lxml")
        #pretty_HTML = soup.prettify() #used this to observe HTML while coding
        #print(pretty_HTML)            #to know what to search for        
        '''
        In this next part, we look for private details of students,
        print them on the screen, and store them in a file.
        '''    
        name, current_address, current_phone, permanent_address,\
        permanent_phone, mail_id, title, status, major \
        = "","","","","","","","",""
        
        for info in soup.find_all('li',{'class':'name'}):
            name = info.text.strip()
        #added code for faculty names,
        if not name: #if name empty try search for tag "name-e"
            for info in soup.find_all('li',{'class':'name-e'}):
                name = info.text.strip()
        #end of added lines
        for info in soup.find_all('li',{'class':'homepostaladdress'}):
            current_address = info.text.strip()
        for info in soup.find_all('li',{'class':'homephone'}):
            current_phone = info.text.strip()
        for info in soup.find_all('li',{'class':'permanentpostaladdress'}):
            permanent_address = info.text.strip()
        for info in soup.find_all('li',{'class':'permanentphone'}):
            permanent_phone = info.text.strip()
        for info in soup.find_all('li',{'class':'mail'}):
            mail_id = info.text.strip()
        for info in soup.find_all('li',{'class':'title'}):
            title = info.text.strip()
        for info in soup.find_all('li',{'class':'classdesc'}):
            status = info.text.strip()
        for info in soup.find_all('li',{'class':'majordesc'}):
            major = info.text.strip()    
            
        person_lst = [name,current_address,current_phone,permanent_address,\
        permanent_phone,mail_id,title,status,major]  #value of the dict 

        missing_areas(person_lst)   #takes care of missing info ie. title, etc
        net_id = grab_netid(person_lst,payload)#finds net_id or prints notfound
        find_name(person_lst,net_id)   #takes care of case if no results found
        
        """net id is 0 if not found, name will be empty if not found; 
           either of these cases should not add anything to the dict
        """
        
        if net_id and person_lst[0]:#if net id & name are both known            
            D[net_id] = person_lst  #add them to the dict          
            print_dict(D,net_id)    #print out the persons info          
        #no return needed, D is referenced to net_it_map and is mutated
    except requests.ConnectionError:
        print("[ - ] No internet connection available.")
    except requests.exceptions.ReadTimeout:
        print("Connection timed out")
#----------------------------------------------------------------------
#-----------------------------------------------------------------------
def banner():
    '''Just a banner'''
    asciitext = '''
     __  __ ____  _   _   ____  _        _ _             
    |  \/  / ___|| | | | / ___|| |_ __ _| | | _____ _ __ 
    | |\/| \___ \| | | | \___ \| __/ _` | | |/ / _ \ '__|
    | |  | |___) | |_| |  ___) | || (_| | |   <  __/ |   
    |_|  |_|____/ \___/  |____/ \__\__,_|_|_|\_\___|_|   
                                                 
      ____           _             _ 
     / ___|___ _ __ | |_ _ __ __ _| |
    | |   / _ \ '_ \| __| '__/ _` | |
    | |__|  __/ | | | |_| | | (_| | |
     \____\___|_| |_|\__|_|  \__,_|_| CSE 231 - Spring 2016
     '''
    print(asciitext)
#-------------------------------------------------------------------------
def print_dict(info_map,net_id):
    """
    Parameters: info dictonary, and net_id
    Prints information for each person in correct format
    """
    print ("-" * 50)
    print("[ + ] Name: {}".format(info_map[net_id][0]))
    print ("-" * 50)
    print("[ + ] Current Address: {}".format(info_map[net_id][1]))
    print("[ + ] Current Phone: {}".format(info_map[net_id][2]))
    print("[ + ] Permanent Address: {}".format(info_map[net_id][3]))
    print("[ + ] Permanent Phone: {}".format(info_map[net_id][4]))
    print("[ + ] Mail ID: {}".format(info_map[net_id][5]))
    print("[ + ] {}".format(info_map[net_id][6]))
    print("[ + ] {}".format(info_map[net_id][7]))
    print("[ + ] {}".format(info_map[net_id][8]))
    print ("-" * 50)
#----------------------------------------------------------------------------
#----------------------------------------------------------------------
def find_using_netid(info_map,given_netid):
    """
    parameters: info_map dictonary, net id    
    grab information via database function and updates dictonary 
    """    
    if len(given_netid) <= 8:             #make sure its a valid Net ID length                
        payload = {'nid':given_netid}     #write correct payload
        print("[ * ] Searching....")      #sometimes it takes a while
        query_MSU_online_database(info_map,payload) #call to update dict
    else:
        print("[ - ] Net ID's are 8 or less characters, try again")         
#------------------------------------------------------------------------
def find_using_name(info_map,first_str,last_str):
    """
    parameters: info_map dictonary, first name, last name    
    grab information via database function and updates dictonary 
    """    
    payload = {"fst":first_str,"lst":last_str} #build corresponding payload
    print("[ * ] Searching....") #may take a while to grab info
    query_MSU_online_database(info_map,payload) #call for info

#----------------------------------------------------------------------
#----------------------------------------------------------------------
def single_netid(info_map):
    """
    parameters: info_map dictonary   
    call find_using_netid to update dictonary
    """    
    given_netid = input ("[ 1 ] Enter NetID: ")
    find_using_netid(info_map,given_netid)
#------------------------------------------------------------------------
def single_name(info_map):
    """
    parameters: info_map dictonary
    prompt for first and last name
    call find_using_name to update dictonary 
    """    
    try:
        first_str,last_str = \
        input("[ 2 ] Enter first and lastname, seperated by a space: ")\
        .strip().split()             #grab first and last name       
        find_using_name(info_map,first_str,last_str)
    except ValueError:              #if not entered 2 words seperated by " "
        print("[ - ] Only two words anticipated ie. 'Barack Obama' ")
#----------------------------------------------------------------------
def display_dict(info_map):
    """
    parameters: info_map dictonary
    calls print_dict to print info in correct format for each line
    """  
    for key in info_map:
        print_dict(info_map,key) #print in desired format
#---------------------------------------------------------------------
def remove_entry(info_map):
    """
    parameters: info_map dictonary
    prompt for net id to remove
    updates dictonary with desired element removed
    """  
    try:    
        net_id = input("[ 6 ] Enter Net ID you wish to remove: ")
        del info_map[net_id]        #delete desired key and value
        print("[ + ] {} was succesfully removed".format(net_id))
    except KeyError:                #If Net ID entered is not in dictionary
        print("[ - ] net id not found in dictonary")
#--------------------------------------------------------------------
def open_file():
    """
    prompts for file name, trys to open file
    returns file pointer
    """  
    while True:
        file_str = input("[ + ] Enter file name: ") #prompt
        try:
            fp = open(file_str, "r")
            return fp  
        except FileNotFoundError:                   #if file not found
            print("[ - ] File Not Found") 
#-------------------------------------------------------------------
def mult_netid(info_map):
    """
    parameters: info_map dictonary
    reads in file of multiple net ids
    call find_using_netid to update dictonary
    """  
    fp = open_file()   
    for line in fp:        
        find_using_netid(info_map,line.strip())     #call funct to update dict
    fp.close()                                      #close file when done
#-------------------------------------------------------------------
def mult_name(info_map):
    """
    parameters: info_map dictonary
    reads in file of multiple first and last names
    call find_using_name to update dictonary
    """     
    fp = open_file()    
    for line in fp: 
        try:
            first_str,last_str = line.strip().split()   #grab first & last name
            find_using_name(info_map,first_str,last_str)
        except ValueError:           #if not entered 2 words seperated by " "
            print("[ - ] Only two words anticipated ie. 'Barack Obama' ")
    fp.close()                                      #close file when done
#-------------------------------------------------------------------
def write_dict(info_map):
    """
    parameters: info_map dictonary
    writes the dictionary to a file
    """ 
    out_fp = open("MSU_DB.txt", "w")        #open desired file
    print(info_map, file = out_fp)          #print dict
    print("[ + ] File succesfully written") #Tell user it has been completed
    out_fp.close()                          #close file when done
#----------------------------------------------------------------------
def main():
    '''
    Main Function: Input file type refers to whether we are providing an input
    file that contains: 1. Firstname Lastname pairs or
    2. NetIDs. The user is forced to choose between 1 or 2.
    For each command a seperate function is called to handle prompting for
    the correct information. From there if adding info, these functions call
    functions that create the correct payload, ie "find_using_name()", from
    which the function 'query_MSU_online_database()' is called which updates 
    the master dictonary
    '''
    MENU = '''
      1. NetID
      2. Firstname Lastname
      3. Multiple NetIDs from file
      4. Multiple Firstname Lastname pairs from file
      5. Display dictionary
      6. Remove name from dictionary
      7. Write dictionary
      x. Exit'''
        
    banner()                            #print banner
    print(MENU) 
    net_id_map = {}                     #initalize master dictonary 
    while True:
        command = input("Enter Command: ")
        if command == "1":              #Given Net ID          
            single_netid(net_id_map)
        elif command == "2":            #Given name
            single_name(net_id_map)            
        elif command == "3":            #Given file of net ids
            mult_netid(net_id_map)
        elif command == "4":            #Given file of names
            mult_name(net_id_map)
        elif command == "5":            #Display Dictonary
            display_dict(net_id_map)
        elif command == "6":            #Remove name from dictonary
            remove_entry(net_id_map)
        elif command == "7":            #Write Dictonary to file
            write_dict(net_id_map)
        elif command.lower() == "x":    #exit
            print("[ + ] Program terminated succesfully")
            break
        else:                           #invlaid command
            print("[ Error ] Invalid command, view the menu below")
            print(MENU)
#------------------------------------------------------------------------
main()


    
   