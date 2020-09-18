"""
Return the trailing Zeros in factorial of given number.

example:
    input: 5
    output: 1
Explaination:
    the factorial of 5 is 120 and it have one trailing zero.
"""
def Fact(n): # Finding the Factorial recursively
    if n == 0:
        return 1
    return n* Fact(n-1)

def Trailing_Zero(n): # Finding zeros
    sfact = list(str(Fact(n))) # geting factorial and converting to a list
    count = 0
    for i in range(len(sfact)-1,0,-1): # finding zeros
        if int(sfact[i]) % 10 == 0: 
            count += 1
        else:
            break
        
    return count

print(Trailing_Zero(10))

"""
Solution explaination:
    in Fact function we found the factorial of given number
    then in Trailing_zero function:
        we first converted the facotrial in a list
        then traversed thorugh the list in reverse fasion becuase we need the zeros in the last of factorial
        then checked for the zeros:
            here we checked if the current element is completly divisible by 10 or not, 
            if yes then we increment the zeros count 
            else we break the loop because any other zero after a non zero number will not be trailing
        at last we return the count.

Time complexity:
    if Factorial is given then time complexity will be O(b), where b is the number of zeros
    if Factorial not given then time complexity will be O(n), where n is the given number.
"""
