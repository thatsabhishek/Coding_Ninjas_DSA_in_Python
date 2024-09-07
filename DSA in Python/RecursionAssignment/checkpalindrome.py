# Determine if a given string 'S' is a palindrome using recurion. Return a Boolean value of true if it is a palindrome and false if it is not.

# Note: You ar enot required to print anything, just implement the function
# Example:
#     Input s = "racecar"
#     Output: true
#     Explanation: "racecar" is a plaindrome

def isPalindrome(str):
    if len(str)<=1:
        return True
    if str[0]!=str[len(str)-1]:
        return False
    return isPalindrome(str[1:-1])