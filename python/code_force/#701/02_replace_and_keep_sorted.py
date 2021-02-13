'''
B. Replace and Keep Sorted
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Given a positive integer k, two arrays are called k-similar if:

they are strictly increasing;
they have the same length;
all their elements are positive integers between 1 and k (inclusive);
they differ in exactly one position.
You are given an integer k, a strictly increasing array a and q queries. For each query, you are given two integers li≤ri. Your task is to find how many arrays b exist, such that b is k-similar to array [ali,ali+1…,ari].

Input
The first line contains three integers n, q and k (1≤n,q≤105, n≤k≤109) — the length of array a, the number of queries and number k.

The second line contains n integers a1,a2,…,an (1≤ai≤k). This array is strictly increasing  — a1<a2<…<an.

Each of the following q lines contains two integers li, ri (1≤li≤ri≤n).

Output
Print q lines. The i-th of them should contain the answer to the i-th query.
'''
