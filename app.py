import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sqlite3
import os

if not os.path.exists("app_data.db"):
    conn = sqlite3.connect("app_data.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT
                    )''')

    conn.commit()
    conn.close()

class LanguageQuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Language Learning Quiz App -ByASH")
        
        self.init_ui()

    def init_ui(self):
        label = QLabel("Welcome to the Language Quiz App", self)
        label.setGeometry(50, 50, 300, 50)
        
        start_button = QPushButton("Start Quiz", self)
        start_button.setGeometry(50, 100, 200, 50)
        start_button.clicked.connect(self.start_quiz)

    def start_quiz(self):
        # Start the quiz logic here
        with open('text.txt') as text:
            lines = text.readlines()
        

    def start_quiz_api(self):
        # this section is for the api of the app
        
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LanguageQuizApp()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
