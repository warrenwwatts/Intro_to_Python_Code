# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:35:19 2018
file for strings chapter
@author: warren watts
"""
# different ways to loop through a string
# will work with lists too.
fruit = "banana"
index = 0
while index < len(fruit):
    char = fruit[index]
    print(char)
    index += 1
print()

# for loop with index
for index in range(len(fruit)):
    char = fruit[index]
    print(index, char)
print()
    
# for loop with iteration through string
for char in fruit:
    print(char)
print()

# for loop with enumerate
for index,char in enumerate(fruit):
    print(index,char)
print()
    
# different ways to print fruit backward a letter at a time

# printing fruit backward with while
index = len(fruit) - 1
while index >= 0:
    print(fruit[index])
    index = index - 1
print()

# using for loop indexed
for index in range(len(fruit)-1,-1,-1):
    print(index, fruit[index])
print()

# using for loop indexed with negative indexing
for index in range(-1,-(len(fruit)+1),-1):
    print(index, fruit[index])
print()

# iterating string with the for loop and reversed
for char in reversed(fruit):
    print(char)
print()

# iterating string with the for loop and slicing
for char in fruit[::-1]:
    print(char)
print()

nirvana = "     .Come as you are,, as   you were, \nas I want you to be...   \n"
nirvana
print(nirvana)

# string functions and methods
# len()
len(nirvana)

# string.upper() and string.lower()
nirvana.lower()
nirvana.upper()

# string.strip() methods
nirvana.lstrip()
nirvana.rstrip()
nirvana.strip()
nirvana.strip().strip(".")

# string.startswith() and string.endswith()
print(nirvana.startswith(".Come"))
print(nirvana.lstrip().startswith(".Come"))
print(nirvana.endswith("be..."))
print(nirvana.rstrip().endswith("be..."))

# find and replace
nirvana.find("you")
nirvana.find("you", 15)
nirvana.find("you", 30)
nirvana.replace("you", "they")

# string.is____ methods
test = "AAAABBB"
test.isupper()
test.isalpha()
test.isalnum()
test.islower()
test.lower().islower()
test.isdecimal()
test.isdigit()
test.isnumeric()


test = "1234"
test.isalpha()
test.isalnum()
test.isdecimal()
test.isdigit()
test.isnumeric()

test = "123.321"
test.isalpha()
test.isalnum()
test.isdecimal()
test.isdigit()
test.isnumeric()
test.replace(".","1",1).isdigit()
test = "1234."
test.replace(".","1",1).isdigit()
float(test)


# string.split() method
word_list = nirvana.split()
print(word_list)
phrase_list = nirvana.split(",")
print(phrase_list)

# string.join() method
nirvana2 = " ".join(word_list)
print(nirvana2)

# string formatting using %
# variables
camels = 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
print(camels)

# variables with spacing 
camels = 'In %5d years I have spotted %5g %10s.' % (3, 0.1, 'camels')
print(camels)

camels = 'In %5d years I have spotted %5.2f %10s.' % (3, 0.1, 'camels')
print(camels)

# variables that are larger than the spacing
camels = 'In %5d years I have spotted %5.2f %10s.' % (3000000, 700.1, 'camelbearpigs')
print(camels)

