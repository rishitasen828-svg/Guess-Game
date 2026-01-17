#Creating Guess Game in Python using Random Module
#Rishita Sen,25BEE091
import random
random_num=random.randint(1,10)
print("You have 3 chances to guess the Digit")
chances=3
play=1
while play<=chances:
    choice=int(input("Enter the Digit you guessed->"))
    if(choice==random_num):
        print("You won!!Congo!!")
    else:
        print("You lost.Better luck next time")    
    play+=1 
if play>chances:
    print("Chances are over")
