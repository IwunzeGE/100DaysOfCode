#Tip Calculator

#1. Create a greeting for your program
print("Welcome To The Tip Calculator\n")

#2. Ask the user for the total bill
bill = float(input("Whats is the total bill? \n$"))

#3. Ask the user for the percenttage tip they'd like to give
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))

#4. Ask the user for the how many people that would split the bill
no_of_split = int(input("How many people would split the bill?\n"))

#4. Calculate the final amount each person is to pay
bill_with_tip = bill + (tip_percentage/100 * bill)
total_bill = bill_with_tip / no_of_split

#5. Round bill to 2 decimal places
rounded_bill = round(total_bill, 2)

print(f"Each person should pay: ${rounded_bill}")


