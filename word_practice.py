import sqlite3
import requests
from datetime import date
import os
import menu
import time


#https://api.api-ninjas.com/v1/randomword
#https://wordsapiv1.p.mashape.com/words/Aranyaka




def main():
    
    print("Welcome to Word Practicing section!")
  
    
    if str(date_checker()) != str(date.today()):
            print("reciveing the data...")
            database()
            print("Done.")
        
    elif str(date_checker()) == str(date.today()):
        dict_counter = 0
        conn = sqlite3.connect('app_data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT word, definition FROM Words")

        words_def = cursor.fetchall()
        for i in range(10):
            print(f"word: {words_def[dict_counter][0]}\nDefinition: {words_def[dict_counter][1]}\n \n")

            command = input("Press Enter to go to the next word: ")

            dict_counter += 1
            os.system('cls' if os.name == 'nt' else 'clear')
        
        conn.close()
    print("Have a nice day!")
    time.sleep(0.3)


        
        




def word():

    word_api = "https://api.api-ninjas.com/v1/randomword"


    response = requests.get(word_api, headers={'X-Api-Key': 'REDACTED'})
 

    word_data = response.json()

    extracted_words = (word_data['word'])
    
    return extracted_words[0]


def definition():

    words = word() 

    definition_api = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(words)
    response = requests.get(definition_api, headers={'X-Api-Key': 'REDACTED'})
    definition_data = response.json()
    
    extracted_definition = (definition_data["definition"])

    return extracted_definition


def database():

    db_connection = sqlite3.connect('app_data.db')
    db_cursor = db_connection.cursor()
    for i in range(10):
        final_word = word()
        final_definition = definition()
        final_date = date.today()
        if final_definition:
            try:
                   db_cursor.execute(
                "INSERT INTO words (word, definition, date) VALUES (?, ?, ?)",
                (final_word, final_definition, final_date)
                )
            except:
                break
               
    db_connection.commit()
    db_connection.close()


def date_checker():
    
        # Connect to SQLite database
    conn = sqlite3.connect('app_data.db')
    cursor = conn.cursor()

    # Execute query to find the latest date
    cursor.execute("SELECT MAX(date) FROM Words")

    # Fetch the result
    latest_date = cursor.fetchone()[0]
    conn.close()

    # Print the latest date (optional)
    return latest_date

    # Close the connection

    
    

if __name__ == "__main__":
    main()