'''Pair with Difference K
You are given an integer array and an integer K. You have to tell if there exists a pair of integers in the given array such that ar[i]-ar[j]=K and i≠j.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N and K - the size of the array and the number K. The second line contains the elements of the array.

Output Format
For each test case, print "true" if the arrays contains such elements, "false" otherwise, separated by new line.

Constraints
40 points
2 <= N <= 1000

60 points
2 <= N <= 100000

General Constraints
1 <= T <= 100
-105 <= ar[i], K <= 105

Example
Input
2
5 60
1 20 40 100 80
10 11
12 45 52 65 21 645 234 14 575 112

Output
true
false

Explanation

Self Explanatory'''

def f(n,k,arr):
    seen=set()
    for i in arr:
        if i-k in seen or i+k in seen:
            return "true"
        seen.add(i)
    return "false"
for _ in range (int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(f(n,k,arr))
