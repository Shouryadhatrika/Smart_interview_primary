'''Trim BST 
You are given two integers L, R, and an array of unique elements, construct a Binary Search Tree from the array, and then trim the BST in a manner such that all its elements lie between [L, R].
Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant).

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains three integers, N - the number of nodes in the BST, L - the lower limit of the range, and R - the upper limit of the range. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the preorder traversal of the trimmed tree, separated by a newline.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Example
Input
3
5 2 4
1 2 3 4 5
5 1 4
3 2 4 1 5
7 2 10
4 5 15 0 1 7 17

Output
2 3 4
3 2 1 4
4 5 7

Explanation
Self Explanatory '''

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
def trim(root,l,r):
    if root==None:
        return
    if root.data<l:
        return trim(root.right,l,r)
    if root.data>r:
        return trim(root.left,l,r)
    root.left=trim(root.left,l,r)
    root.right=trim(root.right,l,r)
    return root
def preorder(root):
    if root==None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

for _ in range(int(input())):
    n,l,r=map(int,input().split())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    root=trim(root,l,r)
    preorder(root)
    print()

Self Explanatory.
