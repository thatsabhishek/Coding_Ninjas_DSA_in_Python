# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up to the stairs.
# You need to return number of possible ways W.

from math import *
from collections import *
from sys import *
from os import *

def Staircase(n):
    if(n<=3):
        if(n==1):
            return 1
        elif(n==2):
            return 2
        else:
            return 4
    x=Staircase(n-1)
    y=Staircase(n-2)
    z=Staircase(n-3)
    return x+y+z
n=int(input())
a=Staircase(n)
print(a)