''' Smart Square 
Consider matrix of size 3x3. A matrix is said to be a smart matrix, if it consists of distinct numbers from 1 to 9 and the sum of every row, column and diagonal is divisible by 5. Given a matrix, find the minimum cost of converting it to a smart square by changing zero or more of its cells. We can convert any number a to b in the range of [1,9] at cost |a-b|.

Input Format
The first line of input contains T - the number of test cases. It's followed by 3T lines. Each test case contains a 3x3 matrix with distinct numbers from 1 to 9.

Output Format
For each test case, print the minimum cost to convert the matrix into a smart square, separated by a new line.

Constraints
1 <= T <= 105

Example
Input
3
4 9 2
3 5 7
6 8 1
8 6 1
3 5 2
4 9 7
1 4 6
3 5 9
2 7 6

Output
4
0
10

Explanation

Test Case 1
We can convert the given matrix to the following smart square which gives a minimum cost of 4.
4 9 2
3 5 7
8 6 1

Test Case 2
The given matrix is already a smart matrix.

Test Case 3
We can convert the given matrix to the following smart matrix which gives a minimum cost of 10.
1 2 7
6 5 9
3 8 4'''

def isMagics(ar):
    return (ar[0]+ar[1]+ar[2])%5==0 and (ar[3]+ar[4]+ar[5])%5==0 and (ar[6]+ar[7]+ar[8])%5==0 and (ar[0]+ar[3]+ar[6])%5==0 and (ar[1]+ar[4]+ar[7])%5==0 and (ar[2]+ar[5]+ar[8])%5==0 and (ar[0]+ar[4]+ar[8])%5==0 and (ar[2]+ar[4]+ar[6])%5==0
def cost(ar,inp_mat):
    c=0
    for i in range(9):
        c+=abs(ar[i]-inp_mat[i])
    return c 
from itertools import permutations
valid=[]
for i in permutations (range(1,10)):
    if isMagics(i):
        valid.append(i)
n=int(input())
for _ in range(n):
    inp_mat=[]
    for _ in range(3):
        inp_mat+=(list(map(int,input().split())))
    arr=[0]*9
    used=[False]*10
    ans=float('inf')
    for i in valid:
        ans=min(ans,cost(i,inp_mat))
    print(ans)
