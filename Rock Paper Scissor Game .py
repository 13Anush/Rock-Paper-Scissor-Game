#!/usr/bin/env python
# coding: utf-8

# In[6]:


#ROCK PAPER SCISSORS GAME USING PYTHON LANGUAGE 

import random

# Rock Paper Scissors game 
def gameWin(computer, you):
    # If two values are equal, declare a tie!
    if computer == you:
        return None

    # Check for all possibilities when computer chose r
    elif computer == 'r':
        if you=='p':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose p
    elif computer == 'p':
        if you=='s':
            return False
        elif you=='r':
            return True
    
    # Check for all possibilities when computer chose s
    elif computer == 's':
        if you=='r':
            return False
        elif you=='p':
            return True

print("Computer Turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    computer = 'r'
elif randNo == 2:
    computer = 'p'
elif randNo == 3:
    computer = 's'

you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")
a = gameWin(computer, you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")


# In[ ]:




