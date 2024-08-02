year = int(input("Enter a year: "))
while len(str(year)) != 4:
  year = int(input("Please enter a 4-digit year!\n"))

if year % 4 == 0 and (year % 100 == 0 or year % 400 == 0):
  print("Leap year.")
else:
  print("This is not a Leap Year")