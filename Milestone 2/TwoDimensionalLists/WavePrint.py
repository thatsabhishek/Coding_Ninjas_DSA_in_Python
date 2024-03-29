# For a given two-dimensional integer array/list of size (N x M), print the array/list in a sine wave order, i.e, print the first column top to bottom, next column bottom to top and so on.

# Sample Input 1:
# 1
# 3 4 
# 1  2  3  4 
# 5  6  7  8 
# 9 10 11 12
# Sample Output 1:
# 1 5 9 10 6 2 3 7 11 12 8 4

from sys import stdin


def wavePrint(mat, nRows, mCols):
    #Your code goes here
    i = 0
    while i < mCols:
        j = 0
        while j != nRows:
            print(mat[j][i], end=" ")
            j += 1
        i += 1
        j -= 1
        if i != mCols:
            while j != -1:
                print(mat[j][i], end=" ")
                j -= 1
            i += 1


#Taking Iput Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0:

    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1