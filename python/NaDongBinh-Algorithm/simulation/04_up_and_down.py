import sys

n = int(sys.stdin.readline())
direction = sys.stdin.readline().split()
# start = [1,1]
# lst = []

# 이하 내 풀이
# for i in direction:
#     if i == "R":
#         if start[-1] + 1 > n:
#             pass
#         else:
#             start[-1] +=1
#     elif i == "L":
#         if start[-1] - 1 <= 0:
#             pass
#         else:
#             start[-1] -=1
#     elif i == "U":
#         if start[0] - 1 <= 0:
#             pass
#         else:
#             start[0] -=1
#     else:
#         if start[0] + 1 > n:
#             pass
#         else:
#             start[0] +=1

# print(*start)

# 책 내용 풀이
x,y = 1,1
dx = [0,0,-1,1] # 좌우 이동
dy = [-1,1,0,0]
move_types = ["L","R","U","D"]

for plan in direction:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            next_x = x + dx[i]
            next_y = y + dy[i]
    if next_x<1 or next_y < 1 or next_x > n or next_y > n:
        continue

    x,y = next_x, next_y
print(x,y)