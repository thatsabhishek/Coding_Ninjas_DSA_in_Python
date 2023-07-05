# For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:
# a. First row(left to right)
# b. Last column(top to bottom)
# c. Last row(right to left)
# d. First column(bottom to top)
#  Mind that every element will be printed only once.
 
# Sample Input 1:
# 1
# 4 4 
# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12 
# 13 14 15 16
# Sample Output 1:
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here

    if nRows == 0:
        return
    r, c = 0, 0
    ne = nRows*mCols
    count = 0
    while count < ne:
        i = c
        while i < mCols and count < ne:
            print(mat[r][i], end=" ")
            count = count+1
            i = i+1
        r = r+1
        i = r
        while i < nRows and count < ne:
            print(mat[i][mCols-1], end=" ")
            count = count+1
            i = i+1
        mCols = mCols-1
        i = mCols-1
        while i >= c and count < ne:
            print(mat[nRows-1][i], end=" ")
            count = count+1
            i = i-1
        nRows = nRows-1
        i = nRows-1
        while i >= r and count < ne:
            print(mat[i][c], end=" ")
            count = count+1
            i = i-1
        c = c+1



#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1