import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget
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
        self.setWindowTitle("Language Learning Quiz App - ByASH")
        
        self.init_ui()

    def init_ui(self):
        label = QLabel("Welcome to the Language Quiz App", self)
        label.setGeometry(50, 50, 300, 50)
        
        start_button = QPushButton("Start Quiz", self)
        start_button.setGeometry(50, 100, 200, 50)
        start_button.clicked.connect(self.start_quiz)

    def start_quiz(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout()

        label = QLabel("Enter Your Name:", self.central_widget)
        self.name_input = QLineEdit(self.central_widget)

        save_button = QPushButton("Save", self.central_widget)
        save_button.clicked.connect(self.save_name)

        layout.addWidget(label)
        layout.addWidget(self.name_input)
        layout.addWidget(save_button)

        self.central_widget.setLayout(layout)

    def save_name(self):
        username = self.name_input.text()
        if username:
            self.label = QLabel(f"Hi, {username}", self)
            self.label.setGeometry(50, 100, 200, 50)
            self.save_username_to_database(username)

    def save_username_to_database(self, username):
        conn = sqlite3.connect("app_data.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LanguageQuizApp()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
