# Given two integers M & N, calculate and return their multiplication using recursion.
# You can only use subtraction and addition for your calculation. No other operators are allowed.

from math import *
from collections import *
from sys import *
from os import *

from sys import setrecursionlimit
setrecursionlimit(10**6) 

def mul(m, n):
    if m == 0 or n == 0:
        return 0
    if n == 1:
        return m 
    if m == 1:
        return n
    return m + mul(m, n - 1)

m = int(input())
n = int(input())
print(mul(m,n))