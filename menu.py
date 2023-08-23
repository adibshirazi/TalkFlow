# menu.py

def display_menu():
    print("1. Start Quiz")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

def get_user_choice():
    choice = display_menu()
    while choice not in ('1', '2'):
        print("Invalid choice. Please select again.")
        choice = display_menu()
    return choice
