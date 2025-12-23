from storage import add_expense, read_expenses
from analysis import get_total, get_category_totals, necessary_vs_unnecessary, reflective_insights
from rules import calculate_points
from account import read_account, set_balance, set_budget, subtract_from_balance, set_currency
from utils import ask_float, ask_text, get_user_category, get_expense_input


def show_summary(expenses, necessary_list, unnecessary_list, budget, currency):
    total = get_total(expenses)
    category_totals = get_category_totals(expenses)
    need, want = necessary_vs_unnecessary(expenses, necessary_list, unnecessary_list)

    print("\n--- SUMMARY ---")
    print(f"Total expenses: {currency}{total:.2f}")
    print("By category:")
    for cat, amt in category_totals.items():
        print(f"  {cat}: {currency}{amt:.2f}")

    print(f"Necessary total: {currency}{need:.2f}")
    print(f"Unnecessary total: {currency}{want:.2f}")

    print("\n--- REFLECTIVE INSIGHTS ---")
    insights = reflective_insights(total, category_totals, need, want, budget)
    for msg in insights:
        print("-", msg)


def show_points(expenses, necessary_list, unnecessary_list, budget):
    points, reasons = calculate_points(expenses, necessary_list, unnecessary_list, budget)
    print("\n--- POINTS ---")
    print("Points:", points)
    print("Reasons:")
    for r in reasons:
        print("-", r)


def setup_account_if_needed():
    acc = read_account()

    if acc.get("currency", "") == "":
        currency = input("Choose your currency symbol (example: $, ₹, €, NPR): ").strip()
        if currency == "":
            currency = ""
        set_currency(currency)

    if acc.get("balance", 0) == 0:
        bal = ask_float("Enter your account balance: ")
        set_balance(bal)

    if acc.get("budget", 0) == 0:
        bud = ask_float("Enter your monthly budget: ")
        set_budget(bud)

    return read_account()


def setup_account():
    account = read_account()

    if account["balance"] == 0:
        balance = float(input("Enter your account balance: "))
        set_balance(balance)

    if account["budget"] == 0:
        budget = float(input("Enter your monthly budget: "))
        set_budget(budget)

    return read_account()



def main():
    account = setup_account()
    budget = account["budget"]

    account = setup_account_if_needed()
    currency = account.get("currency", "")
    budget = account.get("budget", 0)

    print("\nNow classify your categories.")
    necessary_list, unnecessary_list = get_user_category()

    while True:
        print("\n--- MENU ---")
        print("1) Add expense")
        print("2) Show summary")
        print("3) Show points")
        print("4) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            amount, category, note, date, payment_method, merchant, location = get_expense_input()

            expense = add_expense(amount, category, note, date, payment_method, merchant, location)
            subtract_from_balance(amount)

            print("Saved:", expense)

        elif choice == "2":
            expenses = read_expenses()
            account = read_account()
            budget = account.get("budget", 0)
            currency = account.get("currency", "")
            show_summary(expenses, necessary_list, unnecessary_list, budget, currency)

        elif choice == "3":
            expenses = read_expenses()
            account = read_account()
            budget = account.get("budget", 0)
            show_points(expenses, necessary_list, unnecessary_list, budget)

        elif choice == "4":
            print("Bye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

