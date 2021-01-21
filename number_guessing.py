# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:09:26 2021

@author: Enes Zeybek
"""

import random
number = random.randint(1,9) 
while True:
    guess_number = int(input("Guess the number between 1-9: "))
    if guess_number == number:
        print("Exactly right well done")
        break
    elif guess_number < number:
        print("Too low try again")
    else:
        print("Too high try again")
