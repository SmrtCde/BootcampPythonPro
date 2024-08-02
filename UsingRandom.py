import random

## flipping a coin
num = random.randint(1,100)
print(num)
flip = random.randint(1,100)
if flip % 2 == 0:
  print("Heads")
else:
  print ("Tails")

## who pays for lunch?
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
num = random.randint(0,len(names)-1)

print(f"The person who will pay the bill is...{names[num]}")