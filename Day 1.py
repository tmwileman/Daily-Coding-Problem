# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:52:53 2019

@author: tmwil
"""
# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

nums = [10, 15, 3, 7]
k = 17

def sum_of_some_nums (nums, k):
    for x in nums:
        for y in nums:
            if k - x == y:
                print("True", x, y)
            else:
                print("False", x, y)

sum_of_some_nums(nums, k)
