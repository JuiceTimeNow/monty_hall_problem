# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:37:52 2025

@author: richs
"""

import random
import matplotlib.pyplot as plt
import numpy as np
from Monty_Hall_Simulation_Multiple_func import run

plt.close('all')

x = 3
answers = {}


doors = [3,4,5,6,7,8,9,10,11,12,13,14,15]
for door in doors: 
    correct_before, correct_after, pct_change, pct_multiple = run(door)
    answers[door] = [correct_before, correct_after, pct_change, pct_multiple]
    
win_change = [value[2] for value in answers.values()]
win_mult = [value[3] for value in answers.values()]

plt.figure()
plt.plot(doors, win_mult, label = '% more winning after change')
plt.plot(doors, win_change, label = 'Change in winning frequency')
plt.xlabel('Number of doors')
plt.ylabel ('Win Mult %')
plt.legend()
plt.grid()
plt.show()