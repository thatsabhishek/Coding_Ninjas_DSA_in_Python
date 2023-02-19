n = int(input())
i = 1
k = 1
while i<= n:
    j= n
    while j>= 1:
        if j==k:
            print('*',end='')
        else:
            print(j,end='')
        j=j-1
    print()
    i=i+1
    k=k+1
        
