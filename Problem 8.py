# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:02:47 2019

@author: tmwil
"""

# The cincy sequence is a recursively defined sequence as 
# follows. The base cases cincy(1), cincy(2) and cincy(3) are equal to 
# 1. Any other cincy number is defined as the cincy number two before 
# it added to the cinci number three before it multiplied by 2. That is 
# to say cincy(i) = cincy(i-2) + 2 * cincy(i-3). Cincy(4) and cincy(5) 
# = 3, cincy(6) = 5, cincy(7) = 9 and so on. For this problem write 
# code that will help you compute the 25th cincy number. 
    
# pseudo code

def array (x):
    if x <= 3 (our base case):
        return 1
    else:
        recursive function enabling us to calculate the answer
    return the answer
    
# actual code

def cincyNum(cincy):
    if cincy <= 3:
        return 1
    else:
        return (cincyNum(cincy - 2) + 2 * cincyNum(cincy - 3))