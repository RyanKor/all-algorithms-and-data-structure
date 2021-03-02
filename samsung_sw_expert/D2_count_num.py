from collections import Counter
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    case = list(map(int, input().split()))
    counter = Counter(case)
    print(test_case, max(counter.keys(), key=lambda k: counter[k]))
