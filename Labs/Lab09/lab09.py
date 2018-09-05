def open_file():
   """Contuinues to prompt for file until file found"""
    
   file = ""
   while True:
        try:
            file = input("Enter file Name: ")
            fp = open(file, "r")
            break
        except FileNotFoundError:
            print("File Not Found /n")
   return fp

def digit():
    fp = open_file()
    cnt_list = [[1,0,0,0],[2,0,0,0],[3,0,0,0],[4,0,0,0],[5,0,0,0],[6,0,0,0],[7,0,0,0],[8,0,0,0],[9,0,0,0]]
    for line in fp:
        line = line.strip()
        if line[0].isdigit() and line[0] != "0":
            cnt_list[(int(line[0])-1)][1] += 1
    #print(cnt_list)         
    return cnt_list

def formatt():
    BL = ["(30.1%)","(17.6%)","(12.5%)","(9.7%)","(7.9%)","(6.7%)","(5.8%)","(4.1%)","(4.6%)"]
    sum_int = 0
    cnt_list = digit()
    for i in range(9):        
        sum_int += cnt_list[i][1] 
    for i in range(9):        
        cnt_list[i][2] = (cnt_list[i][1]/sum_int)*100
        cnt_list[i][3] = BL[i]
    #print(cnt_list)    
    return(cnt_list)    
        
def print_digit():
    cnt_list = formatt()    
    print("{:6s}{:8s}{:8s}".format("Digit","Percent","Benford"))
    for element in cnt_list:
        print("{:4d}{}{:7.1f}{}{:>8s}".format(element[0],":",element[2],"%",element[3]))
print_digit()    