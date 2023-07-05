# For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.
# Note :
# If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.

# Sample Input 1:
# 1
# 3 2
# 6 9 
# 8 5 
# 9 2 
# Sample Output 1:
# column 0 23

from sys import stdin

def findLargest(arr, nRows, mCols):
    #for column max index and number
    
    row_max = -2147483648
    row_max_index = 0
    for i in range(nRows):
        sum = 0
        for j in range(mCols):
            sum += mat[i][j]
        if sum > row_max:
            row_max = sum
            row_max_index = i
    
    col_max = -2147483648
    col_max_index = 0
    for j in range(mCols):
        sum = 0
        for i in range(nRows):
            sum += mat[i][j]
        if sum > col_max:
            col_max = sum
            col_max_index = j
            
    if col_max > row_max:
        print("column", col_max_index, col_max)
    else:
        print("row", row_max_index, row_max)


























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
    findLargest(mat, nRows, mCols)

    t -= 1