from itertools import permutations, combinations
T = int(input())

for test_case in range(1, T+1):
    case = list(map(int, input().split()))
    result = []
    for i in list(combinations(case,6)):
        result.append(list(i))
    for j in result:
        left = j[:3]
        right = j[3:]
        cnt = 0
        if left[1] -1 == left[0] and left[1] + 1 == left[-1]:
            cnt +=1
        elif left[0] == left[1] == left[-1]:
            cnt +=1
        else:
            pass
        if right[1] -1 == right[0] and right[1] + 1 == right[-1]:
            cnt +=1
        elif right[0] == right[1] == right[-1]:
            cnt +=1
        else:
            pass
        if cnt == 2:
            print(j, "Triplet!")
        elif cnt == 1:
            print(j, "Run!")
        else:
            print(j,"Nothing!")