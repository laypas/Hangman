# Hangman Game
A simple Hangman game built with Python (Flask) and HTML for  for a vocational university project. This project provided practical experience in building a web application with a Python backend.


## How to Run Locally
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/laypas/hangman-game.git
    cd Hangman
    ```

2.  **Set up Python Environment (if needed):**

*   Install the latest version of Python 3
*   Install VSCode
*   Create a virtual environment and activate the environment https://flask.palletsprojects.com/en/stable/installation/#create-an-environment
*   Install Python dependency Flask by using the command "$ pip install Flask", within the activated environment

3.  **Run the Python server:**
    ```Phyton Terminal
    python HangApp.py
    ```

4.  **Open the game in your browser:**
    Open the development server in your web browser.


## Game Instructions

*   A box with empty spaces (one for each letter) in a randomly picked word is displayed.
*   Guess letters by clicking the letters on the on-screen keyboard.
*   You have 8 guesses.
*   Win: Guess the word correctly!
*   Lose: Run out of guesses, and the Hangman is drawn.
*   Reset: Click the "Reset Game" button to play again with a new word.


## Project Structure

hangman/                    # Root directory
├── README.md               # The main README file
├── Hangman.py              # Core game logic (functions, etc.)
├── HangApp.py              # Flask application (routing, handling requests)
└── templates/              # HTML templates
    └── HangTemp.html       # Main game template