# learning random but there is a twist 
# if you saw this code you need to play it and win it 
# good luck
import random

options = ("rock","paper","scissors")
player = None
compscore = 0
playerscore = 0
playin = True

while True:
    computer = random.choice(options)
    player = input("Rock paper scissors (q to quit): ").lower()
    if player == "q":
        break
    while player not in options :
        print("invalid")
        player = input("Rock paper scissors : ")

    if player == computer:
        print("Tie")
    elif player == "paper" and computer == "rock":
        print("Win")
        playerscore += 1
    elif player == "rock" and computer == "scissors":
        print("Win")
        playerscore += 1
    elif player == "scissors" and computer == "paper":
        print("Win")
        playerscore += 1
    else:
        print("Lose")
        compscore += 1

print(f"You : {playerscore} \nComp : {compscore}")
