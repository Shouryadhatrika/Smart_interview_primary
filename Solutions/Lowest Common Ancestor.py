'''Lowest Common Ancestor 
Given an array of unique elements, construct a Binary Search Tree. Now, given two nodes u and v of the BST, find their Lowest Common Ancestor (LCA). LCA is defined as the furthest node from the root that is an ancestor for both u and v.

Input Format
The first line of input contains T - the number of test cases. The first line of each test case contains N, Q - the number of nodes in the BST and the number of queries. The next line contains N unique integers - value of the nodes. It is followed by Q lines, each containing 2 nodes of the tree, u and v.

Output Format
For each test case, for each query print the LCA of the given nodes u and v, separated by space. Separate the output of different test cases with a newline.

Constraints
1 <= T <= 1000
1 <= N,Q <= 1000
0 <= ar[i] <= 10000

Example
Input
2
5 2
3 2 4 1 5
2 5
1 2
7 3
4 5 15 0 1 7 17
0 15
7 17
17 4

Output
3 2
4 15 4

Explanation

Self Explanatory'''




class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,k):
    if root==None:
        return Node(k)
    if k<root.data:
        root.left=insert(root.left,k)
    else:
        root.right=insert(root.right,k)
    return root
def f(root,a,b):
    if root==None:
        return
    if root.data<a and root.data<b:
        return f(root.right,a,b)
    if root.data>a and root.data>b:
        return f(root.left,a,b)
    return root
for _ in range(int(input())):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    for i in range(q):
        x,y=map(int,input().split())
        a=min(x,y)
        b=max(x,y)
        x=f(root,a,b)
        print(x.data,end=" ")
    print()
