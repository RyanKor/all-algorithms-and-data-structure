import sys

# 해결법 1 -> 시간 초과 (아래의 답은 O(N^2)이 출력된다.)
# for i in range(len(target)):
#     if target[i] in A:
#         print(1)
#     else:
#         print(0)


def BinarySearch(arr, val, low, high):
    if low > high:
        return False

    mid = (low + high) // 2
    if arr[mid] > val:
        return BinarySearch(arr, val, low, mid - 1)
    elif arr[mid] < val:
        return BinarySearch(arr, val, mid + 1, high)
    else:
        return True


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
A = sorted(A)

for m in M_list:
    if BinarySearch(A, m, 0, N-1):
        print(1)
    else:
        print(0)
