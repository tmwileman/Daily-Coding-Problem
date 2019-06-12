# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:01:07 2019

@author: tmwil
"""

# You know that after the game 70% of fans in stand B are 
# happy and 50% of fans in stand A are happy. You know that Stand A 
# has an average attendance of 7,500 and stand B has an average 
# attendance of 2,500. What is the chance that a fan was in stand A 
# given that they were happy? 
    
# pseudo code
Std_A_Att = Stand A attendance
Std_B_Att = Stand B attendance
Std_A_Sat = Percent of happy stand A fans
Std_B_Sat = Percent of happy stand B fans

function (Std_A_Att, Std_A_Sat, Std_B_Att, Std_B_Sat):
    Sum the total fans at the game
    Calculate the probability that a fan was in stand A
    Calculate the probability that a fan was was happy
    Use Bayes theorem to calculate the probability that a fan was in section A given that they were happy
    return the resulting value

# actual code
Std_A_Att = 7500
Std_B_Att = 2500
Std_A_Sat = .7
Std_B_Sat = .5

def probAgivenHappy (Std_A_Att, Std_A_Sat, Std_B_Att, Std_B_Sat):
    total = Std_A_Att + Std_B_Att
    probA = Std_A_Att / total
    probHappy = (Std_A_Sat * Std_A_Att + Std_B_Sat * Std_B_Att) / total
    AgivenHappy = (Std_A_Sat * probA / probHappy)
    return AgivenHappy