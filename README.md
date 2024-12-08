# TalkFlow

This is a simple English Quiz application built with Python and Tkinter. The app allows users to take quizzes based on their grade level and practice English vocabulary.

## Features

- **Quiz Mode**: Users can take a quiz by selecting their grade level. The app will fetch random questions from the database and display them to the user.
- **Word Practice Mode**: Users can practice vocabulary words. The app will fetch random words and their definitions from the database and display them one by one.
- **Database Interaction**: The app uses SQLite to store and retrieve quiz questions and vocabulary words.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/adibshirazi/TalkFlow.git
    cd TalkFlow
    ```

2. **Install the required libraries**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up the database**:
    - Ensure that `app_data.db` is present in the same directory as the script.
    - The database should contain a table `qa_table` for quiz questions and `Words` for vocabulary words.

## Usage

1. **Run the application**:
    ```sh
    python app.py
    ```

2. **Using the Application**:
    - **Start Quiz**:  Choose "Start Quiz", enter your grade level, and answer the questions.
    - **Word Practice**: Choose "Word Practice" to start practicing vocabulary words.

## Code Overview

### `app.py`
This script is the main entry point for the application.

- **Imports**:
  - `sqlite3`: For database interaction.
  - `random`: For shuffling quiz questions.
  - `menu`, `word_practice`, `sys`, `graphic_ver`, `os`: Modules for various functionalities of the application.

- **Database Connection**:
  Establishes a connection to the SQLite database `app_data.db`.

- **Functions**:
  - `fetch_questions(grade)`: Fetches quiz questions based on the specified grade level.
  - `ask_question(question_data, question_number)`: Displays a quiz question and gets the user's answer.
  - `grades()`: Prompts the user to enter their grade level.
  - `main()`: The main quiz logic, fetching questions, asking them, and calculating the score.
  
- **Execution**:
  Runs an infinite loop to display the menu and execute the corresponding command.

### `menu.py`
This script handles the user menu and getting the user's name.

- **Database Connection**:
  Establishes a connection to the SQLite database `app_data.db`.

- **Functions**:
  - `username()`: Retrieves the user's name from the database or prompts the user to enter their name if not found.
  - `display_menu()`: Displays the main menu options to the user.
  - `get_user_choice()`: Validates the user's menu choice.
- **Preview**:
    - Start Quiz
    - Start Quiz (graphic version)
    - Word Practice
    - Exit

### `word_practice.py`
This script handles the word practice mode.

- **Imports**:
  - `sqlite3`: For database interaction.
  - `requests`: For making API calls to fetch random words and their definitions.
  - `date`: For checking and storing the date of word retrieval.
  - `os`, `time`: For system operations and delays.
  - `menu`: For interacting with the user menu.

- **Functions**:
  - `main()`: Main logic for word practice, fetching words and definitions, and displaying them to the user.
  - `word()`: Fetches a random word from the API.
  - `definition()`: Fetches the definition of the word from the API.
  - `database()`: Inserts fetched words and definitions into the database.
  - `date_checker()`: Checks the latest date words were retrieved from the database.

### `database_insertor.py`

This script imports questions and answers from text files (`questions.txt` and `answers.txt`) into an SQLite database (`app_data.db`) for use in the English Quiz application.

- **Imports**:
  - `sqlite3`: For database interaction.

- **Description**:
  - Connects to the SQLite database `app_data.db`.
  - Reads questions and answers from text files and splits them into individual items.
  - Inserts each question, options, answer, and grade into the `qa_table`.
  - Commits changes and closes the database connection.

- **Downloading Text Files**:
  - You can download sample `questions.txt` and `answers.txt` files from the internet.
  - Place these files in the same directory as the script before running `database_insertor.py`.

### `graphic_ver.py`
This script contains the main application class for the graphical version of the English Quiz App.

- **Main Application Class**:
  - `EnglishQuizApp`: Initializes the application, creates the UI, and handles the logic for the quiz and word practice modes.

- **Methods**:
  - `start_quiz()`: Starts the quiz by fetching questions from the database and displaying them to the user.
  - `start_word_practice()`: Starts the word practice mode by fetching random words and their definitions from the database and displaying them one by one.
  - `fetch_questions()`: Fetches quiz questions from the database based on the user's grade level.
  - `fetch_words()`: Fetches random words and their definitions from the database.
  - `ask_question()`: Displays a quiz question and gets the user's answer.
  - `show_next_word()`: Displays the next word and its definition in word practice mode.
  - `exit_app()`: Exits the application.

## Database Structure

- **qa_table**:
    - `id`: INTEGER PRIMARY KEY
    - `grade`: TEXT
    - `question`: TEXT
    - `options`: TEXT
    - `answer`: TEXT

- **Words**:
    - `id`: INTEGER PRIMARY KEY
    - `word`: TEXT
    - `definition`: TEXT

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.
