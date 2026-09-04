# guess a number 
# see if any of this number is true
# and if its biger or smaller then this number
# then repeat until you find it
import random

number = str(random.randint(10000,99999))
numfind = ["_","_","_","_","_"]
truenumbers = []
iswon = False
tries = 0

while iswon == False:
    print(f"{numfind[0]} {numfind[1]} {numfind[2]} {numfind[3]} {numfind[4]}")
    guess = input("Please write a number : ")
    tries += 1
    for x in range(5):
        if guess[x] == number[x]:
            numfind[x] = number[x]
            if guess[x] in truenumbers:
                truenumbers.remove(guess[x])
        elif guess[x] in number:
            if guess[x] not in truenumbers:
                truenumbers.append(guess[x])

    if guess == number:
        print("You won")
        iswon = True
    elif guess < number:
        print("Your guess is bigger than the number")
    elif guess > number:
        print("Your guess is smaller than the number")

    print(" ")
    print(f"{numfind[0]} {numfind[1]} {numfind[2]} {numfind[3]} {numfind[4]}")
    print("Correct numbers, wrong positions:", truenumbers)
    print(" ")

print("You won ! ")
print(f"It took {tries} attemps")








