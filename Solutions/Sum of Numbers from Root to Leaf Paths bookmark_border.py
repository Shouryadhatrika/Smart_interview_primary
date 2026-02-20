'''Sum of Numbers from Root to Leaf Paths bookmark_border
Given an array of unique elements, construct a Binary Search Tree and print the sum of all the numbers formed along the path from the root node to the leaf nodes.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the sum separated by a newline. Since the output can be very large, print output % 1000000007.

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
4 5 15 2 1 7 17

Output
12345
666
497095

Explanation

Example 1: 
Total Sum = 12345

Example 2: 
Total Sum = 321 + 345 = 666

Example 3: 
Total Sum = 421 + 45157 + 451517 = 497095 '''



mod=int(1e9+7)
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert (root,k):
    if root==None:
        return Node(k)
    if k<root.data:
        root.left=insert(root.left,k)
    else:
        root.right=insert(root.right,k)
    return root
def f(root,v):
    if root==None:
        return 0 
    v=(v*10**(len(str(root.data))))%mod+root.data
    if root.left==None and root.right==None:
        return v
    return (f(root.left,v)+f(root.right,v))%mod
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    root=None
    for i in arr:
        root=insert(root,i)
    print(f(root,0))
