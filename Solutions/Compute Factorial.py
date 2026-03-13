'''Compute Factorial
Given a number N, print N!.

Input Format
The first line of input contains T - number of test cases. It's followed by T lines, each containing a single number N.

Output Format
For each test case, print N!. Since the result can be very large, print N! % 1000000007 [1e9+7].

Constraints
1 <= T <= 106
0 <= N <= 106

Example
Input
3
5
20
50

Output
120
146326063
318608048

Explanation

Self Explanatory'''

mod=int(1e9+7)
max_n=int(1e6)
fact=[1]*(max_n+1)
for i in range(2,max_n+1):
    fact[i]=(fact[i-1]*i)%mod
for i in range(int(input())):
        n=int(input())
        print(fact[n])
