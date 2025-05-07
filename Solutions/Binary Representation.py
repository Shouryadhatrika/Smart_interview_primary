'''Binary Representation 
Given a positive integer, print its binary representation. 

Input Format
 The first line of input contains T - the number of test cases. It's followed by T lines, each line containing a single integer. 

Output Format
 For each test case, print a binary representation, separated by a new line. 

Constraints
 1 <= T <= 10000 
 0 <= N <= 109

Example
Input
 5
 10
 15
 7
 1
 120

Output
 1010
 1111
 111
 1
 1111000

Explanation

Self Explanatory'''

def fun(N):
    if N==0:
        return "0"
    res=""    
    while N>0  :
        res=str(N&1)+res
        N>>=1
    return (res)    
t=int(input())    
for i in range(t):
    N=int(input())
    print(fun(N))
