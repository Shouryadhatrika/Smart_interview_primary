'''Minimum Cost Dice Rolls 
Given a standard 6-sided dice, find the minimum cost to get a sum of K by rolling a standard 6-sided dice any number of times. You are given the cost of each possible value of the dice, cost[i], where i ∈ [1, 6].

Input Format
The first line of input contains T - number of test cases. It is followed by 2T lines, first line contains K - the sum and second line contains cost of each possible value of the dice .

Output Format
For each test case, print the minimum cost to get sum of K, separated by newline.

Constraints
1 <= T <= 103
1 <= K <= 104
1 <= cost[i] <= 103

Example
Input
2
3
1 4 3 2 6 10
5
12 1 100 20 39 32

Output
3
14

Explanation
Self Explanatory 
'''



for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[float('inf')]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        for j in range(1,7):
            if i-j>=0:
                dp[i]=min(dp[i],dp[i-j]+arr[j-1])
    print(dp[n])

Self Explanatory
