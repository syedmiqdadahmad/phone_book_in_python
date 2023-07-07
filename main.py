# initialize a phone book

phone_book = {}

# func to add contact

def add_contact():
    name = input("Enter a name: ")
    number = input("Enter phone number: ")
    phone_book[name] = number
    print("contact added succesfully.")

def remove_contact():
    name = input("enter a name: ")
    if name in phone_book:
        del phone_book[name]
        print("contact removed")
    else:
        print("contact not found")

def search_contact():
    name = input("enter a name: ")
    if name in phone_book:
        print(phone_book[name])
    else:
        print("contact not found ")

def display_contact():
    if phone_book == 0:
        print("phonebook empty")
    else:
        print(phone_book)

# code for main menu
while True:

    print("1, press to add contact: ")
    print("2, press to remove contact: ")
    print("3, press to search contact: ")
    print("4, press to display contact: ")
    print("5, press to quit contact: ")

    choice = input("enter choice (1-5); ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        remove_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        display_contact()
    elif choice == "5":
        print('goodbye')
        break

else:
    print("enter valid option ! ")

