# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:52:53 2019

@author: tmwil
"""

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
