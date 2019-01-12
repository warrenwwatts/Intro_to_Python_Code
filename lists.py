# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:32:35 2018

@author: warren watts
"""

from copy import deepcopy


# ways to copy a list
numbers = [10.0, 14.4, 17.7, 16.8, [22,55]]
numbers2 = numbers
numbers3 = numbers.copy()
numbers4 = list(numbers)
numbers5 = numbers[:]
numbers6 = deepcopy(numbers)

print(numbers)
print(numbers2)
print(numbers3)
print(numbers4)
print(numbers5)
print(numbers6)
print()

numbers[0] = 7.7
print(numbers)
print(numbers2)
print(numbers3)
print(numbers4)
print(numbers5)
print(numbers6)
print()

numbers3[4] = [77, 22]
numbers2[4][0] = "hi"
print(numbers)
print(numbers2)
print(numbers3)
print(numbers4)
print(numbers5)
print(numbers6)
print()

numbers3[1] = "changed"
numbers4[2] = "changed"
numbers5[3] = "changed"

print(numbers)
print(numbers2)
print(numbers3)
print(numbers4)
print(numbers5)
print(numbers6)
print()

# print(dir(numbers))