'''Diagonal Order Traversal 
Given an array of unique elements, construct a Binary Search Tree and print the tree in a Diagonal Order, starting from the root node. Print the nodes in each diagonal in descending order.

Input Format
The first line of input contains T - number of test cases. It is followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the Diagonal Levels of the Binary Search Tree, separate each level by newline.

Constraints
1 <= T <= 103
1 <= N <= 103
0 <= ar[i] <= 104

Example
Input
2
5
3 2 4 1 5
7
4 5 15 0 1 7 17

Output
3 2 1
4
5

4 0
5 1
15 7
17

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
def f(root,hm,v):
    if root==None:
        return 
    if v in hm:
        hm[v].append(root.data)
    else:
        hm[v]=[root.data]
    f(root.right,hm,v+1)
    f(root.left,hm,v)
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    hm={}
    f(root,hm,0)
    for i in sorted (hm.keys()):
        print(*hm[i])
    print()

Self Expl
