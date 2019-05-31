# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:10:21 2019

@author: tmwil
"""

# This problem was asked by Jane Street.
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the 
# first and last element of that pair. For example, car(cons(3, 4)) 
# returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.
# We will be sending the solution tomorrow, along with tomorrow's 
# question. As always, feel free to shoot us an email if there's 
# anything we can help with.
# Have a great day!

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)