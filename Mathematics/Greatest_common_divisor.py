"""
Question : find the greatest common factor for given two numbers.

by: frosthead, github: github.com/frost-head

example:
    input:
        a = 2, b = 4
    output:
        2
    explaination:
        2 is the highest number that divides both 2 and 4 completely.
"""
def GCD():
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    gcd = 1
    if a<b:
        for i in range(a+1,1,-1):
            if a % i == 0 and b % i == 0:
                gcd = i
                break
    else:
        for i in range(b+1,1,-1):
            if a % i == 0 and b % i == 0:
                gcd = i
                break

    return gcd

print(GCD())

"""
solution explaination:
    In the function GCD.
         We ask the user for two variables 'a' and 'b'.
         Then we set the gcd defualt to 1 because one is a common factor for every number. 
         Then we look for a condition where 'a' is smaller or 'b' is smaller.
            if a is smaller we traverse the range of 'a' in opposite manner i.e. if 'a' is 3 we traverse 3,2,1 in this fashion.
            then we check if 'i'(the number beign trversed) divides a and b completly if it do that we store 'i' in gcd and return.
        if 'b' is smaller we do the vice versa of opposite process.
Time Complexity:
    For the solution time complexity will be O(n) where n is the smaller number.

"""
