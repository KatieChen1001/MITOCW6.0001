#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:37:47 2021

@author: Katie
"""
import numpy

while True:
    try: 
        # Get user input and convert to integer
        x = int(input ("Enter a number x to be the base number: "))
        break
    except:
        # Catch errors if user did not enter an integer, prompt them again
        print("Please enter an integer")

while True:
    try: 
        # Get user input and convert to integer
        y = int(input ("Enter a number y to be the power: "))
        break
    except:
        # Catch errors if user did not enter an integer, prompt them again
        print("Please enter an integer")

raised = x ** y 

print(x, "raised to the power of", y, "is", raised)

print("The log (base 2) of", x, "is", int(numpy.log2(x)))
