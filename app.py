import sqlite3
import random
import menu

# Establish a connection to the SQLite database
conn = sqlite3.connect("app_data.db")
cursor = conn.cursor()

def fetch_questions(grade):
    cursor.execute("SELECT question, options, answer FROM qa_table WHERE grade=?", (grade,))
    return cursor.fetchall()

def ask_question(question_data, question_number):
    question, options, answer = question_data
    options_list = options.split(",")  # Assuming options are stored as a comma-separated string
    print(f"Question {question_number}: {question}")
    for option in options_list:
        print(option)
    
    user_input = input("Your answer (enter the letter corresponding to the option): ")
    return user_input.upper()


def main():
    print("Welcome to the English Quiz!")
    name = menu.username()  # Get the user's name
    print(f"Hello, {name}!")

    user_choice = menu.get_user_choice()

    if user_choice == '1':
        grade = input("Enter your grade (a1-a2, b1-b2, etc.): ").upper
        questions_to_ask = 5
        total_correct = 0

        questions = fetch_questions(grade)

        if len(questions) < questions_to_ask:
            print("Not enough questions for your grade level.")
            return

        random.shuffle(questions)
        asked_questions = set()

        for question_number, question_data in enumerate(questions, start=1):
            while True:
                if question_data in asked_questions:
                    question_data = random.choice(questions)
                else:
                    asked_questions.add(question_data)
                    break

            user_answer = ask_question(question_data, question_number)
            correct_answer = question_data[2]
            if user_answer == correct_answer[0]:
                total_correct += 1
                print("Correct!\n")
            else:
                print(f"Wrong. The correct answer is: {correct_answer}\n")

            if question_number == questions_to_ask:
                break

        score = (total_correct / questions_to_ask) * 10
        print(f"Quiz completed! Your score: {score:.2f}/10")
    else:
        print("\nGoodbye!")

    conn.close()

if __name__ == "__main__":
    main()
print()