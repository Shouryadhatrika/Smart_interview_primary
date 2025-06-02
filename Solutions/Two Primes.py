'''Two Primes 
Given an integer N, find the count of all the positive numbers <= N, which cannot be represented as sum of two primes.

Input Format
The first line of input contains T - number of test cases. It is followed by T lines, each line contains the number N.

Output Format
For each test case, print the count of all the positive numbers <= N, which cannot be represented as sum of two primes, separated by newline.

Constraints
30 points
1 <= T <= 100
2 <= N <= 103

70 points
1 <= T <= 103
2 <= N <= 105

Example
Input
3
5
20
40

Output
3
5
10

Explanation

Test Case 1:
1, 2, 3 are all the positive numbers less than or equal to 5 which cannot be represented as sum of two primes.

Test Case 2:
1, 2, 3, 11, 17 are all the positive numbers less than or equal to 20 which cannot be represented as sum of two primes.

Test Case 3:
1, 2, 3, 11, 17, 23, 27, 29, 35, 37 are all the positive numbers less than or equal to 40 which cannot be represented as sum of two primes.'''


n=10**5+1
primes=[0,0]+[1]*(n-2)
for i in range(1,int(n**0.5)+1):
    if primes[i]:
        for j in range(i*i,n,i):
            primes[j]=0
p=[i for i in range(2,n) if primes[i]]
arr=[0]*n
for i in range(len(p)):
    for j in range(i,len(p)):
        s=p[i]+p[j]
        if s<n:
            arr[s]=1
        else:
            break
arr1=[0]*n
for i in range(1,n):
    arr1[i]=arr1[i-1]+(1 if arr[i]==0 else 0) 
for _ in range(int(input())):
    m=int(input())
    print(arr1[m])
