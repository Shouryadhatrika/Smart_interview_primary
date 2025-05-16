'''Express as Power Sum
Given an integer N, find the number of ways it can be expressed as the sum of the Kth powers of unique natural numbers.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each line containing 2 space-separated integers - N and K.

Output Format
Print the number of ways for each test case, separated by a new line.

Constraints
1 <= T <= 100
1 <= N <= 1000
2 <= K <= 10

Examples
Input
3
10 2
100 2
100 3

Output
1
3
1

Explanation

Test-Case 1
There is only 1 way to express 10 as the sum of squares of unique natural numbers: 12 + 32 = 10

Test-Case 2
There are 3 ways to express 100 as the sum of squares of unique natural numbers: 102 = 62 + 82 = 12 + 32 + 42 + 52 + 72 = 1
Test-Case 3
There is only 1 way to express 100 as the sum of 3rd power of unique natural numbers: 13 + 23 + 33 + 43 = 100'''
def solv(s,req,idx,po,c):
    if s==req:
        c[0]+=1
        return
    if s>req or idx**po>req:
        return
    solv(s+idx**po,req,idx+1,po,c)
    solv(s,req,idx+1,po,c)
for i in range(int(input())):
    n,m=map(int,input().split())
    c=[0]
    solv(0,n,1,m,c)
    print(c[0])
