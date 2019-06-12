# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:01:59 2019

@author: tmwil
"""

# Assume you have a list of numbers. Write a program that 
# outputs the numbers closest to the 25th and 75th percentile in the 
# data. If there are two numbers identically close, assume the length 
# of the list is divisible by 4. Sample input list of numbers [1 … 20]. 
# Output 5, 15. 
    
# pseudo code
numlist = list of numbers

function (list):
    Calculate the length of the list
    Sort the list from lowest to highest
    Calculate an index representing half of the length of the list
    Calculate another index representing a quartile
    Write a function that calculates the first quartile
    Write a function that calculates the third quartile
    Print the outputs from these two functions
    
# actual code
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def Q1andQ3 (numlist):
    listlen = len(numlist)
    numlist = list.sort(numlist)
    index = listlen // 2
    quartile = index // 2
    def Q1 (numlist, listlen, quartile):
        if (listlen % 2):
            return numlist[quartile]
        else:
            return (numlist[quartile] + numlist[quartile + 1]) / 2    
    def Q3 (numlist, listlen, quartile):
        if (listlen % 2):
            return numlist[median + quartile]
        else:
            return (numlist[median + quartile] + numlist[quartile + quartile + 1]) / 2   
    print (Q1, Q3)