'''
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=
'''
import sys

test_case = sys.stdin.readline().rstrip()
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for word in croatia_alphabet:
    test_case = test_case.replace(word, '#')


print(len(test_case))
