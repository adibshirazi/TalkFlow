import sqlite3

# Connect to the SQLite database
db_connection = sqlite3.connect('app_data.db')
db_cursor = db_connection.cursor()

# Read the questions from the file
with open('questions.txt', 'r') as questions_file:
    questions_data = questions_file.read()

# Read the answers from the file
with open('answers.txt', 'r') as answers_file:
    answers_data = answers_file.read()

# Split the text into individual questions and answers
questions = questions_data.split('Question ')
answers = answers_data.split('Answer ')

while True:
    level = input("Grade (A1-A2, B1-B2, C1-C2): ").upper()
    if level in ['A1-A2', 'B1-B2', 'C1-C2']:
        break
    else:
        print("Invalid grade. Please enter A1-A2, B1-B2, or C1-C2.")

# Iterate through the questions and answers and insert them into the database
for question, answer in zip(questions[1:], answers[1:]):
    question_lines = question.strip().split('\n')
    question_text = question_lines[1].strip()
    options = [option.strip() for option in question_lines[2:] if option.strip()]  # Extract options
    
    answer_lines = answer.strip().split('\n')
    answer_text = answer_lines[0].split(": ")[1] if len(answer_lines) > 0 else "(No answer provided)"

    # Convert options list to a formatted string
    options_text = "\n".join(options)
    
    db_cursor.execute(
        "INSERT INTO qa_table (question, options, answer, grade) VALUES (?, ?, ?, ?)",
        (question_text, options_text, answer_text, level)
    )

# Commit the changes and close the database connection
db_connection.commit()
db_connection.close()

print("Data inserted successfully.")
