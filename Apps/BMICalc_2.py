weight = input("Please enter your weight, in lbs: ")
height = input("Please enter your height, in inches: ")

BMI = round(703 * int(weight) / int(height) ** 2)
if BMI < 18.5:
  print(f"Your BMI is {BMI}, and you are underweight.")
elif BMI >= 18.5 and BMI < 25:
  print(f"Your BMI is {BMI}, and you have a normal weight.")
elif BMI >= 25 and BMI < 30:
  print(f"Your BMI is {BMI}, and you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
  print(f"Your BMI is {BMI}, and you are obese.")
else:
  print(f"Your BMI is {BMI}, and you are clinically obese.")