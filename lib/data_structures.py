spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    pass
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

spicy_food_american = get_spicy_food_by_cuisine(spicy_foods, "American")
print(spicy_food_american)        

def print_spiciest_foods(spicy_foods):
    pass
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]

        if food["heat_level"] > 5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    pass
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)      # num_foods is assigned the value of the length of the list spicy_foods, which is 3

    return total_heat_level // num_spicy_foods

def create_spicy_food(spicy_foods, spicy_food):
    pass
    # copying the original list to avoid modifying it directly.
    updated_spicy_foods = spicy_foods.copy()
    # adding the new_spicy_food to the list
    updated_spicy_foods.append(new_spicy_food)

    return updated_spicy_foods

# example usage:

new_spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print(updated_spicy_foods)