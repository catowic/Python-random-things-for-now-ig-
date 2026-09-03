# calculating the intrest of money thing
balance = 0
rate = 0
time = 0

while True:
    balance = float(input("Enter your balance : "))
    if balance <= 0:
        print("You cant type 0 or negative numbers please try again . ")
    else:
        break

while True:
    rate = float(input("Enter your intress rate : "))
    if rate <= 0:
        print("You cant type 0 or negative numbers please try again . ")
    else:
        break

while True:
    time = float(input("Enter time in years : "))
    if time <= 0:
        print("You cant type 0 or negative numbers please try again . ")
    else:
        break

final = balance * pow( 1 + (rate/100) , time )

print(final)
