user_height=float(input("Enter your height in cm: "))
if user_height>=120:
    print("You are able to ride the roller coaster.")
    user_age=int(input("Enter your age: "))
    if user_age<=12:
        bill=5
        print("Child ticket: $5")
    elif user_age<=18:
        bill=7
        print("Youth ticket: $7")
    else :
        bill=10
        print("Adult ticket: $10")

    photo=input("Do you want a photo taken? Y or N: ")
    if photo=="Y":
        # Add $3 to the bill if the user wants a photo
        bill+=3
        print("Photo: $3")
    print(f"Your final bill is: ${bill}")
   

else:
    print("You are not able to ride the roller coaster.")