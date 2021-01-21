# alpha = ord(input())

# i = 97  # 97 == 'a'
# while True:
#     print(chr(i))
#     if chr(i) == chr(alpha):
#         break
#     i += 1


num = int(input())
result = 0
i = 0
while result < num:
    result += i
    if result == num:
        break
    i += 1
print(i)
