'''Finding the Floor 
Given an array, you have to find the floor of a number x. The floor of a number x is nothing but the largest number in the array less than or equal to x.

Input Format
The first line of input contains the N - the size of the array. The next line contains N integers, the elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains a single integer X, for which you have to find the floor of X in the given array.

Output Format
For each query, print the floor of X, separated by a new line. If the floor is not found, print the value of "INT_MIN".

Constraints
30 points
1 <= N <= 105
1 <= Q <= 102
-108 <= ar[i] <= 108

70 points
1 <= N <= 105
1 <= Q <= 105
-108 <= ar[i] <= 108

Example
Input
6
-6 10 -1 20 15 5
5
-1
10
8
-10
-4

Output
-1
10
5
-2147483648
-6

Explanation

Self Explanatory'''
def f(ar,n,x):
    l=0
    h=n-1
    ans=-2147483648
    while(l<=h):
        m=(l+h)//2
        if arr[m]<=x:
            ans=arr[m]
            l=m+1
        else:
            h=m-1
    return ans             
n=int(input())       
arr=list(map(int,input().split()))
arr.sort()
q=int(input())
for i in range(q):
    x=int(input())
    print(f(arr,n,x))

