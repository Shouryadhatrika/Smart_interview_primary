''' X 1s and Y 0s
Given two numbers X and Y, find the number whose binary representation has X 1's followed by Y 0's.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines. Each subsequent line contains two integers separated by a space: X - the number of the 1's and Y - the number of 0's which follows the X 1's in the binary representation of the number.

Output Format
For each test case, print the number whose binary representation has X 1's and Y 0's, separated by a new line. Since this number can be very large, print the result % 1000000007.

Constraints
30 points
1 <= T <= 100
0 <= X,Y <= 15

70 points
1 <= T <= 105
0 <= X,Y <= 105

Example
Input
3
4 3
2 5
10 15

Output
120
96
33521664

Explanation

Test-Case 1
The binary representation of the number that has 4 ones followed by 3 zeros is 1111000 = 120.'''
M=1000000007
def fun(X,Y):
    return((1<<(X+Y))-(1<<Y))%M
T=int(input())    
for i in range(T):
    X,Y=map(int,input().split())
    print(fun(X,Y))
