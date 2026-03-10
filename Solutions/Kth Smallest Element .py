'''Kth Smallest Element 
You are given an integer K and an array of distinct integers of size N. Find the Kth smallest element from the array.

Note: 
 Try solving with the help of MaxHeap or QuickSelect, don't solve using sorting.  Input Format
The first line of input contains T - the number of test cases. For each test case, the first line contains N - the size of the array and an integer K. The second line contains N integers - the elements of the array.


Output Format
For each test case, print the Kth smallest element from the array, separated by a newline.

Constraints
1 <= T <= 100
1 <= K <= N <= 105
0 <= A[i] <= 105

Example
Input
2
5 3
1 5 13 2 8
6 2
10 1 20 8 31 12

Output
5
8

Explanation
self '''

import heapq
for _ in range(int(input())):
    heap=[]
    n,k=map(int,input().split())
    arr=map(int,input().split())
    for n in arr:
        heapq.heappush(heap,-n)
        if len(heap)>k:
            heapq.heappop(heap)
    print(-heap[0])

Self Explanatory
