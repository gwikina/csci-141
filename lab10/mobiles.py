"""
file: mobiles.py
language: python3
author: CS.RIT.EDU
author: ##################### PUT YOUR NAME AND LOGIN ID HERE #####
description: Build mobiles using a tree data structure.
date: 10/2015, 11/2019
purpose: starter code for the tree mobiles lab
"""

############################################################
#                                                          #
#    IMPLEMENT THE STRUCTURE DEFINITIONS PER REQUIREMENTS, # 
#    AND                                                   #
#    IMPLEMENT THE MOBILE CREATION AND ANALYSIS FUNCTIONS. #
#        See the 'define structure here' text below,       #
#        the 'Create mobiles from mobile files' text,      #
#        and the heading 'mobile analysis functions'.      #
#                                                          #
#    (See also the 'pass' statements to replace.)          #
#                                                          #
############################################################

from dataclasses import dataclass
from typing import Union


############################################################
# structure definitions
############################################################

@dataclass
class Ball:
    """
    class Ball represents a ball of some weight hanging from a cord.
    field description:
    cord: length of the hanging cord in inches
    weight: weight of the ball in ounces (diameter of ball in a drawing)
    """
    cord: float
    weight: float
    # define structure here


@dataclass
class Rod:
    """
    class Rod represents a horizontal rod part of a mobile with
    a left-side mobile on the end of a left arm of some length,
    and a right-side mobile on the end of a right arm of some length.
    In the middle between the two arms is a cord of some length
    from which the rod instance hangs.
    field description:
    leftmobile: subordinate mobile is a mobile type.
    leftarm: length of the right arm in inches
    cord: length of the hanging cord in inches
    rightarm: length of the right arm in inches
    rightmobile: subordinate mobile is a mobile type.

    An assembled mobile has valid left and right subordinate mobiles;
    an unassembled mobile does not have valid subordinate mobiles.
    """

    # define structure here
    leftmobile: Union[None, 'Ball', 'Rod', str]
    leftarm: float
    cord: float
    rightarm: float
    rightmobile: Union[None, 'Ball', 'Rod', str]


#########################################################
# Create mobiles from mobile files
#########################################################

def read_mobile(file):
    """
    read_mobile : OpenFileObject -> Dictionary( Ball | Rod )
    read_mobile reads the open file's content and
    builds a mobile 'parts dictionary' from the specification in the file.
    The parts dictionary returned has components for assembling the mobile.
    If the mobile is a simple mobile, the returned value is
    a parts dictionary containing a Ball instance.
    If the mobile is complex, the returned value is a parts list of
    the Rod instance representing the top-most mobile component and
    the other parts.
    The connection point for each part is a string that identifies
    the key name of the part to be attached at that point.

    If there is an error in the mobile specification, then
    return an empty parts dictionary.

    # an example of the file format. 'B10' is key for the 10 oz ball.
    # blank lines and '#' comment lines are permitted.
    B10 40 10

    top B10 240 66 80 B30
    B30 55 30
    """
    parts = {}
    for line in file:
        line = line.strip()
        items = line.split()
        if items[0][0] == 'B':
            parts[items[0]] = Ball(float(items[1]), float(items[2]))
        elif items[0][0] == 'R':
            parts[items[0]] = Rod(items[1], float(items[2]), float(items[3]), float(items[4]), items[5])
        elif items[0] == 'top':
            if len(items) == 3:
                parts[items[0]] = Ball(float(items[1]), float(items[1]))
            elif len(items) == 6:
                parts[items[0]] = Rod(items[1], float(items[2]), float(items[3]), float(items[4]), items[5])
    return parts


def construct_mobile(parts):
    """
    construct_mobile : Dictionary( Rod | Ball ) -> Ball | Rod | NoneType

    construct_mobile reads the parts to put together the
    mobile's components and return a completed mobile object.
    The construct_mobile operation 'patches entries' in the parts.

    The parts dictionary has the components for assembling the mobile.
    Each Rod in parts has a key name of its left and right
    subordinate mobiles.  construct_mobile reads the key to
    get the subordinate part and attach it at the slot where
    the key was located within the component.

    The top mounting point of the mobile has key 'top' in parts.

    If the completed mobile object is a simple mobile, then
    the top returned value is a Ball instance.
    If the completed mobile is a complex mobile, then
    the top returned value is a Rod instance.

    If the parts dictionary contains no recognizable mobile specification,
    or there is an error in the mobile specification, then 
    return None.
    """
    for items in parts.values():
        if isinstance(items, Rod):
            items.leftmobile = parts[items.leftmobile]
            items.rightmobile = parts[items.rightmobile]
    if isinstance(parts['top'], Ball) or isinstance(parts['top'], Rod):
        return parts['top']
    else:
        return None

############################################################
# mobile analysis functions
############################################################

def is_balanced(the_mobile):
    """
    is_balanced : Mobile -> Boolean

    is_balanced is trivially True if the_mobile is a simple ball. 

    Otherwise the_mobile is balanced if the product of the left side
    arm length and the left side is approximately equal to the 
    product of the right side arm length and the right side, AND
    both the right and left subordinate mobiles are also balanced.

    The approximation of balance is measured by checking
    that the absolute value of the difference between
    the two products is less than 1.0.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """

    left_side = 0
    right_side = 0
    if the_mobile is None:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))
    if isinstance(the_mobile, Ball) is False  and  isinstance(the_mobile, Rod) is False:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))
    if isinstance(the_mobile, Ball):
        return True
    elif isinstance(the_mobile, Rod):
        left_side = weight(the_mobile.leftmobile) * the_mobile.leftarm
        right_side = weight(the_mobile.rightmobile) * the_mobile.rightarm
    if abs(left_side - right_side) < 1:
        return True
    else:
        return False


def weight(the_mobile):
    """
    weight : Mobile -> Number
    weight of the the_mobile is the total weight of all its Balls.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """
    if the_mobile is None:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))
    if isinstance(the_mobile, Ball) is False and isinstance(the_mobile, Rod) is False:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))
    if isinstance(the_mobile, Ball):
        return the_mobile.weight
    if isinstance(the_mobile.leftmobile, Ball) and isinstance(the_mobile.rightmobile, Ball):
        return the_mobile.leftmobile.weight + the_mobile.rightmobile.weight
    elif isinstance(the_mobile.leftmobile, Ball) and isinstance(the_mobile.rightmobile, Rod):
        return the_mobile.leftmobile.weight + weight(the_mobile.rightmobile)
    elif isinstance(the_mobile.rightmobile, Ball) and isinstance(the_mobile.leftmobile, Rod):
        return the_mobile.rightmobile.weight + weight(the_mobile.leftmobile)
    else:
        return the_mobile.leftmobile.weight + the_mobile.rightmobile.weight


def height(the_mobile):
    """
    height : the_mobile -> Number
    height of the the_mobile is the height of all tallest side.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """
    if the_mobile is None:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))
    if isinstance(the_mobile, Ball) is False and isinstance(the_mobile, Rod) is False:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))
    h = the_mobile.cord
    if isinstance(the_mobile, Ball):
        return h  + the_mobile.weight
    elif isinstance(the_mobile, Rod):
        left = height(the_mobile.leftmobile)
        right = height(the_mobile.rightmobile)
        if right >= left:
            return right + h
        else:
            return left + h


def main():
    file = open('f4.txt')
    mobile = construct_mobile(read_mobile(file))
    print('Weight: ', weight(mobile))
    print('Balanced:', is_balanced(mobile))
    print('Height: ', height(mobile))

main()