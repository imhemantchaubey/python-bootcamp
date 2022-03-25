import random

dice_nos = []

for i in range(1, 7):
   for j in range(1, 7):
      dice_nos.append((i, j))
      
choice = random.choice(dice_nos)
print(f"You got: {choice}")