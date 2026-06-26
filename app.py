from utils.itinerary import generate_itinerary
from utils.budget import calculate_budget
from utils.hotels import get_hotels
from utils.restaurants import get_restaurants
from utils.weather import get_weather
from utils.maps import get_map
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/planner")
def planner():
    return render_template("planner.html")

@app.route("/result", methods=["POST"])
def result():

    destination = request.form["destination"]
    budget = request.form["budget"]
    days = request.form["days"]
    people = request.form["people"]
    style = request.form["style"]
    interest = request.form["interest"]

    itinerary = generate_itinerary(destination, days, interest)

    budget_data = calculate_budget(budget, days)

    hotels = get_hotels(style)

    restaurants = get_restaurants()

    weather = get_weather()

    map_link = get_map(destination)

    return render_template(

        "result.html",

        destination=destination,
        budget=budget,
        days=days,
        people=people,
        style=style,
        interest=interest,

        itinerary=itinerary,

        budget_data=budget_data,

        hotels=hotels,

        restaurants=restaurants,

        weather=weather,

        map_link=map_link

    )

if __name__ == "__main__":
    app.run(debug=True)