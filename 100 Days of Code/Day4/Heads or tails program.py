#Heads or tail program

#if the random number is = 1 you get Heads
#if the random number is = 0 you get Tails
import random

random_number = random.randint(0,1)

if random_number == 1:
    print("Heads")
elif random_number == 0:
    print("Tails")
