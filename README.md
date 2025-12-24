#IPS Finance


IPS Finance is a simple command-line personal finance tracker written in Python.
I built this project to practice structuring real software, not just writing scripts.

The goal of the project is to track expenses, analyze spending habits, and give
basic feedback on financial behavior.

## Features

- Add and store expenses using JSON
- Categorize expenses (necessary vs unnecessary)
- Compare spending against a budget
- See spending totals by category
- Points-based feedback on spending behavior
- Reflective insights about spending habits
- Simple month-end spending prediction
- Works with any currency (not hardcoded)


## Project Structure

IPS_Finance/
├── app.py            # Streamlit web app
├── main.py           # Runs the CLI program
├── storage.py        # Saves and loads expenses
├── analysis.py       # Spending calculations and insights
├── rules.py          # Points and scoring logic
├── prediction.py     # Spending prediction
├── utils.py          # User input helpers
├── account.py        # Account data (balance, budget, currency)
├── data.json         # Stored expenses
├── account.json      # Stored account information
└── README.md



## How to Run

1. Make sure Python 3 is installed
2. Open a terminal in the project folder
3. Run:

python main.py

4. Follow the prompts in the terminal


## Why I Built This

I wanted to actually see how Python code works, how JSON files are loaded and updated, and how a normal Python program can be turned into a website.

This project helped me practice clean code structure, separating logic into
different files, and thinking about how real applications are designed.


## Live Demo (Web App)

I also created a simple web version of this project using Streamlit.

Live app: https://smartspend-dev.streamlit.app/

