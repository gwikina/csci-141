"""
file: linked_insort.py
author: glw3325
description: returns dna sequence (linked list) with various different conversions and related operations
"""
import linked_code # in case student's dna module didn't import
from dataclasses import dataclass
from typing import Any, Union
from lab08.linked_code import *


@dataclass(frozen=True)
class LinkNode:
    """
    A singly linked node structure
    :field value: the element value stored in this node, i.e.,
                  at the head of this sequence
    "field rest: a reference to the next node in the sequence, i.e.,
                 the tail of this sequence
    """
    value: Any
    rest: Union[None, 'LinkNode']


def convert_to_nodes(input_str):
    """
    takes first element of a string a places it at the head of the node recursively and then uses the rest of the linked
    list to get the rest of the values
    :param input_str: takes a string
    :return: A linked list that each node is of a character in the string

    """
    if input_str == "":
        return None
    elif len(input_str) <= 1:
        return LinkNode(input_str[0], None)
    else:
        return LinkNode(input_str[0], convert_to_nodes(input_str[1:]))


def convert_to_string(node):
    """
    takes each value of the linked list and adds it to an empty string
    :param node: takes in a linked list
    :return: a string of each value in the linked list

    """
    string = ""
    if node is None:
        return ""
    while node is not None:
        string += str(node.value)
        node = node.rest
    return string


def is_match(dna_seq1, dna_seq2):
    """
    :param dna_seq1: first linked list for comparision
    :param dna_seq2: second linked list for comparision
    :return: boolean expression that determines if the sequences are equivalent to each other

    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif (dna_seq1 is None and dna_seq2 is not None) or (dna_seq1 is not None and dna_seq2 is None):
        return False
    elif (dna_seq1.rest is None and dna_seq2.rest is None) and dna_seq1.value == dna_seq2.value:
        return True
    elif dna_seq1.value == dna_seq2.value:
        return is_match(dna_seq1.rest, dna_seq2.rest)
    else:
        return False


def is_pairing(dna_seq1, dna_seq2):
    """
    :param dna_seq1:  first linked list for comparision
    :param dna_seq2:  second linked list for comparision
    :return: boolean expression to show if the sequences is a pairing (A with T and G with C)

    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    if (dna_seq1 is None and dna_seq2 is not None) or (dna_seq1 is not None and dna_seq2 is None):
        return False
    if length_iter(dna_seq1) != length_iter(dna_seq2):
        return False
    else:
        length = length_iter(dna_seq1)
        if dna_seq1.value == 'A' and dna_seq2.value== 'T':
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        elif dna_seq1.value == 'T' and  dna_seq2.value == 'A':
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        elif dna_seq1.value == 'G' and dna_seq2.value == 'C':
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        elif dna_seq1.value == 'C' and dna_seq2.value == 'G':
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        else:
            return False


def is_palindrome(dna_seq):
    """
    :param dna_seq: sequence that we are checking
    :return: boolean expression hat determines if the the reverse is equal to the the original

    """
    if dna_seq is None:
        return True
    elif is_match(dna_seq, reverse_iter(dna_seq)):
        return True
    else:
        return False


def substitution(dna_seq, index, base):
    """
    :param dna_seq: sequence that we are checking
    :param index: index that we are starting with
    :param base: new base to be substituted
    :return: new linked list that removes the values of a certain position and inserts the new base where it was
    """
    if base is None:
        return dna_seq
    elif index == 0:
        dna_seq = remove_at(0, dna_seq)
        return insert_at(0, base, dna_seq)
    elif dna_seq.value is None:
        raise IndexError('Invalid Insertion Index')
    else:
        return LinkNode(dna_seq.value, substitution(dna_seq.rest, index-1, base))


def insertion(dna_seq1, dna_seq2, index):
    """
    :param dna_seq1: first sequence
    :param dna_seq2: second sequence
    :param index: index to be insert the second sequence at
    :return: new linked list with the new added in the position thar=t it needed to be

    """
    if index > 0 and dna_seq1.value is not None:
        return LinkNode(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, index-1))
    else:
        return concatenate(dna_seq2, dna_seq1)


def deletion(dna_seq, index, segment_size):
    """
    :param dna_seq: sequence of which will be deleted
    :param index: index where the deletion begins
    :param segment_size: number of elements to be deleted
    :return: new linked list that represents the result of the deletion
    """
    if segment_size == 0:
        return dna_seq
    elif index == 0:
        while segment_size > 0:
            dna_seq = remove_at(0, dna_seq)
            segment_size = segment_size - 1
        return dna_seq
    elif dna_seq is None:
        raise IndexError('Invalid Index')
    else:
        return LinkNode(dna_seq.value, deletion(dna_seq.rest, index - 1, segment_size))


def duplication(dna_seq, index, segment_size):
    """
    :param dna_seq: sequence of which the segment is copied
    :param index: index which duplication begins
    :param segment_size: number of  elements to be duplicated
    :return: new linked list that represents the linked list after the segment has been copied and inserted into the
    next index position from which the copying ends
    """
    if segment_size == 0:
        return dna_seq
    elif index < 0 or index > length_iter(dna_seq)-1 or segment_size < 0 or index + segment_size > length_iter(dna_seq):
        raise IndexError('Invalid Index')
    elif dna_seq is None:
        raise IndexError('Invalid Index')
    else:
        temp_index = index
        increase = 0
        temp_dna = None
        while segment_size > 0:
            temp_dna = insert_at(increase, value_at(dna_seq, temp_index),  temp_dna)
            segment_size = segment_size - 1
            temp_index = temp_index + 1
            increase = increase + 1
        return insertion(dna_seq, temp_dna, index)


