# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:36:13 2021

@author: Enes Zeybek
"""

a = "rock"
b = "paper"
c = "scissors"
user1 = str(input("User1: "))
user2 = str(input("User2: "))

def play_game(u1,u2):
    if u1 == u2 :
        print("Draw")
        
    elif u1 == a and u2 == b:
        print(user2 + " win")
        
    elif u1 == b and u2 == a:
        print(user1 + " win")
        
    elif u1 == a and u2 == c:
        print(user1 + " win")
        
    elif u1 == c and u2 == a:
        print(user2 + " win")
        
    elif u1 == b and u2 == c:
        print(user2 + " win")
        
    elif u1 == c and u2 == b:
        print(user1 + " win")
    
    else:
        print("You must write : rock, paper or scissors")
        
u1 = str(input(user1 + ": "))
u2 = str(input(user2 + ": "))
play_game(u1,u2)