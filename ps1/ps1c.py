#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:54:20 2021

@author: Katie
"""

annual_salary = float(input("Enter your starting annual salary: "))
semi_annual_raise = 0.07

total_cost = 1000000
required_downpayment_percent = 0.25
portion_down_payment = required_downpayment_percent * total_cost

annual_return = 0.04 # this is r
monthly_return = annual_return / 12 # this is r / 12

target_months = 36

steps = 0

upper_portion_saved = 10000
lower_portion_saved = 0

                 
def calc_portion_saved (upper_portion_saved, lower_portion_saved):
    
    portion_saved = (upper_portion_saved + lower_portion_saved) / 2 
    
    return portion_saved

def calc_savings(target_months, annual_salary, portion_saved, monthly_return, semi_annual_raise):
    """
    
    """
    current_savings = 0
    num_of_months = 0
    
    while num_of_months < target_months:
        current_savings += (annual_salary / 12) * (portion_saved / 10000) + current_savings * monthly_return
        num_of_months += 1 
        
        if num_of_months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
    
    return current_savings

max_savings = calc_savings(target_months, annual_salary, upper_portion_saved, monthly_return, semi_annual_raise)
if max_savings < portion_down_payment: 
    print("Sorry dude, you just can't save enough within the target months")

portion_saved = calc_portion_saved(upper_portion_saved, lower_portion_saved)
my_savings = calc_savings(target_months, annual_salary, portion_saved, monthly_return, semi_annual_raise)

while abs(my_savings - portion_down_payment) > 100: 
    
    if my_savings < portion_down_payment: 
        lower_portion_saved = portion_saved
    else:
        upper_portion_saved = portion_saved
        
    portion_saved = calc_portion_saved(upper_portion_saved, lower_portion_saved)

    my_savings = calc_savings(target_months, annual_salary, portion_saved, monthly_return, semi_annual_raise)

    steps += 1 
    
print("Save this percentage of your salary every month:", portion_saved/10000)
print("Number of steps:", steps)