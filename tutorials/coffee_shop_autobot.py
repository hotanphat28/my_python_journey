"""Module providing function to help a customer order a cup of coffee"""

import sys

# change this to your coffee shop name
COFFEE_SHOP_NAME = "HTP28"

print("Hello, welcome to " + COFFEE_SHOP_NAME + " Coffee!!!\n")

# ask for the customer name
name = input("What's your name?\n")

CONSIDER_EVIL_NAME = ["Ben", "Patricia", "Loki"]

if name in CONSIDER_EVIL_NAME:
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("\nYou're not welcome here Evil " + name + "!! Get out!!\n")
        sys.exit(0)
    else:
        print("\nOh, so you're on of those good " + name + ", Come on in!!\n")
else:
    print("\nHello " + name + ", thank you so much for coming in today.\n")

MENU = ["Black Coffee", "Espresso", "Latte", "Cappuccino", "Frappuccino"]

print(name + ", Here is the menu")
print(MENU)

while True:
    # ask for what the customer's order
    order = input("\nWhat would you like?\n")

    if order in MENU:
        if order == MENU[0]:
            price = 3
        elif order == MENU[1]:
            price = 8
        elif order == MENU[2]:
            add_cream = input("\nDo you want to add cream?\n")
            if add_cream == "Yes":
                price = 11
            else:
                price = 9
        elif order == MENU[3]:
            price = 12
        elif order == MENU[4]:
            price = 13

        break

    print("\nSorry, we don't sell that. Please choose from the menu.")
    print("Here is the menu again")
    print(MENU)

# ask for the quantity the customer wants to order
quantity = int(input("\nHow many coffees would you like?\n"))

total = price * quantity

print("\nThe total price is: $" + str(total))

if quantity > 1:
    print(f"\nSounds good {name}, we'll serve your {quantity} {order}s in a moment.")
else:
    print(f"\nSounds good {name}, we'll serve your {quantity} {order} in a moment.")
