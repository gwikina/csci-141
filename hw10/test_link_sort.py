"""
file: test_link_sort.py
author: your name here
description: tester for functions in linked_insort.py
"""

from linked_code import *
import linked_insort
from linked_insort import *

def read_file( fname ):
    """
       Open a file of containing one integer per line,
       prepend each integer to a linked sequence,
       and return the reverse of the sequence.
       :param fname: A string containing the name of the file
       :return: A linked list of the numbers in the file, ordered
                identically to how they are ordered in the file
    """

    file = open(fname)
    lst = []
    for line in file:
        line = line.strip()
        lst.append(int(line))
    file.close()
    lnk = mk_linked_list_rec( lst )
    return lnk  # Replace this line, too.


def main():
    """
       Read file, build sequence, print it, sort it, print result, and
       pretty-print both lists.
    """

    name = input( "Enter file name: " )
    print(read_file(name))

    if name == "":
        return

    original_s = read_file( name )
    print( "unsorted:", original_s )

    sorted_s = linked_insort.insort( original_s )

    print( "sorted:", sorted_s )

    print("pretty printed original: ", end="")
    linked_insort.pretty_print(original_s)
    print("pretty printed sorted: ", end="")
    linked_insort.pretty_print(sorted_s)


if __name__ == "__main__":
    main()
