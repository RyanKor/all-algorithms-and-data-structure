'''
E. Move and Swap
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given n−1 integers a2,…,an and a tree with n vertices rooted at vertex 1. The leaves are all at the same distance d from the root.

Recall that a tree is a connected undirected graph without cycles. The distance between two vertices is the number of edges on the simple path between them. All non-root vertices with degree 1 are leaves. If vertices s and f are connected by an edge and the distance of f from the root is greater than the distance of s from the root, then f is called a child of s.

Initially, there are a red coin and a blue coin on the vertex 1. Let r be the vertex where the red coin is and let b be the vertex where the blue coin is. You should make d moves. A move consists of three steps:

Move the red coin to any child of r.
Move the blue coin to any vertex b′ such that dist(1,b′)=dist(1,b)+1. Here dist(x,y) indicates the length of the simple path between x and y. Note that b and b′ are not necessarily connected by an edge.
You can optionally swap the two coins (or skip this step).
Note that r and b can be equal at any time, and there is no number written on the root.

After each move, you gain |ar−ab| points. What's the maximum number of points you can gain after d moves?

Input
The first line contains a single integer t (1≤t≤104) — the number of test cases.

The first line of each test case contains a single integer n (2≤n≤2⋅105) — the number of vertices in the tree.

The second line of each test case contains n−1 integers v2,v3,…,vn (1≤vi≤n, vi≠i)  — the i-th of them indicates that there is an edge between vertices i and vi. It is guaranteed, that these edges form a tree.

The third line of each test case contains n−1 integers a2,…,an (1≤ai≤109) — the numbers written on the vertices.

It is guaranteed that the sum of n for all test cases does not exceed 2⋅105.

Output
For each test case, print a single integer: the maximum number of points you can gain after d moves.
'''
