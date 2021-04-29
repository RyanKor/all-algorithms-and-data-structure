import sys
# 완전 탐색을 사용하는 경우
# 탐색해야하는 알고리즘의 전체 데이터 갯수가 100만개 이하일 때 적절하다.
n = int(sys.stdin.readline())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
        