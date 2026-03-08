'''Information Passed In N-ary Tree 
Given an N-ary tree, find the minimum time required to pass "KEY" to all the nodes. Initially, at time t=0, only the root node has the "KEY". At any given time t, a node which has the "KEY", can pass the "KEY" to any one of its child nodes.

Input Format
The first line of input contains T - number of test cases. The first line of each test case contains N - number of nodes and M - number of edges. It is followed by M lines, each contains a pair (u,v) - where v is a child of u.

Note: 1 is always the root node.

Output Format
For each test case, print the minimum time required to pass the data to all the nodes, separated by newline.

Constraints
1 <= T <= 103
1 <= N <= 104﻿

Example
Input
2
8 7
1 4
1 3
4 6
1 7
3 5
6 8
8 2
6 5
1 6
6 3
6 2
2 4
1 5

Output
4
3

Explanation

Test Case-1:


At t = 1, key is passed from node 1 to node 4.
At t = 2, key is passed from node 1 to node 3 and node 4 to node 6.
At t = 3, key is passed from node 1 to node 7, node 3 to node 5 and node 6 to node 8.
At t = 4, key is passed from node 8 to node 2.

Test Case-2:

At t = 1, key is passed from node 1 to node 6.
At t = 2, key is passed from node 1 to node 5 and node 6 to node 2.
At t = 3, key is passed from node 2 to node 4 and node 6 to node 3.
'''



def solve(arr,index):
    if len(arr[index])==0:
        return 0
    list=[]
    for i in arr[index]:
        list.append(solve(arr,i))
    list.sort(reverse=True)
    mx=float("-inf")
    for i in range(len(list)):
        mx=max(mx,list[i]+(i+1))
    return mx 
for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[[] for i in range(n+1)]
    for i in range(m):
        u,v=map(int,input().split())
        arr[u].append(v)
    print(solve(arr,1))
