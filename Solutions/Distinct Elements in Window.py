'''Distinct Elements in Window 
Given an array of integers and a window size K, find the number of distinct elements in every window of size K of the given array.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains the N-size of the array and the K-size of the window. The second line contains N integers - elements of the array.

Output Format
For each test case, print the number of distinct elements in every window of size K, separated by a new line.

Constraints
30 points
1 <= N <= 100
1 <= K <= N

70 points
1 <= N <= 10000
1 <= K <= N

General Constraints
1 <= T <= 1000
-100 <= ar[i] <= 100

Example
Input
3
5 3
-2 -4 -2 4 -2
10 7
3 -4 -3 -4 -2 0 2 -2 6 0
17 13
-5 -1 4 8 -5 -3 -4 7 4 -4 0 8 0 -2 3 2 5

Output
2 3 2
6 5 6 5
8 9 9 10 11

Explanation

Self Explanatory'''

for _ in range(int(input())):
    hm={}
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(k):
        if arr[i] in hm:
            hm[arr[i]]+=1
        else:
            hm[arr[i]]=1
    print(len(hm),end=" ")
    for i in range(k,n):
        if arr[i] in hm:
            hm[arr[i]]+=1
        else:
            hm[arr[i]]=1
        if hm[arr[i-k]]==1:
            del hm[arr[i-k]]
        else:
            hm[arr[i-k]]-=1
        print(len(hm),end=" ")
    print()
