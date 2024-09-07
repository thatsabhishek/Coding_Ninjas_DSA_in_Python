# Problem statement
# You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively. 
# You need to print their intersection; 
# An intersection for this problem can be defined when both the arrays/lists contain a particular value or to put it in other words, when there is a common value that exists in both the arrays/lists.

# Note :
# Input arrays/lists can contain duplicate elements.

# The intersection elements printed would be in ascending order.


from sys import stdin

def intersection(arr1, arr2, n, m) :

    arr1.sort()
    arr2.sort()

    i = 0 #pointer to iterate over arr1
    j = 0 #pointer to iterate over arr2

    while i < n and j < m :
        
        if arr1[i] == arr2[j] :
            print(arr1[i], end = " ") 
            i += 1
            j += 1
        elif arr1[i] < arr2[j] :
            i += 1
        else :
            j += 1



# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1