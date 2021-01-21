a, b, c = input().split()

day = 1

while(day % int(a) != 0 or day % int(b) != 0 or day % int(c) != 0):
    day += 1
print(day)
