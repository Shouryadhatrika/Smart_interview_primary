'''Rabin Karp String Matching Algorithm 
Given 2 strings A and B, find the number of occurrences of A in B as a substring.

Note: 
 Solve using the Rabin-Karp string matching algorithm. Do not use an inbuilt library.  Input Format
The first line of input contains T - the number of test cases. It's followed by T lines. Each line contains 2 strings - A and B, separated by space.

Output Format
For each test case, print the number of occurrences of A in B, separated by a new line.

Constraints
30 points
1 <= len(A), len(B) <= 1000

70 points
1 <= len(A), len(B) <= 10001

General Constraints
1 <= T <= 2000
'a' <= A[i], B[i] <= 'z'

Example
Input
4
smart yekicmsmartplrplsmartrplplmrpsmartrpsmartwmrmsmartsmart
interviews interviewseiwcombvinterviewskrenlzp
ds dsdsajdsrjjdsjjj
algo yalgoalgoalgopalgoaxalgoasaxalgolalgoalgoalgo

Output
6
2
4
9

Explanation

Self Explanatory'''

def f(a,b):
    c=0
    n=len(b)
    m=len(a)
    p=47
    k=int(1e9+7)
    power=[1]*n
    for i in range(1,n):
        power[i]=(power[i-1]*p)%k
    h1=0
    h2=0
    for i in range(n):
        h1=(h1+ord(b[i])*power[i])%k
        h2=(h2+ord(a[i])*power[i])%k
    if h1==h2:
        c+=1
    for i in range(n,m):
        h2=((h2-(ord(a[i-n])*power[0])%k)+k)%k
        h2=(h2*pow(p,k-2,k))%k
        h2=(h2+(ord(a[i])*power[n-1])%k)%k
        if h1==h2:
            c+=1
    return c
for _ in range(int(input())):
    a,b=input().split()
    print(f(b,a))
