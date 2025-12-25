"""Module providing a function to use JSON file format"""
import json
import os

# Function to load contacts
def load_contacts():
    try:
        with open("contacts.json", "r", encoding="utf-8") as rf:
            return json.load(rf)
    except FileNotFoundError:
        return {}

# Function to save contacts
def save_contacts(contacts):
    with open("contacts.json", "w", encoding="utf-8") as wf:
        json.dump(contacts, wf)

# Function to add a new contact
def add_contact(contacts, name, phone_number, email):
    """Adds a new contact to the contacts dictionary and saves it to a JSON file."""
    # Format phone number as xxx-xxx-xxxx
    formatted_phone_number = "-".join(
        [phone_number[:3], phone_number[3:6], phone_number[6:]]
    )

    contacts[name] = {
        "phone_number": formatted_phone_number,
        "email": email,
    }
    save_contacts(contacts)


# Function to search for a contact
def search_contact(contacts, name):
    """Searches for a contact in the contacts dictionary."""
    if name in contacts:
        return contacts[name]
    else:
        return None


# Function to print the contacts
def print_contacts(contacts):
    """Prints all the contacts in the contacts dictionary."""
    for name, contact in contacts.items():
        print(f"Name: {name}")
        print(f"Phone number: {contact['phone_number']}")
        print(f"Email: {contact['email']}")


# Main function
def run():
    """Function running all subfunctions"""
    contacts = load_contacts()
    
    while True:
        # Get the user's choice
        choice = input("What do you want to do? (add, search, print, quit): ")
    
        # Do the task based on the user's choice
        if choice == "add":
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            add_contact(contacts, name, phone_number, email)
        elif choice == "search":
            name = input("Enter the name of the contact you want to search for: ")
            contact = search_contact(contacts, name)
            if contact:
                print(contact)
            else:
                print("Contact not found")
        elif choice == "print":
            print_contacts(contacts)
        elif choice == "quit":
            break
        else:
            print("Invalid choice")


# Run the main function
if __name__ == "__main__":
    run()
