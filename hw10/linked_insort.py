"""
file: linked_insort.py
author: glw3325
description: prints a sequence in an easy-to-read format, while sorting them with an insertion sort algorithm
Battled tested program :)))
"""

from linked_code import *


def insert( value, lnk ):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """
    if lnk is None:
        return LinkNode(value, None)
    elif value < lnk.value:
        return LinkNode(value, lnk)
    else:
        return LinkNode(lnk.value, insert(value, lnk.rest))


def insort( lnk ):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """

    # YOUR CODE HERE

    dummy_link = None
    while lnk is not None:
        if lnk is None:
            pass
        dummy_link = insert(lnk.value, dummy_link)
        lnk = lnk.rest
    return dummy_link

def pretty_print( lnk ):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """
    if lnk is None:
        print()
        return None
    string = str(lnk.value)
    while lnk is not None:
        string += ', ' + str(lnk.value)
        lnk = lnk.rest
    formatted_str = f'[{string[3:]}]'
    print(formatted_str)


