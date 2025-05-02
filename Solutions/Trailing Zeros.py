'''Trailing Zeros bookmark_borderCount the number of trailing 0s in the factorial of a given number.

Input Format
The first line of input contains T - the number of test cases. It is followed by T lines, each containing an integer N.

Output Format
For each test case, print the number of trailing 0s in N!, separated by a new line.

Constraints
1 <= T <= 10000
1 <= N <= 1015

Example
Input
3
2
5
100

Output
0
1
24

Explanation

2! = 2 [No trailing zeros]
5! = 120 [Trailing zeros=1
'''
def fun(n):
    count=0
    while n>=5:
        count+=n//5
        n=n//5
    return(count)    
T=int(input())    
for i in range(T):
    n=int(input())
    print(fun(n))
