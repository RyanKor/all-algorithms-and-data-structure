'''
D. Multiples and Power Differences
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a matrix a consisting of positive integers. It has n rows and m columns.

Construct a matrix b consisting of positive integers. It should have the same size as a, and the following conditions should be met:

1≤bi,j≤106;
bi,j is a multiple of ai,j;
the absolute value of the difference between numbers in any adjacent pair of cells (two cells that share the same side) in b is equal to k4 for some integer k≥1 (k is not necessarily the same for all pairs, it is own for each pair).
We can show that the answer always exists.

Input
The first line contains two integers n and m (2≤n,m≤500).

Each of the following n lines contains m integers. The j-th integer in the i-th line is ai,j (1≤ai,j≤16).

Output
The output should contain n lines each containing m integers. The j-th integer in the i-th line should be bi,j.
'''
