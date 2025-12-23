import json

ACCOUNT_FILE = "account.json"

def read_account():
    try:
        with open(ACCOUNT_FILE, "r") as f:
            account = json.load(f)
            return account
    except (FileNotFoundError, json.JSONDecodeError):
        return {"balance": 0, "budget": 0, "points": 0}    
    

def save_account(account):
    with open(ACCOUNT_FILE, "w") as f:
        json.dump(account, f, indent=4)


def set_balance(balance):
    account= read_account()
    account["balance"] = balance
    save_account(account)
    return account

def set_budget(budget):
    account= read_account()
    account["budget"] = budget
    save_account(account)
    return account

def set_points(points_to_add):
    account= read_account()
    account["points"] = points_to_add
    save_account(account)
    return account
            
def subtract_from_balance(amount):
    account=read_account()
    account["balance"] -= amount
    save_account(account)
    return account