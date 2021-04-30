import sys
from itertools import permutations, product
# N, M = map(int, sys.stdin.readline().split())
# for i in product(range(1,N+1),repeat=M):
#     print(*i)


N, M = map(int, input().split())
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(i+1)
        solve(depth+1, N, M)
        out.pop()

solve(0, N, M)