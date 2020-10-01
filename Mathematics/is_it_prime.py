"""
Question: Given a number "n" return where its prime or not.

By : Ayush, Github : https://github.com/frost-head

Example:
    Input: 3
    Output: Yes
"""


#Code - Brute force Solution
def IsItPrime_naive():
    n = int(input("Enter the number you want to test :"))
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

"""
Solution Explaination:
    In function IsItPrime_naive().
        first we ask user for input of a number.
        then we check whether its '1' if yes we straight return False as one is neither prime nor comosite
        then we travse the range of '2' to n.
            for 'i'(the number beign traversed)
                we see whether n is divisible by i or not if yes we return False, because prime numbers do not have divisor other than one and themselves.
            if there is no element in range that divides n: we return True.

Time complexity for naive approch:
    O(n) will be the time complexity for the worst case senario.
"""

#Code - Efficent approch
def IsItPrime_efficient():
    n = int(input("Enter the the number you want to test :"))
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True    

"""
Solution Explaination:
    In function IsItPrime_efficient().
        as perious solution we ask for number and check whether its one 
        but this time we only trverse root of n.that is while the number(i) times itself that is 'i*i'  is less than 'n'. because the factor appears in pairs.
   
Time Complexity.
    O(root of n) will be the time complexity.
"""



# Driver Code
if __name__ == "__main__":
    print("Choose the approch :\n 0 - Navive-approch \n 1 - Efficient-approch")
    while True:
        c = int(input("Enter your choice :"))
        if c == 0 or c == 1:
            break
        else:
            print("Enter a valid option")
            continue

    if c == 0:
        print(IsItPrime_naive())
    elif c == 1:
        print(IsItPrime_efficient())


