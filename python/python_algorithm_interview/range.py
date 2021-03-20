import sys
a = [i for i in range(100000000)] # for loop
b = range(100000000) # range class 호출

print(len(a))
print(len(b)) # a,b 는 기본적으로 동일한 값을 변수에 할당하고 있으나

print(type(a)) # type : list
print(type(b)) # type : class

print(sys.getsizeof(a)) # 매우 크다
print(sys.getsizeof(b)) # 메모리 차지 비율이 매우 적다.

# index, value를 한번에 loop로 가져오기 --> enumberate()
for i, v in enumerate(b):
    print(i,v)

# 몫과 나머지를 한 번에 구할 때 --> divmod(a,b)

print(divmod(5,3))