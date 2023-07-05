# Given a string S (that can contain multiple words), you need to find the word which has minimum length.
# Note : If multiple words are of same length, then answer will be first minimum length word in the string.
# Words are seperated by single space only.

# Sample Input 1 :
# this is test string
# Sample Output 1 :
# is

## Read input as specified in the question.
## Print output as specified in the question.

s = input().split()
l = []
for i in s:
    l.append(len(i))
print(s[l.index(min(l))])