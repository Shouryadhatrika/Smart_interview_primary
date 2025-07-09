'''Rectangular Area Under Histogram 
Given the height of adjacent buildings, find the largest rectangular area possible, where the largest rectangle can be made of a number of contiguous buildings. For simplicity, assume that all buildings have the same width and the width is 1 unit.
Note that the sides of the rectangle have to be parallel to the axes.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines - the first line contains N - the number of buildings. The second line contains the height of the buildings.

Output Format
For each test case, print the area of the largest possible rectangle, separated by a newline.

Constraints
50 points
1 <= T <= 100
1 <= N <= 103
1 <= A[i] <= 1000

100 points
1 <= T <= 100
1 <= N <= 105
1 <= A[i] <= 104

Example
Input
2
16
5 4 5 4 3 2 5 5 6 7 1 3 4 3 3 3
4
5 11 12 4

Output
20
22

Explanation

Example 1:

The maximum rectangular area is obtained by selecting the highlighted buildings (5, 5, 6, 7), corresponding to the indices 6 to 9. The area is calculated as 5 * 4 = 20. [a * b means rectangle with height a and width b]

Example 2:
The maximum rectangular area is obtained by selecting the buildings of indices 1 and 2. The area is calculated as 11 * 2 = 22. [a * b means rectangle with height a and width b]
'''


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    res=0
    stack=[]
    arr.append(0)
    for i,num in enumerate(arr):
        while stack and arr [stack[-1]]>num:
            h=arr[stack.pop()]
            w=i if not stack else i-stack[-1]-1
            res=max(res,h*w)
        stack.append(i)
    print(res)
