"""
file: droid_factory.py
language: python3
author: Gideon Wikina
author: glw3325 @ rit.edu
description:
"""
from _ctypes import Union
from node import Node
from cs_queue import *
from dataclasses import dataclass
from typing import Any, Union
import sys


@dataclass
class Droid:
    # defines a class for the Droid gives attributes of a serial num and body parts
    serial_number: int  # number of elements in the queue
    head: str  # the front element in the queue
    body: str  # the back element in the queue
    arms: str  # the back element in the queue
    legs: str  # the back element in the queue


def unload(filename, belt):
    """
    pre-condition: assume file exist
    :param filename: name of file which has all the parts
    :param belt: The queue in which the parts will be loaded onto
    :return: The belt that is a product of all parts in the file enqueued onto the belt
    """
    file = open(filename)
    for line in file:
        enqueue(belt, line.strip())
    return belt


def test_unload():
    # unloading unto an empty belt
    belt = Queue(0, None, None)
    print(unload('droid_parts_3.txt', belt))
    print(unload('droid_parts_5.txt', belt))
    print(unload('droid_parts_20.txt', belt))
    # unloading onto a non empty belt
    belt = unload('droid_parts_1.txt', belt)
    print(unload('droid_parts_5.txt', belt))


def is_empty(belt):
    """
    :param belt: the queue in which holds all the Droid parts
    :return: a boolean expression that results from checking if the size of the belt is 0 or if the belt is empty
    """
    if belt.size == 0:
        return True
    return False


def test_is_empty():
    # checking empty: expecting (True)
    belt = Queue(0, None, None)
    if is_empty(belt) is True:
        print(True)
    else:
        print(False)
    # checking not empty: expecting (False)
    belt = unload('droid_parts_1.txt', belt)
    if is_empty(belt) is False:
        print(True)
    else:
        print(False)


def build_droid(serial_number, belt):
    """
    :param serial_number: the number assigned to the Droid for identification
    :param belt: the queue in which holds all the Droid parts
    :post-condition: prints out all the processes that are happening in the droid factory
    """
    if is_empty(belt):
        # if empty, print a message and then leave the function
        print('No parts today, I am guessing the clone wars are over. Roger! Roger!')
        return
    new_droid = Droid(serial_number, '', '', '', '')
    print('Building new Droid with serial number ' + str(new_droid.serial_number))
    while new_droid != Droid(serial_number, 'head', 'body', 'arms', 'legs'):
        # while the new_droid is incomplete remove parts from the queue
        removed = dequeue(belt)
        if new_droid.head == removed or new_droid.body == removed or new_droid.arms == removed or new_droid.legs == removed:
            # if the new_droid already has a part, put the part in the back of the queue
            enqueue(belt, removed)
            print('placing unneeded part back on belt: ' + removed)
        else:
            # if it is a new part, assign it to its correct place
            if removed == 'head':
                new_droid.head = removed
                print('attaching ' + new_droid.head + '...')
            elif removed == 'body':
                new_droid.body = removed
                print('attaching ' + new_droid.body + '...')
            elif removed == 'arms':
                new_droid.arms = removed
                print('attaching ' + new_droid.arms + '...')
            elif removed == 'legs':
                new_droid.legs = 'legs'
                print('attaching ' + new_droid.legs + '...')
    print('Droid ' + str(new_droid.serial_number) + ' has been assembled')


def test_build_droid():
    # build from empty Queue: expected just a print message
    belt = Queue(0, None, None)
    build_droid(10000, belt)
    # build single droid from a queue with just enough parts for one Droid
    belt = unload('droid_parts_1.txt', belt)
    build_droid(10000, belt)
    # build single droid from a queue with more than enough parts for one Droid
    belt = unload('droid_parts_5.txt', belt)
    build_droid(10000, belt)


def build_all(belt):
    """
    :param belt: the queue in which holds all the Droid parts
    :post-condition: builds a droid until the queue is empty and increments the serial number per Droid
    """
    serial_num_base = 10000
    times = 0
    if is_empty(belt):
        # if empty, print a message and then leave the function
        print('No parts today, I am guessing the clone wars are over. Roger! Roger!')
        print()
        return
    while belt.back is not None:
        build_droid(serial_num_base + times, belt)
        print()
        times += 1
    print('All of the droids have been assembled! Time to clock out and play Sabacc...')


def test_build_all():
    # build from empty Queue: expected just a print message
    belt = Queue(0, None, None)
    build_all(belt)
    # build single droid from a queue with just enough parts for one Droid
    belt = unload('droid_parts_1.txt', belt)
    build_all(belt)
    # build single droid from a queue with more than enough parts for one Droid
    belt = unload('droid_parts_20.txt', belt)
    build_all(belt)


def main():
    """
    test_unload()
    test_is_empty()
    test_build_droid()
    test_build_all()
    """
    if len(sys.argv)!=2:
        print("Usage: filename")
    else:
        filename = sys.argv[1]
        belt = Queue(0, None, None)
        belt = unload(filename, belt)
        build_all(belt)


main()
