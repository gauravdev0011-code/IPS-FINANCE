def get_total(expenses):
    total = 0
    for el in expenses:
        total += el["amount"]
    return total    


def get_count(expenses): 
    return len(expenses)


def get_category_totals(expenses):
    totals = {}
    for el in expenses:
        cat = el["category"]

        if cat in totals:
            totals[cat] += el["amount"]
        else:
            totals[cat] = el["amount"]
    return totals