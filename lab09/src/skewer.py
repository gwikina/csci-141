"""
A module for representing the skewer functionality.

author: RITCS
author: << YOUR NAME HERE >>
"""

from kebab_graphics import SkewerUI
from food import food_create
from kebab_spot import KebabSpot, spot_create, spot_size, spot_name, \
    spot_has, spot_string_em
from skewer_exception import SkewerException
from dataclasses import dataclass
from typing import Union
from kebab_spot import *

from lab09.src.kebab_spot import spot_vegan


@dataclass
class Skewer:
    """
    Class: Skewer
    Description: This class receives commands from Kebab and
        works with the KebabSpot class to represent a shish-kabob
        of food items on a skewer.
    """
    top: Union[None, KebabSpot]
    capacity: int
    ui: SkewerUI

def skewer_create(capacity):
    """
    Create a new empty skewer.
    :param capacity (int): the maximum number of items it can hold
    :exception SkewerException: a capacity less than 1 was specified.
    """
    if capacity < 1:
        raise SkewerException("Cannot create skewer!")

    return Skewer(top=None, capacity=capacity, ui=SkewerUI(capacity))

def skewer_add(skewer, name):
    """
    Add a food item to the skewer
    :param skewer (Skewer): this skewer
    :param name (str): the string name of the food item
    :exception SkewerException: item could not be added.
    :return None
    """
    if skewer.top is None or spot_size(skewer.top) < skewer.capacity:
        skewer.top = spot_create(food_create(name), skewer.top)
        skewer.ui.add(skewer.top)
    else:
        raise SkewerException("Cannot add item to a full skewer!")

def skewer_front(skewer):
    """
    Gets the name of the front item on the skewer.
    :param skewer (Skewer): this skewer
    :exception SkewerException: no item was on the skewer
    :return the name of the food item (string) on the front
    """
    if skewer.top is None:
        raise SkewerException("Cannot get item from an empty skewer!")
    return spot_name(skewer.top)

def skewer_remove(skewer):
    """
    Remove the front item from the skewer.
    :param skewer (Skewer): this skewer
    :exception: SkewerException: no item was on the skewer
    :return None
    """
    if skewer.top is None:
        raise SkewerException("Cannot get item from an empty skewer!")

    skewer.ui.remove()
    skewer.top = skewer.top.next

def skewer_size(skewer):
    """
    Get the number of elements on the skewer.
    :param skewer (Skewer): this skewer
    :return the number of elements (int)
    """
    if skewer.top is None:
        return 0
    else:
        return spot_size(skewer.top)

def skewer_capacity(skewer):
    """
    Get the maximum capacity of the skewer.
    :param skewer (Skewer): this skewer
    :return the capacity (int)
    """
    return skewer.capacity

def skewer_close(skewer):
    """
    On destruction, close the graphical window.
    :param skewer (Skewer): this skewer
    :return None
    """
    skewer.ui.close()

def skewer_has(skewer, name):
    """
    Is a particular food item on the skewer?
    :param skewer (Skewer): this skewer
    :param name: the name (string) of the food item to search for
    :return True if the item is on the skewer, False if not.
    """
    if skewer.top is None:
        return False
    else:
        return spot_has(skewer.top, name)

def skewer_string_em(skewer):
    """
    Return a string representation of the items on the skewer.
    :return A string containing all the items on the skewer, from front
    to back, comma separated, and surrounded with square brackets
    """
    return "[" + spot_string_em(skewer.top) + "]"



def skewer_calories(skewer):
    if skewer.top is None:
        return 0
    else:
        spot_vegan(skewer.top)


def skewer_vegan(skewer):
    return spot_vegan(skewer.top)