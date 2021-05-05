from itertools import combinations
def solution(nums):
    answer = 0
    temp = list(combinations(nums,3))
    result = []
    for i in temp:
        result.append(sum(i))
    for i in result:
        if (i % 2 == 0 and i !=2) or i <2:
            pass
        else:
            cnt = 0
            for j in range(2, i+1):
                if i % j == 0:
                    cnt +=1
            if cnt == 1:
                answer +=1
    return answer