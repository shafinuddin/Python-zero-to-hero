print("Welcome to Treasure island.")
print("Your mission is to find the Treasure.")
print("You are at a cross road. Where do you want to go? Type 'left' or 'right'.")
cross_road = input().lower()
if cross_road == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    lake = input().lower()
    if lake == "wait":
        print("You arrive at the island unharmed.")
        print("There is a house with 3 doors. One red, one yellow and one blue.")
        print("Which color do you choose?")
        door = input().lower()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")        