# def greet():
#   print("Hello")
#   print("How do you do?")
#   print("Isn't the weather nice today?\n")

# greet()

######################################################
"""
# def greet_w_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")
#   print(f"Isn't the weather nice today {name}?\n")

# greet_w_name("Ben")
"""
######################################################
"""
def greet_w_name_location(name, location):
	print(f"Hello {name}")
	print(f"What can you tell me about {location}?\n")

greet_w_name_location("Ben", "London")
"""

######################################################
#  Positional Arguments
######################################################
"""
def my_function(a, b, c):
	print(a)
	print(b)
	print(c)

my_function(1, 2, 3)
a=1
b=2
c=3

my_function(3,1,2)
a=3
b=1
c=2
"""

######################################################
#  Keyword Arguments
######################################################
"""
def my_function(a, b, c):
	print(a)
	print(b)
	print(c)

my_function(a=1, b=2, c=3)
a=1
b=2
c=3


# with the keyword arguments, the order of the arguments does not matter
my_function(b=2, c=3, a=1)
a=1
b=2
c=3
"""

######################################################
# Paint Are Calculator
######################################################
"""
def paint_calc(height, width, cover):
	num_cans = (height * width) / cover
	num_cans = 1 if num_cans < 1 else num_cans
	print(f"You'll need a minimum of {round(num_cans)} can(s) of paint.")

he = int(input("Please enter the height of your wall, in ft: "))
le = int(input("Please enter the length of your wall, in ft: "))
co = int(input("Please enter the coverage your paint can cover, in ft: "))

paint_calc(he,le,co)
"""

######################################################
# Prime Numbers Checker
######################################################
"""
number = int(input("Enter a number to check prime-status: "))

def num_checker(num):
	factors = []
	for i in range(2, num):
		if num % i == 0:
			factors.append(i)
	if sum(factors) == num:
		print("Your provided number is a prime.")
	else:
		print(f"Your number is not a prime, and is divisible by {factors}.")

num_checker(number)
"""