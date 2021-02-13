'''
A. Add and Divide
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You have two positive integers a and b.

You can perform two kinds of operations:

a=⌊a//b⌋ (replace a with the integer part of the division between a and b)
b=b+1 (increase b by 1)
Find the minimum number of operations required to make a=0.

Input
The first line contains a single integer t (1≤t≤100) — the number of test cases.

The only line of the description of each test case contains two integers a, b (1≤a,b≤109).

Output
For each test case, print a single integer: the minimum number of operations required to make a=0.
'''

import sys

test_case = int(sys.stdin.readline())

for i in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    cnt = 0
    while True:
        # a를 0으로 만들기 위해 할 수 있는 최소한의 연산
        # a를 b로 나누고 난 몫 그리고 b+1, 2개의 연산만 가능하다
        if b == 1 or a == b:
            b += 1
            cnt += 1
        else:
            cnt += 1
            a = int(a//b)
        if a == 0:
            print(cnt)
            break
