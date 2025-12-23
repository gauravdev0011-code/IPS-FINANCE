def get_user_category():
    necessary = input("Enter necesssary categories \nExample: groceries,rent,car_payment \n: ")
    unnecessary = input("Enter unnecessary categories \nExample: entertainment, dining_out \n: ")

    necessary_list = [el.strip().lower() for el in necessary.split(",")]
    unnecessary_list = [el.strip().lower() for el in unnecessary.split(",")]

    return necessary_list, unnecessary_list