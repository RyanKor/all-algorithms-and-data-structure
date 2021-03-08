'''
※ SW expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

어떤 자연수 A가 주어진다. 여기에 자연수 B를 곱한 결과가 거듭제곱수가 되는 최소의 B를 구하는 프로그램을 작성하라. 여기서 자연수는 1이상인 정수를 뜻한다.

 

[입력]

첫 번째 줄에 테스트 케이스의 수 T 가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 자연수 A(1≤A≤107) 가 주어진다.

 
[출력]
각 테스트 케이스마다 A에 곱한 결과가 거듭제곱수가 되는 최소의 자연수를 출력한다.


'''
# import math
# T = int(input())

# # 시간 초과
# for test_case in range(1, T+1):
#     case = int(input())
#     B = 1
#     while math.sqrt(case * B) != int(math.sqrt(case * B)):
#         B +=1
#     print('#{}'.format(test_case), B)
prime = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime:
        if not i % p: break
    else:
        prime.append(i)
answer = []
T = int(input())
for tc in range(T):
    A = int(input())
    res = 1
    if A**0.5 != int(A**0.5):
        for p in prime:
            cnt = 0
            while not A % p:
                A //= p
                cnt += 1
            if cnt % 2:
                res *= p
            if A == 1 or p > A:
                break
        if A > 1:
            res *= A
    answer.append('#{} {}'.format(tc+1, res))
for ans in answer:
    print(ans)