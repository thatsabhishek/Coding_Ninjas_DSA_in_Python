# Given an integer N, count and return the number of zeros that are present in the given integer using recursion.

from math import *
from collections import *
from sys import *
from os import *

count=0
def count_digit(num):
    global count
    if num ==0:
        return 1
    if (num >0):
        if(num%10==0):
            count +=1
        count_digit(num // 10)
    return count
n=int(input())
print(count_digit(n))