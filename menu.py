# menu.py
import sqlite3
import os

conn = sqlite3.connect("app_data.db")
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
    os.system('cls' if os.name == 'nt' else 'clear')
    username()
    print("1. Start Quiz")
    print("2. Start Quiz (graphic)")
    print("3. Word Practice")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def get_user_choice():
    choice = display_menu()
    while choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please select again.")
        choice = display_menu()
    return choice
 