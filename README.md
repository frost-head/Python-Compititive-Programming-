# **Python-DSA**

## What is it?
#### This is a resource for the guys interested in Compitive programing or want to get a job in tech companies. 
Multiple solved programming questions are avilable (in python) here with explained solutions. Completely for free.

## How To use it Effectively?
Questions are sorted by the topics Like Maths, Arrays,etc. in there seprate folder. open the folder you want to learn topics about. you'll find questions in there. 
vist the Question. 
On the Top of the you'll see Details about the Question and the input output like this.
```python3
"""
Find the digits in a factorial of the given number
Example :
    input = 5 
    output = 3
Explaination:
    factorial of 5 is 120 and 120 have 3 digits
"""
```
then you'll find the Solution for the Question.
```python3
import math

def digits_In_Factorial(N):
    fact = 1 
    for i in range(1,N+1):
        fact *= i 
    return len(str(fact))


print(digits_In_Factorial(5))
```
at the end you'll find the explanation and time complexity of the Approch we took.
```python3
"""
solution explaianation:
    in the function digits_In_factorial:
        we intialise fact as 1 because the factorail of zero is one and number less than 0 is not considered
        than we find the factorail of given number by multiplying the numbers till given number
        and at last return the len of the factorial simply by converting it into a str
Time Complexity for given solution is O(n)
"""
```
*For Contribution Please Check [Contribution.md](https://github.com/frost-head/Python-Compititive-Programming-/blob/master/CONTRIBUTING.md) file*
