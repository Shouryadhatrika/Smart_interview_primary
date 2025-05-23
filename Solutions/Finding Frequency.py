'''Finding Frequency
Given an array, you have to find the frequency of a number X.

Input Format
The first line of input contains N - size of the array. The next line contains N integers, the elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains a single integer X, for which you have to find the frequency of X in the given array.

Output Format
For each query, print the frequency of X, separated by a new line.

Constraints
20 points
1 <= N <= 105
1 <= Q <= 102
-108 <= ar[i] <= 108

30 points
1 <= N <= 105
1 <= Q <= 105
-108 <= ar[i] <= 108

50 points
1 <= N <= 105
1 <= Q <= 105
-108 <= ar[i] <= 108

Example
Input
9
-6 10 -1 20 -1 15 5 -1 15
5
-1
10
8
15
20

Output
3
1
0
2
1

Explanation

Self Explanatory'''
def bs(arr,n,x):
    l=0
    h=n-1
    while l<=h:
        m=(l+h)//2
        if arr[m]==x:
            return m
        elif arr[m]>x:
            h=m-1
        else:
            l=m+1
    return -1
n=int(input())
arr=list(map(int,input().split()))
sarr=sorted(arr)
a=[]
b=[]
c=1
for i in range(1,n):
    if sarr[i-1]==sarr[i]:
        c+=1
    else:
        a.append(sarr[i-1])
        b.append(c)
        c=1
a.append(sarr[-1])
b.append(c)
for _ in range(int(input())):
    q=int(input())
    x=bs(a,len(a),q)
    if x!=-1:
        print(b[x])
    else:
        print(0)
