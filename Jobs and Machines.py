'''You have to complete N jobs using 2 machines. You can only work on 1 job at a time and the jobs should be completed in the order given in the input. The time to complete a particular job on Machine-A is given by A[i] and Machine-B is given by B[i]. Additionally, note that if between the jobs, if you switch from Machine-A to Machine-B or vice-versa, there's an additional time K added to total time, for evey switch that is made. Find the minimum time required to complete all the jobs.

Input Format
The first line of input contains T - number of test cases. First line of each testcase contains 2 integers N and K, it is followed by 2 lines, each containing N integers where ith number in each line denotes the time taken by the Machine-A (say array A) and Machine-B (say array B) to complete the ith job respectively.

Output Format
For each test case, print the minimum time to complete all the jobs, separated by a newline.

Constraints
1 <= T <= 103
1 <= N, K <= 103
1 <= A[i], B[i] <= 105

Example
Input
2
5 8
11 34 50 29 17
36 48 27 13 18
5 2
18 23 44 37 36
46 29 42 45 8

Output
111
132

Explanation

Example 1:
Jobs will be executed in the following order: Machine-A, Machine-A, Machine-B, Machine-B, Machine-B.
Total Cost = 11 + 34 + 8 + 27 + 13 + 18 = 111.

Example 2:
Jobs will be executed in the following order: Machine-A, Machine-A, Machine-A, Machine-A, Machine-B.'''


def solve(a,b,n,t):
    dpa=[0]*(n+1)
    dpb=[0]*(n+1)
    for i in range(1,n+1):
        dpa[i]=min(dpa[i-1],dpb[i-1]+t)+a[i-1]
        dpb[i]=min(dpb[i-1],dpa[i-1]+t)+b[i-1]
    return min(dpb[n],dpa[n])
t=int(input())
for _ in range(t):
    n,t=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(solve(a,b,n,t))
Total Cost = 18 + 23 + 44 + 37 + 2 + 8 = 132.'''
