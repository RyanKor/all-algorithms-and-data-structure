import sys

A, B = sys.stdin.readline().split()


if int(A[::-1]) > int(B[::-1]):
    print(A[::-1])
else:
    print(B[::-1])
