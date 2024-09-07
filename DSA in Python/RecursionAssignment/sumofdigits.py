# Write a recursive function that returns the sum of the digits of a given integer.

from math import *
from collections import *
from sys import *
from os import *

def Sumdigit(n):
    if n <10:
        return n
    return (n%10)+Sumdigit(n//10)

N=int(input())
print(Sumdigit(N))