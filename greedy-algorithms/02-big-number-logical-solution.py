n, m, k = map(int, input().split())  # 예제로부터 주어진 첫번째 라인 입력값 받기

data = list(map(int, input().split()))  # 2번째 입력 값을 배열로 받아오기

data.sort()  # 작은 수 ~ 큰 수로 정렬하기 / 여기서 중복되는 값은 제거하지 않았다.

first = data[n-1]  # 첫번째로 큰 수
second = data[n-2]  # 두번째로 큰 수


# int(m/(k+1)) * k + m % (k + 1)
# 수열의 패턴을 인지해서 반복적으로 더하는 과정을 이해해야한다.

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)
