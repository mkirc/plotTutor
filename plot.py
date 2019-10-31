# this is a comment in python
# everything following a '#' will not be interpreted by the python interpreter

# following are 'imports', they include some foreign code in your code.
# this code is called a package, and is subdivided in modules

# numpy (numerical python) is a package for scientific data manipulation
import numpy as np

# matplotlib is *the* stadard plotting package. 
# it integrates well with numpy,but there are many more
import matplotlib.pyplot as plt

# random is a package for, well generating random numbers,
# or picking random entries in a list.
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


# lets do a linear regression:
# there is a numpy function for this, its called polyfit(). 
# its arguments are x, y, and the exponent of the fit-function
m,b = np.polyfit(values[0], values[1], 1) 

plt.plot(x, y, 'ro', x, m*x+b, '--k')
# plt.plot(x, x, label='linear')
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend('Legend')

plt.show()