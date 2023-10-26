# Given a string, compute recursively a new string where all 'x' chars have been removed.

def removeX(s): 
    if len(s) == 0:
        return s
    smallOutput = removeX(s[1:])
    if s[0] == 'x':
        return smallOutput
    else:
        return s[0] + smallOutput

s = input()
print(removeX(s))
