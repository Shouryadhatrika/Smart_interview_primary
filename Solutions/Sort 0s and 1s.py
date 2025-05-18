'''Sort 0s and 1s 
You are given an array of 0's and 1's. Sort the array in ascending order and print it.

Note: 
 Solve using two-pointer technique.  Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

Output Format
For each test case, sort the array in ascending order and print it in a new line.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= A[i] <= 1

Example
Input
2
5
0 1 1 0 1
6
1 1 1 1 1 0

Output
0 0 1 1 1
0 1 1 1 1 1

Explanation

Self Explanatory'''

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    i=0
    j=n-1
    while i<j :
        while i<n-1 and arr[i]!=1:
          i+=1
        while j>0 and arr[j]!=0:
            j-=1
        if i<j:
            temp=arr[i]        
            arr[i]=arr[j]
            arr[j]=temp
    print(*arr)





