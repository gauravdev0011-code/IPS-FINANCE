from analysis import get_total, get_count

def month_end_spend(expenses):
    if not expenses:
        return ("No prediction available yet.")

    total = get_total(expenses)
    count = get_count(expenses)

    if count == 0:
        return ("No prediction available yet.")

    average_per_expense = total/count

    # Assumption : 30 expenses per month
    estimated_transactions = 30
    predicted_total = average_per_expense * estimated_transactions

    return (
        f"Average per expense: {average_per_expense:.2f}. "
        f"Estimated month-end spending: {predicted_total:.2f}."
    )    