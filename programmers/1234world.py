from itertools import product
def solution(n):
    # n은 500,000,000이하의 자연수 입니다. --> 동적 프로그래밍으로도 해결이 안된다.
    '''
    한 자리 수 -> 1,2,4 (3 == 3 ** 1)
    두 자리 수 -> 11,12,14, 21,22,24, 41,42,44 (9 == 3 ** 2)
    세 자리 수 -> 111,112,114,121,122,124,141,142,144,
                211,212,214,221,222,224,241,242,244,
                411,412,414,421,422,424,441,442,444
                (27 == 3 ** 3)
    십진법 수의 범위 : 1 ~ 3, 4 ~ 12, 13 ~ 40, 41 ~ 122
    124나라 수의 범위 : 3^0 ~ 3^1 / 3^1 + 3^0 ~ 3^2 + 3^1 / 3^2 + 3^1 + 3^0 ~ 3^3 + 3^2 + 3^1 + 3^0
    '''
    world124 = ['1','2','4']
    minimum, maximum = 0,0
    cnt = 0
    while True:
        minimum += 3^cnt
        cnt +=1
        if minimum < n:
            maximum += 3^(cnt+1) + minimum
            break
    temp = list(product(world124,repeat=cnt))
    answer = ''
    return maximum

print(solution(11))