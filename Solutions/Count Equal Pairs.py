'''Count Equal Pairs 
You are given 2 arrays A and B of same size N. A pair is said to be a valid if and only if i < j, A[i] == B[j] and A[j] == B[i]. You have to count total number of valid pairs.

Input Format
First line of input contains T - number of test cases. First line of each test case contains N - size of the array. The second and third line of each test case contains N integers - elements of the array A and B.

Output Format
For each test case, print the count of number of valid pairs, separated by newline.

Constraints
30 points
1 <= N <= 103

70 points
1 <= N <= 105

General Constraints
1 <= T <= 100
0 <= A[i], B[i] <= 109

Example
Input
2
3
1 2 3
3 2 1
5
1 3 7 9 9
3 1 9 7 7

Output
1
3

Explanation

Test Case 1:
There is only one valid pair - (0, 2). This is because A[0] == B[2] and A[2] == B[0].

Test Case 2:
There are 3 valid pairs - (0, 1), (2, 3), (2, 4). For example (0, 1) is valid because A[0] == B[1] and A[1] == B[0].'''
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    hm={}
    c=0
    for i in range(n):
        x=(b[i],a[i])
        if x in hm:
            c+=hm[x]
        y=(a[i],b[i])
        if y in hm:
            hm[y]+=1
        else:
            hm[y]=1
    print(c)
