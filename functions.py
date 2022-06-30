# 1. Write a function named sum_tothat accepts a single integer, n,
# and returns the sum of the integers from 1 to n. For example:


def sum_to(n):
    nums = range(1, n+1)
    sum = 0
    for num in nums:
        sum += num
    return sum

# print(sum_to(6))


# 2. Write a function named largestthat takes a list of numbers as an 
# argument and returns the largest number in that list.

def largest(x):
    sum = 0
    for i in x:
        sum += i
    return sum

# print(largest([1,2,3,4,5]))


# 3. Write a function named occurancesthat takes two string 
# arguments as input and counts the number of occurances of 
# the second string inside the first string.


def occurances(str1,str2):
    matches = 0
    for char2 in str2:
        for char1 in str1:
            if(char1 == char2):
                matches += 1
    return matches

# print(occurances('dad','a'))

# 4. Write a function named product that takes an arbitrary number of 
# numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).


def product(*nums):
    product = 1
    for num in nums:
        product *= num
    return product

# print(product(2,2,4))


















# have to use the def key word
# def first_function():
#     pass

# #empty function returns None
# result = first_function()
# # print(result)


# # Like an arrow function
# # have to use the lambda key word

# nums = [1, 3, 2, 6, 5]
# odds = list( filter(lambda num: num % 2, nums) )

# print(odds)

# def add(a,b, *args):
#     argSum = 0
#     for arg in args:
#         argSum += arg
#     return a + b + argSum

# print(add(10, 20, 5, 5,5,5,5,5,5,5,5,5,5,5))

# def f(*args):
#     print(type(list(args)))
#     for arg in args:
#         print(arg)

# f(1,2,3)

# def dev_skills(dev_name, *skills):
#     dev = {'name': dev_name, 'skills': []}
#     for skill in skills:
#         dev['skills'].append(skill)
#     return dev

# print(dev_skills('jimmy','css','html','javascript'))

#args puts arguments into a tuple
#kwargs puts arguments into a dictionary

def dev_skills(dev_name, **kwargs):
    dev = {'name': dev_name, 'skills': {}}
    for skill, rating in kwargs.items():
        dev['skills'][skill] = rating
    return dev

# print(dev_skills('jimmy', html=5, css=2))
