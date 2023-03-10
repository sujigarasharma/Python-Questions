weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = float(input("Enter your height in inches: "))

weight_kg = weight_pounds * 0.4536

height_m = height_inches / 39.37

bmi = weight_kg / (height_m ** 2)

print("Your BMI is:", round(bmi, 2))
