# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:05:20 2018
Solution to 5.1
Takes numeric input until "done" is entered and then calculates
sum, number of entries and average
@author: warren watts
"""

# set up count and total
count = 0
total = 0

# Infinite loop
while True:
    response = input("Enter a number or done: ")
    # if input is not done, try to convert to float
    if response != "done":
        try:
            number = float(response)
        except:
            # print "invalid input" if it can't be converted to float and
            # continue (skip rest of this pass through loop and loop again)
            print("Invalid input")
            continue
    # else break (exit loop), as input == "done"
    else:
        break
    # add 1 to count and number to total
    count += 1
    total += number

#print sum, number of entries and average
print(total, count, total/count)

