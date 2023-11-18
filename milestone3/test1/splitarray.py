# Given an integer array A of size N, check if the input array can be divided in two groups G1 and G2 with following properties-

# - Sum of both group elements are equal

# - Group 1: All elements in the input, which are divisible by 5

# - Group 2: All elements in the input, which are divisible by 3 (but not divisible by 5).

# - Elements which are neither divisible by 5 nor by 3, can be put in either group G1 or G2 to satisfy the equal sum property.

# Group 1 and Group 2 are allowed to be unordered and all the elements in the Array A must belong to only one of the groups.

# Return true, if array can be split according to the above rules, else return false.

def split(arr ,i ,s1 ,s2=0):
    # Implement Your Function here
    if i== len(arr):
        if s1 == s2:
            return True
        else:
            return False

    if arr[i] % 5 == 0:
        s1 += arr[i]
        return split(arr, i + 1, s1, s2)
    elif arr[i] % 3 == 0:
        s2 += arr[i]
        return split(arr, i + 1, s1, s2)
    else:
        a = split(arr, i + 1, s1 + arr[i], s2)
        b = split(arr, i + 1, s1, s2 + arr[i])
        return a or b


n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr, 0, 0)
if ans is True:
    print('true')
else:
    print('false')