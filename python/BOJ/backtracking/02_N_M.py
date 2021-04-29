import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
temp = list(permutations(range(1,N+1),M))
answer = []
for i in temp:
    arr = sorted(i)
    answer.append(tuple(arr))
answer = list(set(answer))
answer.sort()
for i in answer:
    print(*i)