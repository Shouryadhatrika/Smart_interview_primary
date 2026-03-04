'''Maximum Path Sum 
Given a binary tree with unique elements, find the maximum path sum of any non-empty path.
The input is given in form of a complete binary tree, represented using an array. Assuming array index start from 1, root will be at index 1. For every index i, its child nodes will be at 2i and 2i+1.

Input Format
First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the tree. The next line contains N integers - nodes of the binary tree in the form of a Complete Binary Tree.

Output Format
For each test case, print the maximum path sum, separated by newline.

Constraints
30 points
1 <= T <= 100
1 <= N <= 100

70 points
1 <= T <= 103
1 <= N <= 104

General Constraints
-105 <= ar[i] <= 105

Example
Input
3
15
5 1 7 2 3 -1 13 4 8 9 20 14 -3 6 10
3
10 -1 8
7
5 1 3 2 4 0 6

Output
59
18
19

Explanation
Self Explanatory'''


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(arr,idx):
    if idx>=len(arr):
        return None
    node=Node(arr[idx])
    node.left=insert(arr,2*idx+1)
    node.right=insert(arr,2*idx+2)
    return node
def f(root):
    global ans
    if root==None:
        return 0
    l=f(root.left)
    r=f(root.right)
    cans=max(0,l)+max(0,r)+root.data
    ans=max(cans,ans)
    return root.data+max(0,max(l,r))
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=insert(arr,0)
    ans=float("-inf")
    f(root)
    print(ans)

Self Explanatory
