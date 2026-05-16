# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 16:30:00 2026

@author: avams
"""

import random
randnumber=random.randint(1,100)
Guess=0
userGuess=None
while (randnumber != userGuess):
    try:
        userGuess=int(input("enter your choice:\n"))
        Guess+=1
        if randnumber==userGuess:
            print("your guessed it Right")
        else:
            if randnumber<userGuess:
                print("you entered Wrong! plz guess smaller number")
            elif randnumber>userGuess:
                print("you entered Wrong! plz guess higher number")
    except ValueError:
        print("Invalid Input Enter a Number")
with open("hiscore.txt",'r') as f:
    hiscore=int(f.read())
    
if Guess<hiscore:
    with open("hiscore.txt",'w') as f:
        f.write(str(Guess))
    print(f"New Highest Score in {Guess} guesses")
else:
    print(f"you have just missed the high score, you guessed in {Guess} guesses")
    