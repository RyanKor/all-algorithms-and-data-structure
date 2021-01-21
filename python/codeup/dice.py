a, b = input().split()

# for i in range(int(a)):

#     for j in range(int(b)):
#         print(i+1, j+1)

i = 1
j = 1

while i <= int(a):
    print(i, j)
    j += 1
    if j == int(b):
        print(i, j)
        i += 1
        j = 1
