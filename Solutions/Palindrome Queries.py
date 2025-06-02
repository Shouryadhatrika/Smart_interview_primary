'''Palindrome Queries 
Given a string, check if substring from i to j is a palindrome.

Input Format
The first line of the input contains T - number of test cases. The first line of each test case contains N - the size of the string. The second line of the each test case contains a string of size N, containing only lowercase english alphabets. The third line of each test case contains Q - number of queries. Each of the next Q lines contains two integers i and j, for which you have to check whether substring S[i:j] is a palindrome.

Output Format
For each query, print "Yes" if substring S[i:j] is a palindrome otherwise print "No", separated by newline.

Constraints
30 points
1 <= N <= 103
1 <= Q <= 103

70 points
1 <= N <= 103
1 <= Q <= 105

100 points
1 <= N <= 105
1 <= Q <= 105

General Constraints
1 <= T <= 102
0 <= i <= j < N

Example
Input
1
10
smartmadam
5
1 7
6 8
5 8
5 9
2 2

Output
No
Yes
No
Yes
Yes

Explanation

Self Explanatory'''
mod=int(1e9+7)
maxn=10005
power=[1]*(maxn+1)
p=127
for i in range(1,maxn+1):
    power[i]=(power[i-1]*p)%mod
def is_palindrome(n,i,j,ph,sh):
    if i==0:
        h1=ph[j]
    else:
        h1=((ph[j]-ph[i-1])+mod)%mod
    if j==n-1:
        h2=sh[i]
    else:
        h2=((sh[i]-sh[j+1])+mod)%mod
    spph1=i+1
    spph2=n-j
    d=abs(spph1-spph2)
    if spph1<spph2:
        h1=(h1*power[d])%mod
    else:
        h2=(h2*power[d])%mod
    return h1==h2
for _ in range(int(input())):
    n=int(input())
    s=input()
    ph=[0]*n
    ph[0]=(ord(s[0])*power[1])%mod
    for i in range(1,n):
        ph[i]=(ph[i-1]+(ord(s[i])*power[i+1]))%mod
    sh=[0]*n
    sh[n-1]=(ord(s[n-1])*power[1])%mod
    for i in range(n-2,-1,-1):
        sh[i]=(sh[i+1]+(ord(s[i])*power[n-i]))%mod
    for _ in range(int(input())):
        i,j=map(int,input().split())
        if is_palindrome(n,i,j,ph,sh):
            print("Yes")
        else:
            print("No")
