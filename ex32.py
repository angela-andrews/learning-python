# Loops and Lists
the_count = [1,2,3,4,5]
fruits = ['apples','oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes throug a list

for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists. First, start with an empty one
elements = []

# then, use the range function to do 0 to 5 counts

for i in range(0,6):
    print(f"Adding {i} to the list")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")


# Range Function:
# Range is a sequence type like list and tuple are
# an immutable sequence of numbers and is commonly used for looping a sepcific number of times in for loops
# range(start, stop, [step])
# step is optional and defaults to 1
# if start is omitted, the default is 0
# Range examples:
"""
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]

"""
# Line 25 didn't need a loop to print.
# Avoided the for-loop and assigned the range to elements2 and printed
elements2 = []
elements2 = list(range(6))
print(elements2)

# =======================Notes========================
# list is another sequence type
# list([iterable])  see above
# make a list different ways

# [] empty list
# [a,b,c] assign values to a list. strings in quotes 
# list comprehension 
# type constructor list() or list(iterable)
# https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/
# https://www.datacamp.com/community/tutorials/python-list-comprehension
# https://www.geeksforgeeks.org/reduce-in-python/
 # https://www.geeksforgeeks.org/filter-in-python/
# https://www.geeksforgeeks.org/python-map-function/
# jupyter-lab 
# instead jupyter-notebook 
 # Python map() function
#map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

#Syntax :

#map(fun, iter)