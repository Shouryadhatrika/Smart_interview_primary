'''
Vertical Order Traversal
Given an array of unique elements, construct a Binary Search Tree and print the tree in a Vertical Order, starting from the left-most node. Print the nodes in each vertical in sorted order.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the Vertical Levels of the Binary Search Tree, separate each level by newline. Separate the output of different test cases with an extra newline.

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
3 1 2 5 4
7
4 5 15 0 1 7 17

Output
1
2
3
4
5

1
2 3 4
5

0
1 4
5 7
15
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
    f(root.left,hm,v-1)
    f(root.right,hm,v+1)
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    hm={}
    f(root,hm,0)
    for i in sorted(hm.keys()):
        print(*sorted(hm[i]))
    print()
