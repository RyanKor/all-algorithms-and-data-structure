# series = input().split()
# result = int(series[0])

# for i in range(int(series[-1])-1):
#     result += int(series[1])
# print(result)

series = input().split()
result = int(series[0])

for i in range(int(series[-1])-1):
    result = (result * int(series[1])) + int(series[2])
print(result)
