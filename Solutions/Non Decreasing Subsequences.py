'''Non Decreasing Subsequences 
You are given an array of integers of size N. Find the total number of non-decreasing subsequences present in the array.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

Output Format
Print the total number of non-decreasing subsequences present in the array for each test case on a new line.
Since this number can be very large, print the result % 1000000007.

Constraints
30 points
1 <= T <= 100
1 <= N <= 20
-105 <= A[i] <= 105

70 points
1 <= T <= 100
1 <= N <= 103
-105 <= A[i] <= 105

Example
Input
2
4
1 8 2 5
10
9 7 8 6 5 7 4 3 2 1

Output
9
14

Explanation

Test Case-1:
The are 9 non-decreasing subsequences:
{1}, {8}, {2}, {5}, {1,8}, {1,2}, {1,5} and {2,5} and {1,2,5}.

Test Case-2:
The are 14 non-decreasing subsequences:
{9}, {7}, {8}, {6}, {5}, {7}, {4}, {3}, {2}, {1}, {7,8}, {7,7}, {6,7} and {5,7}.
'''
def solv(arr,n,idx,prev):
    if idx==n:
        return 1
    c=solv(arr,n,idx+1,prev)
    if(arr[idx]>=prev):
        c+=solv(arr,n,idx+1,arr[idx])
    return c
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print((solv(arr,n,0,float('-inf'))-1)%100000007)
