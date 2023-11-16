# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a"*".

from math import *
from collections import *
from sys import *
from os import *

def pairstar(s):
    n=len(s)
    if n<=1 :
        return s
    temp = pairstar(s[1:])
    if s[0]==s[1]:
        return s[0]+"*"+temp
    else:
        return s[0]+temp
 

s= input().strip()
print(pairstar(s))