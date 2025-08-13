'''Level Order of Tree 
Given an array of unique elements, construct a Binary Search Tree and print the Level Order of the tree.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the Level Order of the Binary Search Tree, separate each level by a newline. Separate the output of different test cases with an extra newline.

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
1
2
3
4
5

3
2 4
1 5

4
0 5
1 15
7 17

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
def levorder(root):
    q=[root]
    while len(q)!=0:
        s=len(q)
        for i in range(s):
            print(q[0].data,end=" ")
            if q[0].left!=None:
                q.append(q[0].left)
            if q[0].right!=None:
                q.append(q[0].right)
            q.pop(0)
        print()
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    levorder(root)
