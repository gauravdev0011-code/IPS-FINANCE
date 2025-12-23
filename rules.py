def calculate_points(expenses, necessary_categories, unnecessary_categories, budget):
    points = 0
    reasons = []

    total_expenses = sum(el["amount"] for el in expenses)
    necessary_amount = 0
    unnecessary_amount = 0

    for el in expenses:
        category = el["category"]
        amount = el["amount"]

        if category in necessary_categories:
            points += 2
            necessary_amount += amount
            reasons.append(f"+2: necessary expense ({category})")

        elif category in unnecessary_categories:
            points -= 3
            unnecessary_amount += amount
            reasons.append(f"-3: unnecessary expense ({category})")

        else:
            reasons.append(f"0: category not classified ({category})")

    # Budget rule
    if total_expenses <= budget:
        points += 5
        reasons.append("+5: stayed within budget")
    else:
        points -= 10
        reasons.append("-10: exceeded budget")

    # Need vs want rule
    if necessary_amount > unnecessary_amount:
        points += 3
        reasons.append("+3: spent more on necessary than unnecessary")
    elif unnecessary_amount > necessary_amount:
        points -= 10
        reasons.append("-10: spent more on unnecessary than necessary")
    else:
        reasons.append("0: equal necessary and unnecessary spending")

    return points, reasons









    