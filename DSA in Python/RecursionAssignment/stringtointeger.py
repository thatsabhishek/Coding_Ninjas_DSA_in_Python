# Write a recursive function to convert a given string into the number it represents.
# That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.

def String_to_Integer(n,si):
    if(si==0):
        return int(n[si])
    smalloutput=int(n[si])+10*String_to_Integer(n,si-1)
    return smalloutput
a=input()
n=String_to_Integer(a,len(a)-1)
print(n)