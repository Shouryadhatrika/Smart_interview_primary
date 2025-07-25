'''Sum with Queries 
You are given an array of integers of size N. You are also given Q queries consisting of three integers i, j, and x.
For each query, increment each element of the array from index i to j by a value of x. At the end, print the sum of all the elements of the array.

Input Format
The first line of input contains T - the number of test cases. For each test case, the first line contains N - the size of the array. The second line contains N integers - the elements of the array.
The third line contains Q - the number of queries. The Q subsequent lines each contain 3 integers i, j - the indices denoting the subarray and x - the value to be added to the elements of the subarray.

Output Format
For each test case, after processing all the queries, print the sum of all the elements of the entire array, separated by newline.

Constraints
1 <= T <= 100
1 <= N <= 105
1 <= Q <= 10000
-105 <= A[i], x <= 105
0 <= i <= j < N

Example
Input
2
5
1 5 -3 2 8
2
1 3 1
0 1 2
6
4 10 -1 2 8 -3
1
3 5 6

Output
20
38

Explanation

Test-Case 1
Query 1: Adding 1 to each element of the array from indices 1 to 3 will make the array [1, 6, -2, 3, 8].
Query 2: Adding 2 to each element of the array from indices 0 to 1 will make the array [3, 8, -2, 3, 8].
The sum of all the elements is 20.'''


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ts=sum(a)
    q=int(input())
    for _ in range(q):
        i,j,x=map(int,input().split())
        ts+=(j-i+1)*x
    print(ts)
