""" 
file: biggiesort.py

description: takes a file annd then puts each line into a list, then sorts the file using a unique sorting algorithim

language: python3

author: glw3325 @ RIT.EDU

Gideon Wikina


1) In what kind of test case does insertion sort perform better than biggie sort? Clearly describe the test case.

The test case in which insertion sort performs better than biggie sort is when the list is already or close to being sort as inserition sort will minimum time O(n) when elements are already sorted.
For example, if you had, 5,6,7,8 and tried to sort it the case would run faster than biggie sort. 


2) Why does biggie sort perform worse than insertion sort in that test case?

With insertion sort, it compares adjacent pairs with logical operators, but with biggie sort it still haas to iterates through the loop at least once in order to find the max index and then again to swap. So in this case
insertion sort will always be faster that biggie sort.

"""
def find_max(lst, first, end):
    
    """

    first it finds the number that holds the  most value in the list, from a given index position

    then it iterates through the lst to find the index position of said max number

    returns the index position of the max number

    """
    
    max_number = lst[first]
    max_index = first
    for number in lst[first:end] :
        if number > max_number:
            max_number = number
    for i in range(len(lst)):
        if lst[i] == max_number:
            max_index = i
    return max_index
def swap(lst,end, max_index):
    
    """

    while the end of list is greater than 0, it iterates through the list

    if the list item is equal to the maximum value in the list it will swap the position between the end of the list and its current position

    the the end of the list will decrease by one because you are trying the correct max is already at the end

    the max index will change as our end changes to find the max between 0 and our new end

    returns the list

    """
    
    while end > 0:                      #while end of our list comparsion is greater than 0
        for i in range(len(lst)):
            if lst[i] == lst[max_index]:
                temp = lst[end-1]
                lst[end-1] = lst[i]
                lst[i] = temp
                end = end -1
                max_index = find_max(lst, 0, end)
    return lst
def biggie_sort(lst):
    
    """

    for every value in the list, it will check if a swap is in order

    returns the sorted list

    """
    
    for mark in range(len(lst) - 1):
        swap(lst,len(lst), find_max(lst,0, len(lst)))
    return lst
def read_unsorted_list(filename):
    
    """

    opens a file and appends each line into a list

    strips the line of its spaces

    returns the list

    """
    
    file = open(filename)
    lst = []
    for line in file:
        lst.append(int(line.strip()))
    return lst
def main():
    
    """

    Prompt for an input file name
    
    Open the file, read the file, and store the data in a list and then prints the list
    
    Call your biggie sort procedure passing the list
    
    Reprint the  sorted list 

    """
    
    filename = input('Enter the file name: ')
    unsorted_list = read_unsorted_list(filename)
    msg1 = f'Unsorted list: {unsorted_list}'
    print()
    print(msg1)
    sorted_list = biggie_sort(unsorted_list)
    msg2 = f'Sorted list: {sorted_list}'
    print()
    print(msg2)
main()
