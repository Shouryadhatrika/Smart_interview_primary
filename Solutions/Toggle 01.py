'''Toggle 01
Consider an array of 0's of size N. You are given Q queries of the following types:
1 idx: Toggle the element present at the given index. If the element is 0, make it 1 and vice versa.
2 idx: Print the distance of the nearest 1 from the given index.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains N - the size of the array and Q - the number of queries, separated by a space.
The Q subsequent lines contain two integers K - the type of the query and i - an index in the array.

Output Format
For each test case, process the queries and for each query of type 2, print the result separated by a newline.
For queries of type 2, if such an element is not found, print -1.

Constraints
30 points
1 <= N <= 103
1 <= Q <= 1000

70 points
1 <= N <= 109
1 <= Q <= 5x104

General Constraints
1 <= T <= 100
K ∈ [1,2]

Example
Input
2
5 4
1 1
2 0
1 3
2 4
6 4
2 0
1 0
1 5
2 2

Output
1
1
-1
2

Explanation

Example 1:

Initially, the array is: 0 0 0 0 0

First query: 1 1
Toggle the element at index 1. The resulting array is: 0 1 0 0 0

Second query: 2 0
Print the distance to the nearest 1 from index 0. Since the nearest 1 is present at index 1, the distance is 1.

Third query: 1 3
Toggle the element at index 3. The resulting array is: 0 1 0 1 0

Fourth query: 2 4
Print the distance to the nearest 1 from index 4. Since the nearest 1 is present at index 3, the distance is 1.'''

for _ in range(int(input())):
    n,q=map(int,input().split())
    hs=set()
    for _ in range(q):
        t,idx=map(int,input().split())
        if t==1:
            if idx in hs:
                hs.remove(idx)
            else:
             hs.add(idx)
        else:
            m=float('inf')
            for i in hs:
                m=min(abs(i-idx),m)
            if m!=float('inf'):
                print(m)
            else:
                 print(-1)
