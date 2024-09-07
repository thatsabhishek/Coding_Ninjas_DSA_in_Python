# Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
# Return true or false.
# Do it recursively.

# Example: s="abchjsgsuohhdhyrikkknddg" contains all characters of t="coding" in the same order.
#         So function will return true.
        
        
def contains(s,t):
    # Base case: if the target string t is empty, it is always present in s
    if not t:
        return True
    
    # Base case: if s is empty but t is not, then t cannot be present in s
    if not s:
        return False
    
    # Check if the first characters of s and t match
    if s[0] == t[0]:
        # If they match, check the rest of the string
        return contains(s[1:], t[1:])
    else:
        # If they don't match, move to the next character in s
        return contains(s[1:], t)
    
s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')