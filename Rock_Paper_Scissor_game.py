# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 19:40:32 2025

@author: avams
"""

import random

def rockPaperScissor(computer,you):
    if computer==you:
        return None
    elif computer=='R':
        if you=='P':
            return True
        elif you=='S':
            return False
    elif computer=='P':
        if you=='S':
            return True
        elif you=='R':
            return False
    elif computer=='S':
        if you=='R':
            return True
        elif you=='P':
            return False
print("computer turn:Rock(R) Paper(P) Scissor(S)?") 
randno=random.randint(1,3)
if randno==1:
    computer='R'
elif randno==2:
    computer='P'
elif randno==3:
    computer="S"  
you=input("your turn:Rock(R) Paper(P) Scissor(S):\n")
a=rockPaperScissor(computer,you)
print(f"computer choose:{computer}")
print(f"your choose:{you}")    
if computer==you:
    print("its a tie")
elif a:
    print("you won")
else:
    print("you loose")    
       