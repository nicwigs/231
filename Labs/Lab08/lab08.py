name = ""   #name
x1 = 0      #exam1
x2 = 0      #exam2
x_list = []
avg = 0
s_list = []
cnt = 0
x1tot = 0
x2tot = 0

file_str = input("Enter file name: ")
print()
fp = open(file_str,"r")
for line in fp:
    name = line[:20].strip()
    x_list = line[20:].split()
    x1 = int(x_list[0])
    x2 = int(x_list[1])
    avg = (x1 + x2)/2
    tup = name,x1,x2,avg
    s_list.append(tup)
s_list.sort()
print("{:20s}{:7s}{:7s}{:7s}".format("Name","Exam 1","Exam 2","Average"))
print()
for s in s_list:
    print("{:20s}{:<7d}{:<7d}{:<7.2f}".format(s[0],s[1],s[2],s[3]))
for q in s_list:
    cnt += 1
    x1tot += q[1]
    x2tot += q[2]
print()
print("Exam 1 average: ",x1tot/cnt)
print("Exam 2 average: ",x2tot/cnt)
print(s_list)

    

