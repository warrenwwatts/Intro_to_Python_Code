# -*- coding: utf-8 -*-
"""
This is a script to get hours and pay rate from the user,
calculate the total pay and print it out.
"""
# function to calculate pay 
def calc_pay(hrs,wage=15.0):
    """
    calc_pay() takes hrs and wage as inputs and returns
    the pay for the week.
    """
    if hrs <= 40:
        pay = hrs * wage
        #print("no overtime")
    else:
        pay = hrs * wage + (hrs - 40.0) * wage * 0.5
        #print("you got overtime", hours-40, "hours")
    return pay

def get_float(query):
    """
    get_float takes str query as input, 
    returns a float value from input
    """
    value_str = input(query)
    try: 
        value_float = float(value_str)
    except:
        #print("Not a valid number, setting  to 0")
        #value_float = 0.0
        value_float = get_float("Not a valid number, Try again: ")
    return value_float

    
# get hours and rate using get_float()
hours = get_float("Hours: ")
rate = get_float("Rate: ")

# print pay
print("Pay: ", calc_pay(hrs=hours,wage=rate))





"""def print_args(*args, **kwargs):
    print(args)
    print(kwargs)
    
print_args("hello", 1, 2, key="there", mama=2)
"""