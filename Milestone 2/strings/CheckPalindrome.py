# Given a string, determine if it is a palindrome, considering only alphanumeric characters.
# Palindrome
# A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards and forwards.

# Sample Input 1 :
# abcdcba
# Sample Output 1 :
# true 

s = input()
r = s[::-1]

if s == r :
    print('true')
else:
    print('false')
    
# CN Code
from sys import stdin

def ispalindrome(string):
    left = 0
    right = len(string) - 1
    
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

#main
string = stdin.readline().strip()
ans = ispalindrome(string)
if ans:
    print("true")
else:
    print("false")