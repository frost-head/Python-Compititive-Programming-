"""
Find the digits in a factorial of the given number

Example :
    input = 5 
    output = 3

Explaination:
    factorial of 5 is 120 and 120 have 3 digits
    
By: Ayush github: github.com/frost-head
"""


import math

def digits_In_Factorial(int(input("Enter the Number"))):
    fact = 1 
    for i in range(1,N+1):
        fact *= i 
    return len(str(fact))


print(digits_In_Factorial())

"""
solution explaianation:
    in the function digits_In_factorial:
        we intialise fact as 1 because the factorail of zero is one and number less than 0 is not considered
        than we find the factorail of given number by multiplying the numbers till given number
        and at last return the len of the factorial simply by converting it into a str


Time Complexity for given solution is O(n)
"""
