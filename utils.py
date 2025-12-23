def ask_float(message):
    while True:
        try:
            return float(input(message))
        except:
            print("Please enter a valid number.")

def ask_text(message):
    return input(message).strip().lower()       

def ask_date(message):
    return input(message).strip()

def get_user_category():
    necessary = input("Enter necessary categories (comma separated)\n"
        "Example: groceries,rent,car_payment\n> "
    )
    unnecessary = input(
        "Enter unnecessary categories (comma separated)\n"
        "Example: entertainment,dining_out\n> "
    )

    necessary_list = [el.strip().lower() for el in necessary.split(",") if el.strip()]
    unnecessary_list = [el.strip().lower() for el in unnecessary.split(",") if el.strip()]

    return necessary_list, unnecessary_list

def get_expense_input():
    amount = ask_float("Enter the amount: ")
    category = ask_text("Enter the category: ")
    note = ask_text("Enter a note (optional): ")
    date = ask_date("Enter the date (YYYY-MM-DD): ")            
    payment_method = ask_text("Enter the payment method: ") 
    merchant = ask_text("Enter the merchant name: ")
    location = ask_text("Enter the location: ")

    return amount, category, note, date, payment_method, merchant, location

