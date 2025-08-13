'''Depth of Tree Nodes 
Given an array of unique elements, construct a Binary Search Tree and for every node, print the depth of that node.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the depth of every node of the Binary Search Tree, separated by a newline.

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
0 1 2 3 4
0 1 1 2 2
0 1 2 1 2 3 3

Explanation'''

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
def filldept(root,d,hm):
    if root==None:
        return
    hm[root.data]=d
    filldept(root.left,d+1,hm)
    filldept(root.right,d+1,hm)
        
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    hm={}
    filldept(root,0,hm)
    for i in arr:
        print(hm[i],end=" ")
    print()

Self Explanator
