from storage import add_expense, read_expenses
from analysis import get_total, get_count, get_category_totals

add_expense(12.5, "Food", "Coffee", "2025-12-21", "Card", "Starbucks", "Jacksonville")

expenses = read_expenses()

print("Count:", get_count(expenses))
print("Total:", get_total(expenses))
print("By category:", get_category_totals(expenses))

