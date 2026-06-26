def calculate_budget(total_budget, days):

    total_budget = float(total_budget)
    days = int(days)

    hotel = total_budget * 0.40
    food = total_budget * 0.25
    transport = total_budget * 0.20
    activities = total_budget * 0.15

    return {
        "Hotel": round(hotel, 2),
        "Food": round(food, 2),
        "Transport": round(transport, 2),
        "Activities": round(activities, 2),
        "Per Day": round(total_budget / days, 2)
    }