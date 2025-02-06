#A Random number is a number that is chosen from a range 
# in a way that is unpredictable.
#We have two types of random numbers:
#1. Pseudo-random numbers: These are generated by a computer
#2. True random numbers: These are generated by some physical process
#In this module, we will be dealing with pseudo-random numbers

from numpy import random #importing the random module from numpy

x = random.randint(100) #random.randint(Low (included), High=None (excluded), Size=None, dtype='int')
print(x) #prints a random number between 0 and 100

#Low and high can be specified with different bounds
x = random.randint(100, 200) #prints a random number between 100 and 200
print(x)

x = random.randint([1, 5, 7], 10)
print(x) #prints a random number between 1 and 10, 5 and 10, 7 and 10

x = random.randint([1, 10, 20], [10, 20, 30])
print(x) #prints a random number between 1 and 10, 5 and 20, 7 and 30

x = random.randint(100, size=(5)) #prints an array of 5 random numbers between 0 and 100
print(x)

#Size can be a int or tuple of ints
x = random.randint(10, size=(3, 5)) #prints a 2-D array of 3 rows and 5 columns
print(x)

#random.rand() returns a random float between 0 and 1
x = random.rand() #random.rand(d0, d1, ..., dn) the dimensions of the returned array should be specified
print(x) 

x = random.rand(5) 
print(x) 

x = random.rand(2, 3)
print(x)

#random.choice() returns a random element from an array
#random.choice(a, size=None, replace=True, p=None)
# a: 1-D array-like or int (if int, it is treated as np.arange(a))
# size: int or tuple of ints, optional
# replace: boolean, optional (True = sample with replacement, False = sample without replacement)
# p: 1-D array-like, optional (The probabilities associated with each entry in a, 
#   if not given the sample assumes a uniform distribution over all entries in a)

x = random.choice([3, 5, 7, 9])
print(x)

x = random.choice(5)
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 2))
print(x)

x = random.choice([0, 1, 2, 4, 5, 6], size=(2,3), replace=False) #You cannot sample more than the number of elements in the array
print(x)

# x = random.choice([0, 1, 2], size=(2,3), replace=False) #ValueError: Cannot take a larger sample than population when 'replace=False'
# print(x)

x = random.choice([0, 1, 2], size=(2,3), replace=True) #Replace=True allows you to sample more than the number of elements in the array
print(x)

x = random.choice([0, 1, 2], size=10, p=[0.1, 0.2, 0.7]) #p specifies the probability of each element
print(x)

#p is used for data distribution