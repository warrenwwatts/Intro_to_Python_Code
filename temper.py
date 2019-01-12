# -*- coding: utf-8 -*-
"""
This is a script to get hours and pay rate from the user,
calculate the total pay and print it out.
"""
# get temp in C from input, convert to int
tempc_str = input("Temperature in C: ")
tempc = float(tempc_str)

# calculate temp F
tempf  = tempc * (9/5) + 32

# print tempf
print("Temp in Farenhiet", tempf, "F")
print()







