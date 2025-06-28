'''Equal 0s and 1s 
You are given an array of 0's and 1's. Find the length of the longest subarray which has an equal number of 0's and 1's.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

Output Format
For each test case, print the length of the longest subarray which has equal 0's and 1's, separated by a newline.

Constraints
10 points
1 <= T <= 100
1 <= N <= 100

20 points
1 <= T <= 100
1 <= N <= 1000

70 points
1 <= T <= 1000
1 <= N <= 104

Example
Input
2
5
0 1 1 0 1
6
1 1 1 1 1 0

Output
4
2

Explanation

Example 1: The longest subarray which has an equal number of 0's and 1's is [0 1 1 0]

Example 2: The longest subarray which has an equal number of 0's and 1's is [1 0]
'''
t=int(input())
for _ in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    prefix_sum_idx={0:-1}
    max_len=0
    prefix_sum=0
    for i in range(n):
        if arr[i]==0:
            prefix_sum-=1
        else:
            prefix_sum+=1
        if prefix_sum not in prefix_sum_idx:
            prefix_sum_idx[prefix_sum]=i
        else:
            max_len=max(max_len,i-prefix_sum_idx[prefix_sum])
    print(max_len)
