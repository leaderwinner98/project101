import random

response = "y"

while response == "y":

    dice_value = random.randint(1, 6)
    

    print("-------")
    print(f"| {dice_value}   |")
    print("-------")
    
    response = input("Enter 'y' to roll again, 'n' to exit: ")
    
    while response != "y" and response != "n":
        response = input("Please enter 'y' to roll again, 'n' to exit: ")

print("Thanks for playing!")
