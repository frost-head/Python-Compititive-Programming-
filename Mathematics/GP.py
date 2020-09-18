"""
Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

example:
    input:  a = 2 
            b = 4
            n = 10
    output: 1024
explanantion:
    at the 10th value of given gp would be 1024.
    
By: Ayush github: github.com/frost-head
"""

def GP(a,b,n):
    r = b/a
    return a*(r**(n-1))


print(GP(2,4,10))

"""
solution explaination:
    in GP function:
        first we find r by dividing a and b
        then we return the value of a*(r**(n-1)), which is the formula to find the nth term of GP
time Complexity:
    the solution will solve it in O(1) because we are using a constant function to solve the problem.
"""
