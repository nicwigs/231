import csv
import pylab

fp = open("STC_2014_STC005.csv","r")

for i in range(3):
    fp.readline()

fp_reader = csv.reader(fp)
    
state_lst = []
for row in fp_reader:
    state_lst.append([row[2],(float(row[5])/float(row[3]))*100])

values = [state[1] for state in state_lst]
indices = [i for i in range(len(values))]

# figsize adjusts the entire figure dimensions -- place before other pylab instructions
pylab.figure(figsize=(11,8))

pylab.title("Ratio of Sales Tax to All State Taxes by State")
pylab.xlabel('State')
pylab.ylabel('Ratio')

# 1. These next two lines put labels on the x axis, one at each of the indices
states = [state[0] for state in state_lst]
pylab.xticks(indices,states,rotation=90)

pylab.ylim([0,100])

# 3. more complex plot especially when combined with xticks line above
mybarwidth = 0.8    # default is 0.8; you might want it smaller
pylab.bar(indices,values,mybarwidth,align='center')

