from flask import Flask, jsonify, request, render_template
import json
from datetime import datetime
import random

app = Flask(__name__)

MEALS_DB = {
    "breakfast": [
        {
            "name": "Oatmeal with Fruits",
            "calories": 350,
            "protein": 12,
            "carbs": 60,
            "fats": 8,
            "ingredients": ["oats", "banana", "berries", "honey", "almonds"],
        },
        {
            "name": "Eggs and Toast",
            "calories": 400,
            "protein": 20,
            "carbs": 35,
            "fats": 15,
            "ingredients": ["eggs", "whole grain bread", "avocado", "tomatoes"],
        },
    ],
    "lunch": [
        {
            "name": "Chicken Salad",
            "calories": 450,
            "protein": 35,
            "carbs": 25,
            "fats": 20,
            "ingredients": [
                "chicken breast",
                "mixed greens",
                "olive oil",
                "cucumber",
                "tomatoes",
            ],
        },
        {
            "name": "Quinoa Bowl",
            "calories": 420,
            "protein": 18,
            "carbs": 65,
            "fats": 15,
            "ingredients": [
                "quinoa",
                "black beans",
                "corn",
                "avocado",
                "lime",
                "cherry tomatoes",
            ],
        },
    ],
    "dinner": [
        {
            "name": "Grilled Salmon",
            "calories": 500,
            "protein": 40,
            "carbs": 30,
            "fats": 25,
            "ingredients": ["salmon", "brown rice", "broccoli", "lemon"],
        },
        {
            "name": "Stir-Fried Tofu",
            "calories": 450,
            "protein": 25,
            "carbs": 45,
            "fats": 20,
            "ingredients": [
                "tofu",
                "brown rice",
                "mixed vegetables",
                "soy sauce",
                "ginger",
            ],
        },
    ],
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/meals")
def get_meals():
    return render_template("meals.html", meals=MEALS_DB)


@app.route("/create_plan")
def plan_page():
    return render_template("create_plan.html")


@app.route("/generate_plan", methods=["POST"])
def generate_plan():
    days = int(request.form.get("days", 1))
    if days < 1 or days > 7:
        return jsonify({"error": "Days should be between 1 and 7"}), 400

    meal_plan = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "days": {},
    }

    # Keep track of previous day's meals to avoid repetition
    prev_lunch = None
    prev_dinner = None

    for day in range(1, days + 1):
        # Randomly select breakfast
        breakfast = random.choice(MEALS_DB["breakfast"])

        # Select lunch avoiding previous day's choice
        available_lunches = [
            lunch for lunch in MEALS_DB["lunch"] if lunch != prev_lunch
        ]
        lunch = random.choice(available_lunches)
        prev_lunch = lunch

        # Select dinner avoiding previous day's choice
        available_dinners = [
            dinner for dinner in MEALS_DB["dinner"] if dinner != prev_dinner
        ]
        dinner = random.choice(available_dinners)
        prev_dinner = dinner

        meal_plan["days"][f"day_{day}"] = {
            "breakfast": breakfast,
            "lunch": lunch,
            "dinner": dinner,
            "total_calories": sum(
                [
                    breakfast["calories"],
                    lunch["calories"],
                    dinner["calories"],
                ]
            ),
        }

    return render_template("plan_result.html", plan=meal_plan)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
