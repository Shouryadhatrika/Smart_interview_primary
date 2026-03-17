'''Number of Dice Rolls for Given Sum 
Given a standard 6-sided dice, find the number of ways to get a sum of N.

Input Format
The first line of input contains T - number of test cases. It's followed by T lines, each line contains N - the desired sum.

Output Format
For each test case, print the number of ways to get a sum of N, separated by new line. Since the answer can be very large, print answer % 1000000007 [1e9+7].

Constraints
1 <= T <= 105
1 <= N <= 105

Example
Input
5
3
11
7
5
500

Output
4
976
63
16
765996555

Explanation

Example 1:
You can get a sum of 3 in the ways:
(1,1,1), (1,2), (2,1), (3) '''


mod=int(1e9+7)
lmt=int(10**5)+1
dp=[0]*(lmt)
dp[0]=1
for i in range(1,lmt):
    for j in range(1,7):
        if i-j>=0:
             dp[i]=(dp[i]+dp[i-j])%mod
for _ in range(int(input())):
    n=int(input())
    print(dp[n])
(1,1,1), (1,2), (2,1), (3)'''
