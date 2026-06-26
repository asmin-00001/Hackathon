def get_hotels(style):

    hotels = {

        "Budget": [
            "Backpackers Inn",
            "Budget Stay Hotel",
            "Mountain Hostel"
        ],

        "Luxury": [
            "Grand Palace Hotel",
            "Luxury Resort",
            "Royal Suites"
        ],

        "Family": [
            "Family Paradise",
            "Holiday Resort",
            "Comfort Hotel"
        ],

        "Solo": [
            "Solo Hostel",
            "Traveller's Home",
            "Nomad Inn"
        ],

        "Backpacking": [
            "Adventure Hostel",
            "Nomad Base",
            "Camp Lodge"
        ]
    }

    return hotels.get(style, [])