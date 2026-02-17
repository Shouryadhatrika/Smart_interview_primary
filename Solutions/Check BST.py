'''Check BST 
Given a binary tree with unique elements, check if it's a Binary Search Tree.
The input is given in the form of a complete binary tree, represented using an array. Assuming the array index starts from 1, the root will be at index 1. For every index i, its child nodes will be at 2i and 2i+1.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the tree. The next line contains N integers - nodes of the binary tree in the form of a Complete Binary Tree.

Output Format
For each test case, print "True" if the given Binary Tree is a Binary Search Tree, "False" otherwise, separated by a newline.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Example
Input
5
11
92 10 963 5 334 928 973 2 9 263 860
9
156 153 6947 149 154 1761 7230 9 152
4
40 49 87 651
5
449 792 594 688 618
15
736 43 882 3 460 741 887 0 42 247 465 739 844 886 888

Output
False
True
False
False
True

Explanation
Self Explanatory
'''
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
def checkbst(root,x,y):
    if root==None:
        return True
    return root.data>x and root.data<y and checkbst(root.left,x,root.data) and checkbst(root.right,root.data,y)
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=insert(arr,0)
    print(checkbst(root,float("-inf"),float("inf")))

Self Explanatory
