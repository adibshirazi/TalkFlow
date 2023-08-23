# menu.py
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def username():
    cursor.execute("SELECT * FROM user")
    user_record = cursor.fetchone()
    
    if user_record is None:
        name = input("What's Your Name? ")
        cursor.execute("INSERT INTO user (name) VALUES (?)", (name,))
        conn.commit()
        return name
    else:
        return user_record[0]  # Assuming name is the first column

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
 