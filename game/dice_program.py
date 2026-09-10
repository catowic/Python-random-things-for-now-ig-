import random

dices = {1:("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
         2:("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
         3:("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
         4:("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
         5:("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
         6:("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")}

dice = []
total = 0
num_of_dice = int(input("Enter dice count : "))

for _ in range(num_of_dice):
   dice.append(random.randint(1,6))

for line in range(5):
   for die in dice:
      print(dices.get(die)[line], end=" ")
   print()

for die in dice:
   total += die

print(f"\nTotal : {total}")
