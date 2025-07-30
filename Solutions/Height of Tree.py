'''Height of Tree 
Given an array of unique elements, construct a Binary Search Tree and find the height of the tree.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the height of the Binary Search Tree, separated by a newline.

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
4
2
3

Explanation

Self Explanatory'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
        if root is None:
            return Node(data)
        if data<=root.data:
            root.left=insert(root.left,data)
        else:
            root.right=insert(root.right,data)
        return root
def height(root):
        if root is None:
            return -1
        return 1+ max(height(root.left),height(root.right))
T=int(input())
for _ in range(T):
        N=int(input())
        data=list(map(int,input().split()))
        root=None
        for i in data:
            root= insert(root,i)
        print(height(root))
