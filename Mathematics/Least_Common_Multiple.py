"""
Question :
    Find the least common multiple of two numbers.

By : Ayush , github: https://github.com/frost-head

Example:
    Input: a = 6 , b = 4
    
    Output: 12
"""

#Code
def LCM():
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))

    c = a*b
    d = max(a,b)
    for i in range(d,c+1):
        if i%a == 0 and i%b == 0:
            return i 

print(LCM())


"""
Solution Explaination:
    In function LCM.
        we first take two numbers from user.
        then we multiply them and store the value of bigger number in a variable.
        now we traverse through the range of numbers between the bigger number and the value of there multiplication. Because LCM will be between them now we look for the number that is divisible by both "a" and "b". if yes then we return it.

Time Complexity:
    time complexity for given solution will be O(a*b - max(a,b)).
"""

