# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:35:32 2019

@author: tmwil
"""

# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer 
# in linear time and constant space. In other words, find the lowest 
# positive integer that does not exist in the array. The array can 
# contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input 
# [1, 2, 0] should give 3.
# You can modify the input array in-place.
# We will be sending the solution tomorrow, along with tomorrow's 
# question. As always, feel free to shoot us an email if there's 
# anything we can help with.
# Have a great day!


list = [3, 4, -1, 1]

new_list = []

for i in list:
    if i >= 0:
        new_list.append(i + 1)
    print(min(new_list))