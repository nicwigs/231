cnt = 0
min_h = 1000000
max_h = -1
min_w = 1000000
max_w = -1
min_b = 1000000
max_b = -1
b = 0
name = ""
h = 0
w = 0
tot_h = 0
tot_w = 0
tot_b = 0
avg_h = 0
avg_w = 0
avg_b = 0


filein = open("data.txt","r")
fileout = open("output.txt", "w")
filein.readline()
print("{:12s}{:12s}{:12s} {:12s}".\
format("Name","Height(m)","Weight(kg)","BMI"),file = fileout)
for line in filein:
    name = line[0:line.find(" ")]
    h = float(line[12:24].strip())
    w = float(line[24:36].strip())
    b = w/h**2
    if h < min_h:
        min_h = h
    if h > max_h:
        max_h = h
    if w < min_w:
        min_w = w
    if w > max_w:
        max_w = w
    if b < min_b:
        min_b = b
    if b > max_b:
        max_b = b
    cnt +=1
    tot_h += h
    tot_w += w
    tot_b += b
    print("{:12s}{:<12.2f}{:<12.2f}{:<12.2f}"\
    .format(name,h,w,b),file = fileout)
avg_h = tot_h / cnt
avg_w = tot_w / cnt
avg_b = tot_b / cnt
print(file = fileout)
print("{:12s}{:<12.2f}{:<12.2f}{:<12.2f}"\
.format("Average",avg_h,avg_w,avg_b),file = fileout)
print("{:12s}{:<12.2f}{:<12.2f}{:<12.2f}"\
.format("Max",max_h,max_w,max_b),file = fileout)
print("{:12s}{:<12.2f}{:<12.2f}{:<12.2f}"\
.format("Min",min_h,min_w,min_b),file = fileout)
fileout.close()
filein.close()
