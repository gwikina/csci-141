""" 
file: bumpersort.py

description: takes a file annd then puts each line into a list, then sorts the file using a unique sorting algorithim

language: python3

author: glw3325 @ RIT.EDU

Gideon Wikina

"""
import random
import time
from merge_sort import merge_sort
from quick_sort import quick_sort
def bumper_sort(lst, k):
    
    """
    Creates a list hist of length k + 1, initialize each element to 0. (“hist” stands for histogram.)

    Uses the elements of data to index into hist. Executes a loop over the values of data, and every time you see a value increment (bump) the count of that value in hist[i]

    Using a loop, as many times as the value in hist[i], append i to result. That is, you append i to result hist[i] number of times. 
    
    """
    
    hist = [0] * (k+1)
    c = 0
    result = []
    for i in lst:
        hist[i] = hist[i] + 1
    #print(hist)
    for i in hist:
        while i > 0:
            result.append(c)
            i = i - 1
        c = c+1
    return  result
def find_max(lst):

    # defines max num as the first element of the list
    
    # iterates through list and checks if a number is bigger than the max and if the number is, it becomes the new max
    
    max_number = lst[0]
    for number in lst:
        if number > max_number:
            max_number = number
    return max_number
def random_lst(number_of_elements, first, last):
    
    # Creates a list of a defined number of elements within a specific range (first, last)
    
    lst = []
    for i in range(0, number_of_elements):
        lst.append(random.randrange(first, last))
    return lst
def main():

    """

    prints and sorts both data of a large and small stature

    compares the times of different sorting algorithims 
    
    """
    data = [2,5,3,0,2,3,0,3]
    print('Small list, unsorted: ' + str(data))
    data_after = bumper_sort(data, find_max(data))
    print('Small list, bump-sorted: ' + str(data_after))
    
    new_lst =  random_lst(1000, 0, 300)
    print()
    print('Large list, unsorted: ' + str(new_lst))
    
    sorted_new_lst = bumper_sort(new_lst, find_max(new_lst))
    print()
    print('Large list, bump-sorted: ' + str(sorted_new_lst))

    print()
    print('Sorting a randomized list of 1000 element')
    start = time.process_time()
    answer = merge_sort(new_lst)
    end = time.process_time()
    print( "Merge sort in: " + str(end - start) + 'seconds')
    start = time.process_time()
    answer = quick_sort(new_lst)
    end = time.process_time()
    print( "Quick Sort in: " + str(end - start) + 'seconds')
    start = time.process_time()
    answer = bumper_sort(new_lst, find_max(new_lst))
    end = time.process_time()
    print( "Bumper Sort in: " + str(end - start) + 'seconds')
    start = time.process_time()
    answer = sorted(new_lst)
    end = time.process_time()
    print( "Sorted in: " + str(end - start) + 'seconds')

    print()
    print('Sorting a randomized list of 1000000 element')
    new_lst =  random_lst(1000000, 0, 300)
    start = time.process_time()
    answer = merge_sort(new_lst)
    end = time.process_time()
    print( "Merge sort in: " + str(end - start) + 'seconds')
    start = time.process_time()
    answer = quick_sort(new_lst)
    end = time.process_time()
    print( "Quick Sort in: " + str(end - start) + 'seconds')
    start = time.process_time()
    answer = bumper_sort(new_lst, find_max(new_lst))
    end = time.process_time()
    print( "Bumper Sort in: " + str(end - start) + 'seconds')
    start = time.process_time()
    answer = sorted(new_lst)
    end = time.process_time()
    print( "Sorted in: " + str(end - start) + 'seconds')
    
main()
    
    
