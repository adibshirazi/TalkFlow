import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import random
import menu

conn = sqlite3.connect("app_data.db")
cursor = conn.cursor()

class EnglishQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English Quiz App")

        self.label = tk.Label(self.root, text="Welcome to the English Quiz!")
        self.label.pack()

        self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()

    def fetch_questions(self, grade):
        cursor.execute("SELECT question, options, answer FROM qa_table WHERE grade=?", (grade,))
        return cursor.fetchall()

    def ask_question(self, question_data, question_number):
        question, options, answer = question_data
        options_list = options.split(",")  # Assuming options are stored as a comma-separated string

        question_text = f"Question {question_number}: {question}\n"
        options_text = "\n".join(options_list)

        user_input = simpledialog.askstring("Quiz Question", question_text + options_text + "\nYour answer:")
        return user_input.upper()

    def start_quiz(self):
        name = menu.username()
        messagebox.showinfo("Welcome", f"Hello, {name}!")

        grade = simpledialog.askstring("Enter Grade", "Enter your grade (a1-a2, b1-b2, etc.):").upper()
        questions_to_ask = 5
        total_correct = 0

        questions = self.fetch_questions(grade)

        if len(questions) < questions_to_ask:
            messagebox.showerror("Error", "Not enough questions for your grade level.")
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

            user_answer = self.ask_question(question_data, question_number)
            correct_answer = question_data[2]
            if user_answer == correct_answer[0]:
                total_correct += 1
                messagebox.showinfo("Correct", "Correct!\n")
            else:
                messagebox.showerror("Incorrect", f"Wrong. The correct answer is: {correct_answer}\n")

            if question_number == questions_to_ask:
                break

        score = (total_correct / questions_to_ask) * 10
        messagebox.showinfo("Quiz Completed", f"Quiz completed! Your score: {score:.2f}/10")
    
        conn.close()

def main():
    root = tk.Tk()
    app = EnglishQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
