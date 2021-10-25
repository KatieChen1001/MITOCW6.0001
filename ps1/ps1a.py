#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:54:46 2021

@author: Katie
"""

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25 * total_cost

annual_return = 0.04 # this is r
monthly_return = annual_return / 12 # this is r / 12

monthly_saved = (annual_salary / 12) * portion_saved

current_savings = 0
num_of_months = 0

while current_savings <= portion_down_payment:
    
    current_savings += monthly_saved + current_savings * monthly_return
    
    num_of_months += 1

print("Number of months:", num_of_months)