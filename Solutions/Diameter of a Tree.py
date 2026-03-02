'''Diameter of a Tree 
Given an array of unique elements, construct a Binary Search Tree and find the diameter of the tree. Diameter is defined as the number of nodes on the longest path between 2 nodes of the tree.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - the value of the nodes.

Output Format
For each test case, print the diameter of the Binary Search Tree, separated by a newline.

Constraints
1 <= T <= 1000
1 <= N <= 5000
0 <= ar[i] <= 10000

Example
Input
3
5
1 2 3 4 5 
5
2 4 3 1 5 
7
4 5 15 0 1 7 17

Output
5
4
6

Explanation
Self Explanatory'''

from collections import deque
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
def solve(root):
    if root is None:
        return 0,0
    ld,lh=solve(root.left)
    rd,rh=solve(root.right)
    cur_h=1+max(lh,rh)
    cur_d=max(ld,rd,lh+rh+1)
    return cur_d,cur_h

for _ in range(int(input())):
    n=map(int,input().split())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    ans,_=solve(root)
    print(ans)
Self Explanatory
