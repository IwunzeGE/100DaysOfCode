#LEAP YEAR CHECKER

print("Welcome To The Leap Year Checker!\n")

year = int(input("What year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 ==  0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap  year")
else:
    print("This is not a leap year")