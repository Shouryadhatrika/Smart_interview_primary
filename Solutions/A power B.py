'''
A power B 
Given 2 numbers - A and B, evaluate AB.

Note: 
 Do not use any inbuilt functions / libraries for your main logic.  Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each line containing 2 numbers - A and B, separated by space.

Output Format
For each test case, print AB, separated by new line. Since the result can be very large, print result % 1000000007

Constraints
30 points
1 <= T <= 1000
0 <= A <= 106
0 <= B <= 103

70 points
1 <= T <= 1000
0 <= A <= 106
0 <= B <= 109

Example
Input
4
5 2
1 10
2 30
10 10

Output
25
1
73741817
999999937

Explanation

Self Explanatory'''

c=1000000007
def fun(a,b):
    if(b==0):
        return 1
    ans=fun(a,b//2)
    if(b%2==0)   :
        return((ans%c)*(ans%c))%c
    else:
        return (a*((ans%c)*(ans%c))%c)%c
T=int(input())            
for _ in range (T):
    l=list(map(int,input().split()))
    print(fun(l[0],l[1])%c)
