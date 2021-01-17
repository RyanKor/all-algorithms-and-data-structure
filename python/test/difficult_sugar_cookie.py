h, w = map(int, input().split())

result = [[0]*w for i in range(h)]
# print(result)
n = int(input())

for i in range(n):
    length, direction, x, y = map(int, input().split())

    if direction == 0:
        for j in range(length):
            result[x-1][y-1+j] = 1
    else:
        for j in range(length):
            result[x-1+j][y-1] = 1


for i in result:
    for j in range(len(i)):
        print(i[j], end=" ")
    print()
