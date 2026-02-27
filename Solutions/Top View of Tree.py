'''Top View of Tree 
Given an array of unique elements, construct a Binary Search Tree and print the top-view of the tree. The top view of a tree is the set of nodes visible when the tree is viewed from the top.

Input Format
Given an array of unique elements, construct a Binary Search Tree and print the top-view of the tree. The top view of a Tree is the set of nodes visible when the tree is viewed from the top.

The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - the value of the nodes.

Output Format
For each test case, print the top view of the Binary Search Tree, separated by a new line. Print the set of visible nodes from left to right.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Example
Input 
3
6
10 20 13 3 17 18 
6
10 3 20 15 14 12 
7
10 3 8 20 7 6 4 

Output
3 10 20 18 
12 3 10 20 
4 6 3 10 20 

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
def f(root,hm):
    q=[(root,0)]
    while q:
        n,v=q[0]
        if v not in hm:
            hm[v]=n.data
        if n.left!=None:
            q.append((n.left,v-1))
        if n.right!=None:
            q.append((n.right,v+1))
        q.pop(0)
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    hm={}
    f(root,hm)
    for i in sorted(hm.keys()):
        print(hm[i],end=" ")
    print()







Self Expl
