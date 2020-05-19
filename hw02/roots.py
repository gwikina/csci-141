""" 
file: roots.py
description: solves the quadratic equation bytaking in parameters
language: python3
author: glw3325 @ RIT.EDU
Gideon Wikina
"""
import math
def printEquation(a,b,c):
    """ prints the quadratic equation i its truest form """
    equation = f'{a}x^2 + {b}x + {c} = 0'
    print(equation)
def determinant(a, b, c):
    """ solves and returns the determinant
    """
    determinant_num = (b**2) - (4*a*c)
    return determinant_num
def checkForNoRoots(a,b,c):
    """ prints no roots
    """
    determinant_num = determinant(a, b, c)
    printEquation(a,b,c)
    print('No roots')
def checkForOneRoot(a,b,c):
    """ prints "one root" and then solves for it """
    determinant_num = determinant(a, b, c)
    root = (-b + math.sqrt(determinant(a, b, c))) / (2*a)
    root_answer = f'x = {root}'
    printEquation(a,b,c)
    print('One root')
    print(root_answer)
def checkForTwoRoots(a,b,c):
    """ prints "two roots" and then solves for them """
    determinant_num = determinant(a, b, c)
    first_root = (-b + math.sqrt(determinant(a, b, c))) / (2*a)
    second_root=  (-b - math.sqrt(determinant(a, b, c))) / (2*a)
    root1_answer = f'x = {first_root}'
    root2_answer = f'x = {second_root}'
    printEquation(a,b,c)
    print('Two roots')
    print(root1_answer)
    print(root2_answer)
def quadratic_roots(a,b,c):
    """
    checks that there are no roots
    uses the detterminant to complete the quadratic formula
    provides if-else statements to see that how many roots are present """
    determinant_num = determinant(a, b, c)
    if (determinant_num  < 0):
       checkForNoRoots(a,b,c)
    elif(determinant_num  == 0):
        checkForOneRoot(a,b,c)
    elif(determinant_num  > 0):
        checkForTwoRoots(a,b,c)
    else:
        print('Invalid Entry')
def runCases():
    """
    runs 10 distinct cases
    
    """
    quadratic_roots(2,-11,-21)
    quadratic_roots(4,1,4)
    quadratic_roots(1,0,0)
    quadratic_roots(1,2,1)
    quadratic_roots(1,1,1)
    quadratic_roots(-1,-1,-1)
    quadratic_roots(1,0,-4)
    quadratic_roots(1,1,0)
    quadratic_roots(1,9,0)
    quadratic_roots(-5,-2,1)
def main():
    """
    Ask user to input an A, B , and C

    Prints two lines for spacing

    runs quadraticc_roots with the user's inputted values
    
    """
    a = int(input('Enter A: '))
    b = int(input('Enter B: '))
    c = int(input('Enter C: '))
    print()
    print()
    quadratic_roots(a,b,c)
runCases()
main()
    
    
    


    
        
