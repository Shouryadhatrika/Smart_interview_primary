'''Power of 2 
Given a number, check if it is a power of 2.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each line containing a single positive integer.

Output Format
For each test case, print "True" or "False", separated by a new line.

Constraints
1 <= T <= 10000
1 <= N <= 1018

Example
Input
5
1
8
10
25
512

Output
True
True
False
False
True

Explanation

Self Explanatory'''

t=int(input())
for i in range(t):
    n=int(input())
    if((n&(n-1))==0):
     print("True")
    else:
        print("False")
