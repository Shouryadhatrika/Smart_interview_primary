'''Count the Triangles
You have a collection of N rods. Each rod has a unique mark on it. You are given the lengths of each rod. You have to tell how many different triangles can be formed using these rods.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the number of rods. The second line contains the lengths of the rods.

Output Format
For each test case, print the total number of different triangles possible, separated by new line.

Constraints
30 points
1 <= T <= 100
1 <= N <= 100
1 <= A[i] <= 100000

70 points
1 <= T <= 100
1 <= N <= 1000
1 <= A[i] <= 100000

Example
Input
2
6
20 67 72 83 23 59
6
4 2 10 12 8 10

Output
14
10

Explanation

Self Explanatory '''
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    count=0
    for i in range(n-1,0,-1):
        l=0
        r=i-1
        while(l<r):
            if(arr[l]+arr[r]>arr[i]):
                count+=r-l
                r-=1
            else:
                l+=1
    print(count)
