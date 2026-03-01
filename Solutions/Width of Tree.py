'''Width of Tree 
Given an array of unique elements, construct a Binary Search Tree and find the width of the tree. The width of the tree is defined as the maximum distance between the vertical levels of any pair of nodes, where both the nodes belong to the same horizontal level.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - the value of the nodes.

Output Format
For each test case, print the width of the tree, separated by a newline.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Example
Input
3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 

Output
0
4
2

Explanation
Self Explanatory 
'''
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
Self Expl
