import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
import sqlite3
import random
import menu
import os
import word_practice
from datetime import date
import time

conn = sqlite3.connect("app_data.db")
cursor = conn.cursor()

class EnglishQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English Quiz App")

        self.style = ttk.Style()  # Create a style instance
        self.style.configure("TButton", padding=10, relief="flat", background="#007acc", foreground="black")

        self.label = ttk.Label(self.root, text="Welcome to Talk Flow", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=15)

        self.start_button_quiz = ttk.Button(self.root, text="Start Quiz", command=self.start_quiz)
        self.start_button_quiz.pack(pady=10)

        self.start_button_word_practice = ttk.Button(self.root, text="Word Practice", command=self.start_word_practice)
        self.start_button_word_practice.pack(pady=10)

        self.exit_button = ttk.Button(self.root, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)

    def fetch_questions(self, grade):
        cursor.execute("SELECT question, options, answer FROM qa_table WHERE grade=?", (grade,))
        return cursor.fetchall()

    def exit_app(self):
        self.root.destroy()
        os._exit(0)

    def ask_question(self, question_data, question_number):
        question, options, answer = question_data
        options_list = options.split(",")  # Assuming options are stored as a comma-separated string

        question_text = f"Question {question_number}: {question}\n"
        options_text = "\n".join(options_list)

        user_input = simpledialog.askstring("Quiz Question", question_text + options_text + "\nYour answer:")
        return user_input.upper()

    def start_word_practice(self):
        name = menu.username()
        messagebox.showinfo("Welcome", f"Hello, {name}!")


        if str(word_practice.date_checker()) != str(date.today()):
            messagebox.showinfo("Welcome", f"Hello, {name}!")
            


        
        new_window = tk.Toplevel(self.root)
        new_window.title("Word Practice")
        new_window.geometry("400x300")
        
        self.word_label = ttk.Label(new_window, text="", font=("Helvetica", 14))
        self.word_label.pack(pady=10)
        
        self.definition_text = ScrolledText(new_window, wrap=tk.WORD, font=("Helvetica", 12), height=5, width=40)
        self.definition_text.pack(pady=10)
        
        self.next_button = ttk.Button(new_window, text="Next Word", command=self.show_next_word)
        self.next_button.pack(pady=10)
        
        self.word_counter = 0

        if str(word_practice.date_checker()) == str(date.today()):
            self.words_def = self.fetch_words()
            if self.words_def:
                self.show_next_word()
            else:
                messagebox.showinfo("No Words", "No words available for practice.")
                new_window.destroy()

    def fetch_words(self):
        cursor.execute("SELECT word, definition FROM Words ORDER BY RANDOM()")
        words = cursor.fetchall()
        return words

    def show_next_word(self):
        if self.word_counter < len(self.words_def) and self.word_counter < 10:
            word, definition = self.words_def[self.word_counter]
            self.word_label.config(text=f"Word: {word}")
            self.definition_text.delete(1.0, tk.END)  # Clear previous text
            self.definition_text.insert(tk.END, f"Definition: {definition}")
            self.word_counter += 1
        else:
            messagebox.showinfo("Completed", "You have completed the word practice session!")
            self.next_button.config(state="disabled")

    def start_quiz(self):
        name = menu.username()
        messagebox.showinfo("Welcome", f"Hello, {name}!")

        grade = simpledialog.askstring("Enter Grade", "Enter your grade (a1-a2, b1-b2, etc.):").upper()
        questions_to_ask = 5
        total_correct = 0
        questions = self.fetch_questions(grade)
        levels = ["A1-A2", "B1-B2"]
        if grade not in levels:
            messagebox.showerror("Error", "Please try again!")
            return

        elif len(questions) < questions_to_ask:
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
    root.geometry("300x300")
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.geometry(f"+{position_right}+{position_down}")

    app = EnglishQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
