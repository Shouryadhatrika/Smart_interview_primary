'''Cabinets Partitioning
You are given a job that has been divided into N tasks. The task cannot be divided any further. Each of the N tasks takes Si number of seconds to complete. Your job will be completed when all your tasks are completed. You have K workers at your disposal to help you complete the tasks. But as per the nature of the job, a worker can only be allocated continuous tasks. A worker can work only on a single task at any given point in time. However, the workers can work in parallel on different tasks. You have to find the minimum possible time in which you can complete the job.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N and K - the number of tasks and available workers for the current job, separated by space. The next line contains N positive integers - denoting the time taken to complete the ith task.

Output Format
For each test case, print the minimum possible time in which you can complete the job, separated by a new line.

Constraints
50 points 
1 <= N,K <= 20

100 points 
1 <= N,K <= 10000

General Constraints
1 <= T <= 50
1 <= Si <= 103

Example
Input
6
10 3
1 10 13 4 5 12 23 12 18 8
8 4
17 27 22 45 26 32 45 16
2 2
74 61
7 3
74 24 61 81 66 76 51
2 1
54 10
4 2
15 30 10 50

Output
38
66
74
159
64
55

Explanation

Test Case 1: The arrangement for which we can achieve minimum possible time is as follows:
[1 10 13 4 5] - Worker 1
[12 23] - Worker 2
[12 18 8] - Worker 3

Test Case 2: The arrangement for which we can achieve minimum possible time is as follows:
[17 27 22] - Worker 1
[45] - Worker 2
[26 32] - Worker 3
[45 16] - Worker 4'''
def check(arr,mid,n,k):
    s=0
    count=0
    for i in arr:
        if i > mid:
            return False
        s+=i
        if s>mid:
            s=i
            count+=1
    count+=1
    if count<=k:
        return True
    return False
def partitioncabinet(arr,n,k):
    total=sum(arr)
    low=1
    high=total
    ans=0
    while (low<=high):
        mid=(low+high)//2
        if(check(arr,mid,n,k)):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    print(partitioncabinet(arr,n,k))
