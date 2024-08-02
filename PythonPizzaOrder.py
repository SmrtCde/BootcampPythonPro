print("Welcome to Python Pizza!\nAvailable Sizes:\nS - $15\nM - $20\nL - $25\n")
s = input("What size pizza would you like?: ")

size = s.upper()
topping = 0
cheese = 0
price = 0

while price == 0:
  if size == "S":
    price += 15
  elif size == "M":
    price += 20
  elif size == "L":
    price += 25
  else:
    s = input("You've entered an invalid size, please try again:")
    size = s.upper()

pepperoni = input("Would like you add peporoni for $2.00? Y or N\n: ")
pepperoni = pepperoni.upper()
if pepperoni == "Y":
  topping += 2 if size == "S" else 3

exCheese = input("Would you also like to add extra cheese for $1.00? Y or N\n: ")
exCheese = exCheese.upper()
if exCheese == "Y":
  cheese += 1

total = price + topping + cheese
print(f"Thank you. Your total is ${total}")