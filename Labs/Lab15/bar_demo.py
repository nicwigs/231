# Simple bar graph

import pylab

values = [20, 80, 50, 75]
indices = [i for i in range(len(values))]

# figsize adjusts the entire figure dimensions -- place before other pylab instructions
#pylab.figure(figsize=(10,5))

pylab.title("Simple Bar Graph Demo")
pylab.xlabel('X-axis label')
pylab.ylabel('Y-axis label')

# 1. These next two lines put labels on the x axis, one at each of the indices
#names = ['fred','ming','rose','rich']
#pylab.xticks(indices,names,rotation=90)

# 2. What does ylim do?
#pylab.ylim([0,100])


# simple plot
pylab.bar(indices,values)

# 3. more complex plot especially when combined with xticks line above
#mybarwidth = 0.8    # default is 0.8; you might want it smaller
#pylab.bar(indices,values,mybarwidth,align='center')
