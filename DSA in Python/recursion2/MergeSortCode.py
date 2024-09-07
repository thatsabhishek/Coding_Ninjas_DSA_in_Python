# You are given the starting 'l' and the ending 'r' positions of the array 'ARR'.
# You must sort the elements between 'l' and 'r'.

# Note:
#     Change in the input array itself. So no need to return or print anything.

def mergeSort(arr: [int], l: int, r: int):
    if l<r:
        mid = (l+(r-1))//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)

        merge(arr, l, mid, r)

def merge(arr:[int], l:int, mid:int, r:int):
    a1 = mid-l+1
    a2 = r-mid

    L = [0]*a1
    R = [0]*a2

    for i in range(a1):
        L[i] = arr[l+i]
    for j in range(a2):
        R[j] = arr[mid+1+j]

    i = j =0
    k = l

    while i<a1 and j<a2:
        if L[i] <+ R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i<a1:
        arr[k] = L[i]
        i+=1
        k+=1
    while j<a2:
        arr[k] = R[j]
        j+=1
        k+=1

