'''
Preorder Inorder to Postorder 
Given the preorder and inorder traversals of a binary tree with unique elements, print the PostOrder Traversals of the tree.

Input Format
The first line of input contains T - the number of test cases. It's followed by 3T lines. The first line of each test case contains N - the number of nodes in the BST. The second line contains N unique integers denoting the preorder traversal of the tree. The third line contains N unique integers denoting the inorder traversal of the tree.

Output Format
For each test case, print the PostOrder Traversal of the Binary Tree, separated by a newline.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Example
Input
3
7
1 2 4 5 3 6 7
4 2 5 1 6 3 7
10
8 5 9 7 1 12 2 4 11 3
9 5 1 7 2 12 8 4 3 11
9
2 7 3 6 8 11 5 9 4
3 7 8 6 11 2 5 4 9

Output
4 5 2 6 7 3 1
9 1 2 12 7 5 3 11 4 8
3 8 11 6 7 4 9 5 2

Explanation
Self Explanation '''

def p(pro,ino,l,r,hm):
    global pos
    if l>r:
        return 
    idx=hm[pro[pos]]
    pos+=1
    p(pro,ino,l,idx-1,hm)
    p(pro,ino,idx+1,r,hm)
    print(ino[idx],end=" ")
    return
for _ in range(int(input())):
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    hm={}
    idx=0
    pos=0
    for i in arr2:
        hm[i]=idx
        idx+=1
    p(arr1,arr2,0,n-1,hm)
    print()

Self Explanatory
