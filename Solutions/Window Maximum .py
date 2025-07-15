'''Window Maximum 
Given an array of integers of size N and a window size K. For each continuous window of size K, find the highest element in the window. Output the sum of the highest element of all the windows.

Input Format
The first line of input contains T - number of test cases. It is followed by 2T lines, the first line contains N and K - the size of the array and the window size K. The second line contains N integers - the elements of the array.

Output Format
For each test case, print the sum of the highest element of all the windows of size K, separated by a newline.

Constraints
30 points
1 <= T <= 1000
1 <= N <= 1000
1 <= K <= N
-104 <= A[i] <= 104

70 points
1 <= T <= 1000
1 <= N <= 10000
1 <= K <= N
-104 <= A[i] <= 104

Example
Input
2
7 3
4 10 54 11 8 7 9
4 2
11 15 12 9

Output
182
42

Explanation

Example 1:
Window [4 10 54] : maximum element = 54
Window [10 54 11] : maximum element = 54
Window [54 11 8] : maximum element = 54
Window [11 8 7] : maximum element = 11
Window [8 7 9] : maximum element = 9
Total Sum = 54 + 54 + 54 + 11 + 9 = 182

Example 2:
Window [11 15] : maximum element = 15
Window [15 12] : maximum element = 15
Window [12 9] : maximum element = 12
Total Sum = 15 + 15 + 12 = 42'''

import heapq
from collections import Counter
from collections import deque
def findWindowMaxSum(arr,k):
    s=0
    dq=deque()
    for i in range(k):
        while(len(dq)!=0 and arr[i]>dq[-1]):
            dq.pop()
        dq.append(arr[i])
    s=max(arr[:k])
    for i in range(k,len(arr)):
        while(len(dq)!=0 and arr[i]>dq[-1]):
            dq.pop()
        dq.append(arr[i])
        if dq[0]==arr[i-k]:
            dq.popleft()
        s+=dq[0]
    return s 
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    print(findWindowMaxSum(arr,k))
