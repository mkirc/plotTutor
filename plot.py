# this is a comment in python
# everything following a '#' will not be interpreted by the python interpreter

# following are 'imports', they include some foreign code in your code.
# this code is called a package, and is subdivided in modules

# numpy (numerical python) is a package for scientific data manipulation
import numpy as np

# matplotlib is *the* stadard plotting package. 
# it integrates well with numpy,but there are many more
import matplotlib.pyplot as plt

# i bet you figure out, what this package does:
import random


# this function generates 100 random numbers and puts them in a list
xList = []
for randomNumber in range(100):
	xList.append(random.randrange(100))

# now we enter values into a numpy.array object. 
# you can think of it as a list 
x = np.array(xList)


yList = []
for yNum in range(100):
	yList.append(yNum)
# also we need a list for y values. we also generate an array for that
y = np.array(yList)



# now we introduce an important concept: a list of lists
# or think of it as... a matrix!
values = np.array([y, x])

# the assert statement tests if some condition is true
# and stops execution otherwise. it is a handy tool
# to test your assumptions
assert values.shape == (2, 100) # its shape is 2x100


# now we compute the mean and standard deviation of x
# lets define a function which takes a list of values as
# input, computes the mean and returns it!
def myMean(vList):

	mean = sum(vList)/len(vList)
	return mean

# there is also a numpy implementation, 
# but it comes down to the same thing.
xMean = np.mean(x)
assert myMean(x) == xMean # see?


# so now we go for the standard deviation
# first lets try to implement out own:

def myStd(vList, sample=False):

	# first we need to compute the mean of all values
	# i'll use the numpy version for brevity
	vBar = np.mean(vList)

	# now we compute the sum of the squared deviations
	dSum = np.sum((vBar - vList)**2)

	# now we divide by n for the population
	# or n-1 for a sample

	if not sample:
		sqArg = dSum / len(vList)
	else:
		sqArg = dSum / (len(vList) - 1)


	# and compute the sqare root
	fin = np.sqrt(sqArg)

	# you may be asking yourself, why we are doing this stepwise
	# it's really just for readability; why don't you try to
	# implement your own standard deviation function as short as
	# possible?

	return fin 

# note, that np.std uses n as the denominator
# so it can be better to use your own function

xStd = np.std(x)
assert myStd(x) == xStd # comment out if you use myStd() with sample=True
print('X Mean: ' +  str(xMean))
print('X Standard Deviation: ' + str(xStd))


# now we compute the mean and standard deviation of y
yMean = np.mean(y)
yStd = np.std(y)
print('Y Mean: ' +  str(yMean))
print('Y Standard Deviation: ' + str(yStd))



# plotting this would be a little bit dull, lets get to something 
# 'more' interesting: we use values from physics practical A, W1
# they are found in the assets/ directory, in a .csv - file (comma seperated value)
# every decent excel-like programme can output a file like that
# we could totally write our own parser for storing the values in an array-object,
# but there is already an excellent module for that
import csv
# now we initalize the ranges for the different parts of the graph
x1 = []
x2 = []
x3 = []

y1 = []
y2 = []
y3 = [] 

x = []
y = []


with open('assets/w1_values.csv') as openFile:
	csvreader = csv.DictReader(openFile)
	
	for row in csvreader:
		# here we insert the values into their respective ranges
		if int(row['t']) < 360:
			y1.append(float(row['T']))
			x1.append(float(row['t']))
		elif int(row['t']) < 660:
			y2.append(float(row['T']))
			x2.append(float(row['t']))
		else:
			y3.append(float(row['T']))
			x3.append(float(row['t']))

x = x1 + x2 + x3
y = y1 + y2 + y3

x1 = np.array(x1)
x2 = np.array(x2)
x3 = np.array(x3)
y1 = np.array(y1)
y2 = np.array(y2)
y3 = np.array(y3)

x = np.array(x)
y = np.array(y)

# lets do a linear regression:
# there is a numpy function for this, its called polyfit(). 
# its parameters are x,y and the degree of the fit function
m1, b1 = np.polyfit(x1, y1, 1)
m3, b3 = np.polyfit(x3, y3, 1)

# so we obtain two linear fit functions with the following parameters:
f = m1*x+b1
g = m3*x+b3

print('Linear Fit 1: ' + str(round(m1, 5)) + '*x+' + str(round(b1, 2)))
print('Linear Fit 2: ' + str(round(m3, 5)) + '*x+' + str(round(b3, 2)))

# this is a bar to visualize the center of the slope
yBar = np.linspace(23.5, 29.5, 30)
xBar = (330 + 660) / 2

# lets get the intersections of f,g with the slope
# we only have to evaluate f,g at x = xBar!

iSec1 = m1*xBar+b1
iSec2 = m3*xBar+b3


# lets add error bars to our plot:
# we assume to have a constant error of 0.1 °C in
# the temperature reading:
yerr = 0.1
plt.errorbar(x, y, yerr, capsize=3, ls='none') 
# the ls (linestyle) keyword argument fixed wierd behaviour



# plotting is straigtforward: you only define a plt.plot() function
# you actually can overload it
# the stuff in '' corresponds to a colour and a sign for the graph
plt.scatter(x, y, marker='+', color='r' ) # plotting x,y
plt.plot(x, f, '--k') # plotting f 
plt.plot(x, g, '-b') # plotting g
plt.plot([xBar for i in range(len(yBar))], yBar) # plotting the bar
plt.plot(xBar, iSec1, 'ro')
plt.plot(xBar, iSec2, 'ro')
# always label your axes!
plt.xlabel('t/s')
plt.ylabel('T/°C')
plt.title('first plot!')
plt.show()