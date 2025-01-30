# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:32:15 2025

@author: richs
"""

import random
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')

correct_after = 0
incorrect_after = 0

correct = 0
incorrect = 0

experiments = 100000

# Step 3: Check if we guessed the correct door
for i in range(experiments):
    doors = [False, False, False]  # Initially all False
    winning_index = random.choice([0, 1, 2])  # Randomly pick the index of the 'winning' door
    doors[winning_index] = True
    choice_index = random.choice([0, 1, 2])
    if doors[choice_index]:
        correct +=1
    else:
        incorrect += 1



# Repeat experiment many times:
for i in range(experiments):
    # Step 1: Randomly set exactly one door as the winner
    doors = [False, False, False]
    winning_index = random.choice([0, 1, 2])
    doors[winning_index] = True

    # Step 2: Choose one door at random
    choice_index = random.choice([0, 1, 2])

    # ---- Monty reveals a losing door (that is neither the winning door nor your chosen door) ----
    # Collect all doors that are not winning and not chosen:
    possible_doors_to_open = [idx for idx in [0,1,2] 
                              if idx != winning_index and idx != choice_index]
    # Monty reveals (removes) one such door:
    opened_door = random.choice(possible_doors_to_open)

    # ---- Switch your choice to the remaining door ----
    # The remaining door is the one that is not your current choice and not the opened door:
    new_choice_index = next(idx for idx in [0,1,2]
                            if idx not in [choice_index, opened_door])

    # Step 3: Check if, after switching, you have the winning door
    if doors[new_choice_index]:
        correct_after += 1
    else:
        incorrect_after += 1

# Summarize results
total = correct + incorrect
ctpct = correct / total
ictpct = incorrect / total
y = np.array([correct, incorrect])
labels = [f'Correct {ctpct:.3f}', f'Incorrect {ictpct:.3f}']


total_after = correct_after + incorrect_after
ctpct_after = correct_after / total_after
ictpct_after = incorrect_after / total_after
y_after = np.array([correct_after, incorrect_after])
labels_after = [f'correct_after {ctpct_after:.3f}', f'Incorrect_after {ictpct_after:.3f}']

plt.figure()
plt.pie(y, labels=labels, autopct='%.1f%%')
plt.title("Results before Switching")
plt.tight_layout()
plt.legend(loc = 2)
plt.show()


plt.figure()
plt.pie(y_after, labels=labels_after, autopct='%.1f%%')
plt.title("Results after Switching")
plt.tight_layout()
plt.legend(loc = 1)
plt.show()
