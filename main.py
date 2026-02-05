import sys
import os

# Import modules
from scripts import calculation
from scripts import coffee_shop_autobot
from scripts import get_to_know_you
from scripts import show_calendar_in_month
from scripts import student_object
from scripts import contacts

def print_menu():
    print("\n--- Python Journey Tutorials ---")
    print("1. Calculation (Average Scores)")
    print("2. Coffee Shop Autobot")
    print("3. Get To Know You")
    print("4. Show Calendar")
    print("5. Student Object Demo")
    print("6. Contacts App")
    print("q. Quit")

def run():
    while True:
        print_menu()
        choice = input("\nSelect a tutorial to run: ")

        if choice == '1':
            print("\n--- Running Calculation ---")
            calculation.run()
        elif choice == '2':
            print("\n--- Running Coffee Shop Autobot ---")
            coffee_shop_autobot.run()
        elif choice == '3':
            print("\n--- Running Get To Know You ---")
            get_to_know_you.run()
        elif choice == '4':
            print("\n--- Running Show Calendar ---")
            show_calendar_in_month.run()
        elif choice == '5':
            print("\n--- Running Student Object Demo ---")
            student_object.run()
        elif choice == '6':
            print("\n--- Running Contacts App ---")
            contacts.run()
        elif choice.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    run()
