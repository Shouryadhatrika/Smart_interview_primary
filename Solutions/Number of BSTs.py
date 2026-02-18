'''Number of BSTs 
Given a binary tree with unique elements, find the number of Binary Search Trees that are part of the given binary tree and have unique root nodes.
The input is given in the form of a complete binary tree, represented using an array. Assuming the array index starts from 1, the root will be at index 1. For every index i, its child nodes will be at 2i and 2i+1.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the tree. The next line contains N integers - nodes of the binary tree in the form of a Complete Binary Tree.

Output Format
For each test case, print the number of Binary Search Trees, separated by a newline.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 100000

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
10
9
2
3
15

Explanation
Self Explanatory '''


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
    global c 
    if root==None:
        return
    if checkbst(root):
        c+=1
    f(root.left)
    f(root.right)
def checkbst(root):
    prev=[None]
    def inorder(root):
        if not root:
            return True
        if inorder(root.left)==False:
            return False
        if prev[0]!=None and root.data<=prev[0]:
            return False
        prev[0]=root.data
        return inorder(root.right)
    return inorder(root)
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    root=insert(arr,0)
    f(root)
    print(c)

Self Explanatory
