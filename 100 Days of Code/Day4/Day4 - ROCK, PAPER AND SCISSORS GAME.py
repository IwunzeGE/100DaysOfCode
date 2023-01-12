#ROCK, PAPER AND SCISSORS GAME

import random
print("Welcome to Rock, Paper and Scissors Game")
print("Type 0 for Rock, 1 for Paper & 2 for Scissors")

players_choice = int(input("What do you choose?\n"))

computer_choice = random.randint(0, 2)

if players_choice == 0:
#rock  
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif players_choice == 1:
#papers
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif players_choice > 2:
    print("This is an invalid number!!")

else:
#scissors    
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")



if computer_choice == 0:
#rock
    print("Computer chose:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif computer_choice == 1:
#papers
    print("Computer chose:")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif players_choice >2:
    print("Error!")
    
else:
#scissors
    print("Computer chose:")    
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


if players_choice == 0 and computer_choice == 2:
    print("You won!!")
elif players_choice == 2 and computer_choice == 1:
    print("You win!!")
elif players_choice == 1 and computer_choice == 0:
    print("You win!!")
elif players_choice == computer_choice:
    print("It\'s a draw!!")
elif players_choice > 2:
    print("You lose!!")
else:
    print("You lose!!")