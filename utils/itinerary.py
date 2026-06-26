def generate_itinerary(destination, days, interest):

    itinerary = []

    for day in range(1, int(days) + 1):

        itinerary.append({
            "day": day,
            "title": f"Day {day}",
            "activity": f"Explore {destination} with a focus on {interest}."
        })

    return itinerary