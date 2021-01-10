# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:09:26 2021

@author: Enes Zeybek
"""

import numpy as np
number = np.random.randint(1,10)
checking = True 
while checking:
    guess_number = int(input("Guess the number between 1-9: "))
    if guess_number == number:
        print("Exactly right well done")
        checking = False
    elif guess_number < number:
        print("Too low try again")
    else:
        print("Too high try again")