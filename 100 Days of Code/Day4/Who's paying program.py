#Who's paying program

#input the names seperated by a comma and space
import random
names = input("Type in your names (seperated by a comma and space):\n")

#take the inputs and put them into a list by spliting them using the ,
list_of_names = names.split(", ")

#check for the total number of names
no_of_names = len(list_of_names)

#no_of_names -1 in order to get in the right arrangement of arrays
random_payer = random.randint(0, no_of_names-1)

#index list_of_names so that it takes random values
person_that_will_pay = list_of_names[random_payer]

print(f"{person_that_will_pay} will pay the bill today")