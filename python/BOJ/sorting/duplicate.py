import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
answer = list(set(lst))
answer.sort()
print(*answer)