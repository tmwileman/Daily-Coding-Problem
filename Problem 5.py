# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:00:21 2019

@author: tmwil
"""

# Suppose you have two five sided dice. What is the 
# expected value of their product?  

# pseudo code
sides = number of sides on each die
num_die = number of dice

function(sides, num_die):
    sum each number in the range from 1 to sides
    divide the sum by the number of sides on each die then
    multiply by the total number of die
    return the resulting value

sides = 5
num_die = 2

# actual code
def dieEV (sides, num_die):
    die_sum = 0
    for i in range (1, sides + 1):
        die_sum = die_sum + i
    EV = (die_sum / sides) * num_die
    return EV