num = int(input())
result = []

for i in range(num):
    result.append(i+1)
    if result[i] % 3 == 0:
        result[i] = "X"
    print(result[i], end=" ")
