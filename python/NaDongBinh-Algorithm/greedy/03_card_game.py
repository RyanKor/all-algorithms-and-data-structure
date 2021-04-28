import sys

n,m = map(int, sys.stdin.readline().split())
lst = []
answer = []
for i in range(n):
    card = list(map(int, sys.stdin.readline().split()))
    lst.append(card)

for i in lst:
    answer.append(min(i))

print(max(answer))