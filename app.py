import streamlit as st
from storage import read_expenses, add_expense
from analysis import get_total, get_count, get_category_totals, necessary_vs_unnecessary, reflective_insights
from rules import calculate_points

st.set_page_config(page_title="IPS Finance", layout="centered")

st.title("IPS Finance")
st.caption("Track spending, see patterns, and earn points for discipline.")

# --- Sidebar setup ---
st.sidebar.header("Settings")

currency = st.sidebar.text_input("Currency (symbol or code)", value="$")
budget = st.sidebar.number_input("Monthly budget", min_value=0.0, value=0.0, step=10.0)

necessary_raw = st.sidebar.text_input("Necessary categories (comma separated)", value="groceries,rent,car_payment")
unnecessary_raw = st.sidebar.text_input("Unnecessary categories (comma separated)", value="entertainment,dining_out")

necessary_list = [x.strip() for x in necessary_raw.split(",") if x.strip()]
unnecessary_list = [x.strip() for x in unnecessary_raw.split(",") if x.strip()]

st.divider()

# --- Add expense form ---
st.subheader("Add Expense")
with st.form("add_expense_form", clear_on_submit=True):
    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    category = st.text_input("Category (example: Food)")
    note = st.text_input("Note (optional)")
    date = st.text_input("Date (YYYY-MM-DD)")
    payment_method = st.text_input("Payment method (cash/card/upi)")
    merchant = st.text_input("Merchant (example: Walmart)")
    location = st.text_input("Location (example: Jacksonville)")

    submitted = st.form_submit_button("Add")

if submitted:
    if amount <= 0 or not category or not date:
        st.error("Amount must be > 0 and Category/Date cannot be empty.")
    else:
        add_expense(amount, category, note, date, payment_method, merchant, location)
        st.success("Expense added.")

# --- Dashboard ---
expenses = read_expenses()

st.subheader("Dashboard")

if not expenses:
    st.info("No expenses yet. Add your first expense above.")
else:
    total = get_total(expenses)
    count = get_count(expenses)
    category_totals = get_category_totals(expenses)
    need, want = necessary_vs_unnecessary(expenses, necessary_list, unnecessary_list)

    points, reasons = calculate_points(expenses, necessary_list, unnecessary_list, budget)

    st.metric("Transactions", count)
    st.metric("Total spent", f"{currency}{total:.2f}")

    st.write("### Category totals")
    st.json(category_totals)

    st.write("### Need vs Want")
    st.write(f"Necessary: {currency}{need:.2f}")
    st.write(f"Unnecessary: {currency}{want:.2f}")

    st.write("### Points")
    st.write(f"Total points: **{points}**")
    with st.expander("Why points changed"):
        for r in reasons:
            st.write("-", r)

    st.write("### Reflective insights")
    insights = reflective_insights(total, category_totals, need, want, budget)
    if isinstance(insights, str):
        st.write(insights)
    else:
        for i in insights:
            st.write("-", i)

    st.write("### All expenses")
    st.dataframe(expenses, use_container_width=True)
