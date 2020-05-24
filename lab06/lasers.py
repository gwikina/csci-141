""" 
file: biggiesort.py

description: takes a file annd then puts each line into a list, then sorts the file using a unique sorting algorithim

language: python3

author: glw3325 @ RIT.EDU

Gideon Wikina

"""


def readFile(filename):
        
    """

    opens a file and appends each line into a list

    strips the line of its spaces

    returns the list

    """
    
    file = open(filename)
    for line in file:
        lst = line.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst

def tower_location(filename):
    
    """

    prints all the tower locations 
    
    """
    
    laser_lst = readFile(filename)
    for i in range(0, len(laser_lst)):
        if i > 0 and i < (len(laser_lst)-2):
            print(i)
            print(laser_lst[i-1]+ laser_lst[i+1]+ laser_lst[i+2])
    for i in range(0, len(laser_lst)):
        if i > 1 and i < (len(laser_lst)-1):
            print(i)
            print(laser_lst[i-2]+ laser_lst[i-1]+ laser_lst[i+1])

def best_tower(filename, towers):
    
    """

    while the number of towers is greater than 0, it takes the maximum number of the list and calculates the sum depending on if the the laser is up on down

    compares each value to see which is higher and then prints out the number of towers decided, in greater to least
    

    """
    
    laser_lst = readFile(filename)
    while (towers > 0):
        max_number, max_index = 0, 0
        for i in range(0, len(laser_lst)):
            if i > 0 and i < len(laser_lst)-2:
                sum1 = (laser_lst[i-1] + laser_lst[i+1] + laser_lst[i+2])
                if sum1 > max_number:
                    max_number = sum1
                    max_index = i
                    is_up = True
        for i in range(0, len(laser_lst)):
            if i > 1 and i < len(laser_lst)-1:
                sum2 = (laser_lst[i-2] + laser_lst[i-1]+ laser_lst[i+1])
                if sum2 > max_number:
                    max_number = sum2
                    max_index = i
                    is_up = False
                    
        if is_up == True:
            print('Center at location ' + str(max_index) + ' facing upward scoring of ' + str(max_number) )
            laser_lst[max_index - 1] = 0
            laser_lst[max_index + 1] = 0
            laser_lst[max_index + 2] = 0
            
        else:
            print('Center at location ' + str(max_index) + ' facing downward scoring of ' + str(max_number) )
            laser_lst[max_index - 2] = 0
            laser_lst[max_index - 1] = 0
            laser_lst[max_index + 1] = 0
        towers = towers - 1 
        
def main():
    best_tower('lasers.txt', 3)
main()

