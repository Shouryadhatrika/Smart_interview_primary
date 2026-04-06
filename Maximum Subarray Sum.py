'''Maximum Subarray Sum 
Maximum Subarray Sum bookmark_borderGiven an array of integers, find the maximum subarray sum.

Input Format
The first line of input contains T - number of test cases. It is followed by 2T lines. First line of each test case contains N - size of the array and the second line contains N integers - elements of the array.

Output Format
For each test case, print the maximum subarray sum, followed by the start and end indices of the subarray, separated by new line. If multiple subarrays give the same sum, consider the lexicographically smaller one for the answer.

Constraints
20 points
1 <= T <= 100
1 <= N <= 102

30 points
1 <= T <= 100
1 <= N <= 103

50 points
1 <= T <= 100
1 <= N <= 104

General Constraints
-103 <= A[i] <= 103

Example
Input
3
9
-24 0 28 28 55 -31 -27 -45 -24
10
40 5 39 45 31 -44 73 -16 -31 27
7
57 18 -14 17 31 16 -16

Output
111 1 4
189 0 6
125 0 5

Explanation
Self Explanatory '''

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    max_sum=arr[0]
    cur=arr[0]
    st=0
    end=0
    temp=0
    for i in range(1,n):
        if arr[i]>cur+arr[i]:
            cur=arr[i]
            temp=i
        else:
            cur+=arr[i]
        if cur>max_sum:
            max_sum=cur
            st=temp
            end=i
    print(max_sum,st,end)

Self Explanatory
