"""
A module that represents the valid food types.

author: RITCS
author: << YOUR NAME HERE >>
"""
from dataclasses import dataclass

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato', 'mushroom'}

# The set of vegetables
VEGGIES = {'onion', "pepper", 'tomato', 'mushroom'}   # TODO

# The calories for each food item (a dictionary, where 
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
    'mushroom': 7
}

@dataclass(frozen=True)
class Food:
    name: str
    veggie: bool
    calories: int


def food_create(name):
    """
    Create a new food item.
    :param name: the name of the food
    :return: new Food object
    """
    n = name
    if name in VEGGIES:
        v = True
    else:
        v = False
    for key in CALORIES:
        if name == key:
            c = CALORIES[key]
    return Food(n, v, c)
