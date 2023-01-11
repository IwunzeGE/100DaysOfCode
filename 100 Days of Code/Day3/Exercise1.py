print("WELCOME TO THE BMI CALCULATOR")
height = input("Whats your height in metres\n")
weight = input("Whats  yor weight in Kg\n")
converted_height = float(height) ** 2
converted_weight = float(weight)
#round up your values to the nearest whole number
bmi = round((converted_weight) / (converted_height))

if bmi < 18.5:
    print(f"Your BMI IS {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI IS {bmi}, you have normal weight")
elif bmi < 30:
    print(f"Your BMI IS {bmi}, you are overweight\nSee a nutritionist!!")
elif bmi < 35:
    print(f"Your BMI IS {bmi}, you are obese\nSee a doctor!!")
else:
    print(f"Your BMI IS {bmi}, you are clinically obese\nSee a doctor ASAP!!")
