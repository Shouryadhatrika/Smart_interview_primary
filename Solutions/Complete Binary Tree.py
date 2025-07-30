'''Complete Binary Tree 
Given an array of unique elements, construct a Binary Search Tree and check if it is a Complete Binary Tree [CBT]. In a Complete Binary Tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print "Yes" if it is a Complete Binary Search Tree, "No" otherwise, separated by a newline.

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
4 2 5 3 1
7
4 5 15 0 1 7 17

Output
No
Yes
No

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
def is_completebt(root,idx,n):
    if root==None:
        return True
    if idx>n:
        return False
    return is_completebt(root.left,2*idx,n) and is_completebt(root.right,2*idx+1,n)
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    if(is_completebt(root,1,n)):
        print("Yes")
    else:
        print("No")
