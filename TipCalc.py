print("Welcome to the tip calculator!")
totbill = input("What was the total bill? $ ")
tipRate = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

totbill = float(totbill)
tipRate = float(tipRate)
people = int(people)

print(f"Each person should pay: ${round(totbill + (totbill * tipRate / 100),1) / people}")