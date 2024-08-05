##Password Generator
import random
import string

n_list = [*range(0,11-1,1)]
up = list(string.ascii_uppercase)
low = list(string.ascii_lowercase)
l_list = up + low
s_list = list(string.punctuation)

num_numbers = 0
num_letters = 0
num_symbols = 0
num_all = 0

length = input("\nHow long would you like your password to be?\n"
              "(We recommend a minimum of 12 characters)\n")
while not length.isdigit():
  length = input("Please enter a valid number.\n")
  length = input("\nHow long should your password be?\n")
length = int(length)

while num_all < length:
  try:
    num_numbers = random.randint(2,length // 3)
    num_letters = random.randint(2,length - num_numbers)
    num_symbols = random.randint(2,length - num_numbers - num_letters)
    num_all = num_numbers + num_letters + num_symbols
  except ValueError:
    pass

r_num = []
pos = 0
while len(r_num) <= num_numbers-1:
  n = random.choice(n_list)
  r_num.insert(pos,n)
  pos = pos + 1
[str(n) for n in r_num]

r_let = []
pos = 0
while len(r_let) <= num_letters-1:
  n = random.choice(l_list)
  r_let.insert(pos,n)
  pos = pos + 1

r_sym = []
pos = 0
while len(r_sym) <= num_symbols-1:
  n = random.choice(s_list)
  r_sym.insert(pos,n)
  pos = pos + 1

x = 1
password = []
stage = r_num + r_let + r_sym
while x <= len(stage):
  n = random.choice(stage)
  password.insert(x,n)
  x = x + 1
password_str = ''.join(str(p) for p in password)

print(f"\nYour password is: {password_str}")