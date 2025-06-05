'''Large Range Primes 
Given 2 numbers M and N (M<=N), print all prime numbers between M and N (inclusive).

Input Format
The first line of input contains T - the number of test cases. Its followed by T lines, each line containing 2 space-separated integers - M and N.

Output Format
For each test case, print all prime numbers p such that M <= p <= N, separated by a new line. Print an extra newline between outputs of different test cases.

Constraints
30 points
1 <= T <= 100
0 <= M <= N <= 106
0 <= N-M <= 105

70 points
1 <= T <= 100
0 <= M <= N <= 1012
0 <= N-M <= 105

Example
Input
2
1 10
3 5

Output
2
3
5
7

3
5

Explanation

Self Explanatory'''

n=10**6+1
primes=[0,0]+[1]*(n-2)
for i in range(1,int(n**0.5)+1):
    if primes[i]:
        for j in range(i*i,n,i):
            primes[j]=0
primes=[i for i in range(1,n) if primes[i]]
def f(a,b):
    x=int(b**0.5)
    arr=[1]*(b-a+1)
    i=0
    while primes[i]<=x:
        p=primes[i]
        s=max(p*p,(a+p-1)//p*p)
        for j in range(s,b+1,p):
            arr[j-a]=0
        i+=1
    if a==1:
        arr[0]=0
    for i in range(b-a+1):
        if arr[i]:
            print(i+a)
for i in range(int(input())):
    a,b=map(int,input().split())
    f(a,b)
    print()
