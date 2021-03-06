N = int(input()) 
arr = [str(n) for n in range(1,N+1)]
 
for i in range(len(arr)):
    a = ''
    for j in arr[i]: 
        if j in ['3','6','9']:
            a += '-'
            arr[i] = a
 
print(*arr)