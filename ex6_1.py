# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:33:59 2018
Code for Exercise 8.1
with some examples list methods
@author: warren watts
"""
# list comprehension example:
# simplest version is [<expression> <for loop>]
# generates a list
a = [i*3 for i in range(7)]

# equivalent code
b = list()
for i in range(7):
    b.append(i*3)


# function to remove first and last item of list
def chop(lst_in):
    del lst_in[0]
    lst_in.pop()
    return 

# function to return a copy of the list with first and last item
# removed
def middle(lst_in):
    return lst_in[1:-1] # or lst_in[1:len(lst_in)-1]

print(a)
print(b)
chop(a)
print(a)
print(middle(a))
print(a)

# show built in list functions -
print(dir(b))

# use list.index() to find index of item in list
print("6 is at index:", b.index(6))

# use list.append(<item>) to add item to end of list
b.append(6)
print(b)

# use list.insert(<index>, <item>) to add item at a index location
b.insert(4, 6)
print(b)

# use list.remove to remove item by value, only removes first occurance
b.remove(6)
print(b)

# use list.pop() to remove last item or item at index, list.pop()
# returns item removed
print(b.pop())
print(b)
c = b.pop(1)
print(c, b)

# can also use operator del to remove an item
# example using index to find the item to remove
del b[b.index(18)]
print(b)