"""
Question :
    given the constants(a,b,c) of a Quadratic Eq find the roots of Eq.

Example:
    input:
        a = 3
        b = 5 
        c = -7
    output:
        x = 0, y = -3
"""

# CODE
import math

def quadraticRoots():
    a = int(input("Enter a :"))
    b = int(input("Enter b :"))
    c = int(input("Enter c :"))
    d = (b**2) - (4*a*c)
    if d<0:
        print("Imaginary")
    else:
        x = int( ((-b) + (d**(1/2)) )//(2*a) ) 
        y = int( ((-b) - (d**(1/2)) )//(2*a) )
        print(f' x = {x}, y = {y}')
    
quadraticRoots()


"""
Solution explaination:
    In function quadraticRoots().
        We fist ask user the constants of the quation.(a,b,c)
        then we check whether roots of eq are real or imaginary by b^2 - 4ac. you can look for the use of quadratic formula on internet.
        if roots are imaginary we print roots are imaginary.
        else we use quadratic formula((-b +- root(b^2 - 4ac))/2a) to print the values of x and y.
Time Complexity:
    The given solution will have a time complexity of O(1), as we are using a formula that will take constant time.
"""
