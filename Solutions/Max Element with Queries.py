'''Max Element with Queries
Max Element with Queries bookmark_borderYou are given an array of integers of size N. You are also given Q queries consisting of three integers i, j, and x. For each query, increment each element of the array from index i to j by a value of x. At the end, print the largest element of the array.

Input Format
The first line of input contains T - the number of test cases. For each test case, the first line contains N - the size of the array. The second line contains N integers - the elements of the array. The third line contains Q - the number of queries. The Q subsequent lines each contain 3 integers i, j - the indices denoting the subarray and x - the value to be added to the elements of the subarray.

Output Format
For each test case, after processing all the queries, print the max element of the entire array, separated by a new line.

Constraints
30 points
1 <= N <= 102
1 <= Q <= 102

70 points
1 <= T <= 100
1 <= N <= 105
1 <= Q <= 104

General Constraints
1 <= T <= 100
-105 <= A[i], x <= 105
0 <= i <= j < N

Example
Input
2
5
1 2 3 4 5
2
0 3 7
1 2 2
6
4 10 -1 2 8 -3
1
3 5 6

Output
12
14

Explanation

Test-Case 1
Query 1: Adding 7 to each element of the array from indices 0 to 3 will make the array [8, 9, 10, 11, 5].
Query 2: Adding 2 to each element of the array from indices 1 to 2 will make the array [8, 11, 12, 11, 5].
The max element of the array is 12.'''

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    diff=[0]*(n+1)
    q=int(input())
    for _ in range(q):
        i,j,x=map(int,input().split())
        diff[i]+=x
        if j+1<n:
            diff[j+1]-=x
    curr=0
    max_ele=float('-inf')
    for i in range(n):
        curr+=diff[i]
        a[i]+=curr
        if a[i]>max_ele:
            max_ele=a[i]
    print(max_ele)
