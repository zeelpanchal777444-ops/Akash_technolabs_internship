# game number if win number increase else decrese

import random

score = 0
chance = 5

print("_______________Number Guess Game (1 to 5)_______________")
print("~~~~~~~~~~~~You have only 5 chance~~~~~~~~~~~~~")
print()


for i in range(chance):
    computer = random.randint(1,5)
    
    user = int(input(f"Enter the number b/w (1 to 5) {i+1} : "))
    
    if user < 1 or user > 5:
        print("Number must be in 1 to 5")
        continue
    print("Computer choose :",computer)
    
    if user == computer:
        score+=1
        print("Won !!")
        
    else:
        score-=1
        wrongscore = score - 1
        print("Wrong")
        print("Current score : ",score)
        
print("\n")
        
print("~ ~ ~ ~ ~ ~ Game over ~ ~ ~ ~ ~ ~")
print("Final score : ",score)