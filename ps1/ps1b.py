#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:20:56 2021

@author: Katie
"""


annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter semi-annual salary raise as demical: "))

required_downpayment_percent = 0.25
portion_down_payment = required_downpayment_percent * total_cost

annual_return = 0.04 # this is r
monthly_return = annual_return / 12 # this is r / 12

current_savings = 0
num_of_months = 0

while current_savings <= portion_down_payment:
    
    current_savings += (annual_salary / 12) * portion_saved + current_savings * monthly_return
    
    num_of_months += 1
    
    if num_of_months % 6 == 0: 
        annual_salary += annual_salary * semi_annual_raise

print("Number of months:", num_of_months)