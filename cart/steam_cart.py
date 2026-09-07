# basic cart program
# that helps for learning python dictionaries
games = {"terraria": 2.89,
         "rdr2": 14.99,
         "astroneer": 3.74,
         "dayz": 24.99}

cart = []
total = 0

for key, value in games.items():
    print(f"{key:12} : {value:.2f}")

while True:
    game = input("Select an item (q to quit) : ").lower()
    if game == "q":
        break
    elif games.get(game) is not None:
        cart.append(game)
    else:
        print("Game doesnt exist.")

for x in cart:
    total += games.get(x)
    print(x, end=" ")

print(f"\nTotal is ${total:.2f}")
