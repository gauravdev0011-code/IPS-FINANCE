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


def necessary_vs_unnecessary(expenses, necessary_list, unnecessary_list):
    need= 0
    want=0

    for el in expenses:
        if el["category"] in necessary_list:
            need += el["amount"]
        elif el["category"] in unnecessary_list:
            want += el["amount"]   
        else:
            print(f"Category {el['category']} is not classified as necessary or unnecessary.")

    return need, want            


def reflective_insights(total, category_totals, need, want, budget):
    insights = []

    if total == 0:
        return("No expenses provided.")
    if not category_totals:
        return("No category data provided.")    
    

    top_category = max(category_totals, key=category_totals.get)
    top_percent =(category_totals[top_category] / total) * 100
    insights.append(f"Most of your spending goes on {top_category} at {top_percent:.1f}% of your total expenses.")

    if budget > 0: 
        if total > budget:
            insights.append("You spent more than your budget, which indicates poor planning.")
        else:
            insights.append("You stayed within your budget, showing financial discipline.")
            insights.append(f"You have used {(total / budget) * 100:.1f}% of your budget.")

    if want > need:
        insights.append("Unnecessary spending is higher than necessary spending. Consider reviewing priorities.")

    else:
        insights.append("Necessary spending is higher than unnecessary spending. This shows controlled behavior.")

    return insights