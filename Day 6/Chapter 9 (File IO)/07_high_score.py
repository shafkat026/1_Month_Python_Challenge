# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.

import random

def game():
    score =random.randint(0,999)
    
    with open("Hi-score.txt") as f:
        hiscore = f.read().strip()
        if(hiscore!=""):
             hiscore= int(hiscore)
        else:
             hiscore=0

    print(f"Your Score is {score}")
    print(f"Previous High Score is {hiscore}")


    if(score>hiscore):
        print("🎉 New High Score!")
        with open("Hi-score.txt", "w") as f:
             f.write(str(score))
    
    return score

game()