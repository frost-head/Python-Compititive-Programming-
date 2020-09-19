"""
Check wheather the given number is a palindrome number or not.

Example:
    input = 252
    output = True
    
    Explaination:
        if we right 252 in reverse it will be the same as input, Hence it is a palindrome number.

Note: Every single digit number is a pailndrome number.

By: Ayush ,Github: github.com/frost-head

"""
def isPalindrome(I = int(input("Please enter the number you want to test: "))):
	rev = 0 
	temp = I
	j = temp
	while j > 0:
		temp = j % 10
		rev = rev * 10 + temp
		j = j//10
	if rev == I:
		return True
	else:
		return False
	

print(isPalindrome())

"""
Solution Explaination:
    In function isPalindrome:
        first we intialise rev as 0 and make a temp variable same as inputed number
        then we traverse through the j in reverse manner but instead of decrementing 1 we divide j by 10 that means we are removing the unit place
            eg: 454//10 = 45
        in loop first we are storing the value of unit digit in temp
            eg: if j is 454 we are storing 4 in it, in next iteration it will be 5 and so on.
        then putting that in rev
             eg: if rev is 0,then store 3, for the next iteration it will become 32 in number 123
        after j becomes less than 0, we break
        then we check whether rev is same as inputed number if yes we return True else return False

Time Complexity : O(x), where x will be the number of digits in the inputed number.
"""
