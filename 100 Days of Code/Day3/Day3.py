#Treasure Island

print("Welcome to Treasure Island.\nYour mission is to find the tresure.")

first_move = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"\n').lower()

if first_move == "left":
    #Game will continue
    second_move = input("You have reached a lake, there is an island in the middle of the lake, Type 'swim' to swim to the island or 'wait' to wait for a boat\n").lower()
    if second_move == "wait":
        #Game will continue
        third_move = input("You arrived at the island. You can see three doors. Which colour would you open to see the treasure? red, blue or yellow\n").lower()
        if third_move == "yellow":
            print("You found the treasure! You win")
        elif third_move == "red":
            print("Its a room full of fire! Game over")
        elif third_move == "blue":
            print("You entered a room full of bees! Game over")
        else:
            print("You chose a door that does not exist! Game over")
    else:
        print("You got attacked by  an angry  shark! Game over")    
else:
    print("You fell into a hole! Game over")
