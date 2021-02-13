'''
F. Copy or Prefix Sum
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given an array of integers b1,b2,…,bn.

An array a1,a2,…,an of integers is hybrid if for each i (1≤i≤n) at least one of these conditions is true:

bi=ai, or
bi=∑ij=1aj.
Find the number of hybrid arrays a1,a2,…,an. As the result can be very large, you should print the answer modulo 109+7.

Input
The first line contains a single integer t (1≤t≤104) — the number of test cases.

The first line of each test case contains a single integer n (1≤n≤2⋅105).

The second line of each test case contains n integers b1,b2,…,bn (−109≤bi≤109).

It is guaranteed that the sum of n for all test cases does not exceed 2⋅105.

Output
For each test case, print a single integer: the number of hybrid arrays a1,a2,…,an modulo 109+7.
'''
