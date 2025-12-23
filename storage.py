import json

EXPENSE_FILE = "data.json"

def read_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as f:
            expenses = json.load(f)
            return expenses
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as f:
         json.dump(expenses, f, indent=4)

def add_expense(amount, category, note, date, payment_method, merchant, location):
    expenses = read_expenses()

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date,
        "payment_method": payment_method,
        "merchant": merchant,
        "location": location

    }

    expenses.append(expense)
    save_expenses(expenses)

    return expense
    