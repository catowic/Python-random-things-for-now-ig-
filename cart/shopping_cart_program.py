# basic shopping cart program
# you can write foods 
# and their prices
# then you can see the items and total 
foods = []
prices = []
total = 0
print()

while True:
    food = input("enter a food to add cart (Q to quit) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of {food} : "))
        foods.append(food)
        prices.append(price)

print("/-------Cart-------/")

for x in foods:
    print(x, end=" ")

for price in prices:
    total += price
    
print(f"\nYour total is {total:02}")
