'''Smaller Elements
You are given an array of integers. For each element in the array, find the number of smaller elements on the right side and print the total count.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

Output Format
For each test case, print the sum of count of smaller elements on right side of each element in the array, separated by new line.

Constraints
30 points
1 <= N <= 103

70 points
1 <= N <= 105

General Constraints
1 <= T <= 100
-104 <= A[i] <= 104﻿

Example
Input
2
5
4 10 54 11 8
6
15 35 25 10 15 12

Output
4
10

Explanation

Test Case 1
Smaller Elements on right side of 4 : 0
Smaller Elements on right side of 10 : 1
Smaller Elements on right side of 54 : 2
Smaller Elements on right side of 11 : 1
Smaller Elements on right side of 8 : 0
Total Count = 0 + 1 + 2 + 1 + 0 = 4

Test Case 2
Smaller Elements on right side of 15 : 2
Smaller Elements on right side of 35 : 4
Smaller Elements on right side of 25 : 3
Smaller Elements on right side of 10 : 0
Smaller Elements on right side of 15 : 1
Smaller Elements on right side of 12 : 0
Total Count = 2 + 4 + 3 + 0 + 1 + 0 = 10'''
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr1=[0]*20001
    t=0
    for i in range(n-1,-1,-1):
        val=arr[i]+10000
        s=0
        for j in range(val):
            s+=arr1[j]
        t+=s
        arr1[val]+=1
    print(t)
