'''Balanced Tree

Given an array of unique elements, construct a Binary Search Tree and check if it is balanced. A tree is said to be balanced if, for every node, the difference between the height of its child nodes is not greater than 1.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print "Yes" if the Binary Search Tree is balanced, "No" otherwise, separated by a newline.

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
def btree(root):
    if root==None:
         return 0, True
    lh,f1=btree(root.left)
    rh,f2=btree(root.right)
    b=abs(lh-rh)<=1 and f1 and f2
    return max(lh,rh)+1,b
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    ans=btree(root)[1]
    if ans:
        print("Yes")
    else:
        print("No")
