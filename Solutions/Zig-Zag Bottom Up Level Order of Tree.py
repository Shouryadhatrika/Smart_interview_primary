'''Zig-Zag Bottom Up Level Order of Tree 
Given an array of unique elements, construct a Binary Search Tree and print the Level Order of the tree in a zig-zag fashion, not top-down, but bottom-up. Assume the root is at level-1, zig-zag means that nodes at even levels will be printed left to right and the nodes at odd levels will be printed from right to left.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the bottom-up Level Order Traversal of the Binary Search Tree in a zig-zag fashion, separated by a newline.

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
5 4 3 2 1
5 1 2 4 3
7 17 15 1 0 5 4

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
def levorder(root):
    q=[root]
    ans=[]
    while len(q)!=0:
        s=len(q)
        arr=[]
        for i in range(s):
            arr.append(q[0].data)
            if q[0].left!=None:
                q.append(q[0].left)
            if q[0].right!=None:
                q.append(q[0].right)
            q.pop(0)
        ans.append(arr)
    return ans
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    ans=levorder(root)
    a=[]
    for i in range(len(ans)):
        if i%2!=0:
            a.append(ans[i][::-1])
        else:
            a.append(ans[i])
    for i in a[::-1]:
        print(*i[::-1],end=" ")
    print()

Self Explanatory
