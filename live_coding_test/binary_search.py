def binary_search(arr,target,left,right):
    mid = (left+right)//2
    if arr[mid] == target:
        return arr[mid]
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,right)
    elif arr[mid] > target:
         return binary_search(arr,target,left,mid-1)

T = int(input)

arr = list(map(int, input().split()))

lst = sorted(arr)


print(binary_search(lst, 5, 0, len(lst)-1))