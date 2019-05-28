# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:30:15 2019

@author: tmwil
"""

# Good morning! Here's your coding interview problem for today.
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at 
# index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

import numpy as np

array = np.array([1, 2, 3, 4, 5])

new_array = []

for i in array:
    new_array.append(np.prod(array) / i)

print(new_array)
