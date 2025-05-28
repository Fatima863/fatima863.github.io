# Beginner level practice of higher order functions 

from functools import reduce
# Description: Python program that takes numbers and double them using higher order functions

def doubles (x):
    return x*x
numbers = [1,2,3,4,5,6,7,8,9,10]
double = list(map(doubles, numbers))
print(double)

# Description: Python program that filters even numbers

def evens (x):
    if x%2 == 0:
        return x
numbers = [1,2,3,4,5,6,7,8,9,10]
filtered_list = list(filter(evens, numbers))
print(filtered_list)

# Description: Python program that prints sum using higher order functions

def sum(x,y):
    return x+y
numbers = 1,2,3,4,5,6,7,8,9,10
summation = reduce(sum, numbers)
print(summation)

# Description: Python program that adds prefixes

names = ['Ali', 'Hassan', 'Hussain']
prefix = "Mr","Mr","Mr"
full_name = list(zip(prefix,names))
print(str(full_name))

# Description: using filter function

def four_letters(x):
    if len(x) < 7:
        return x
fruits = ['Apple','mango','orange','grapes','watermelon','cherry']
filtered_list = list(filter(four_letters, fruits))
print(filtered_list)
