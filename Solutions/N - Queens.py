'''N - Queens
The N-queens puzzle involves placing N queens on an N x N chessboard such that no two queens can attack each other. Given an integer N, display all the unique solutions. Each solution should represent a distinct board configuration with '1' indicating a queen and '0' indicating an empty space.

Input Format
The first line of input contains T - the number of test cases. It is followed by T lines, each line contains N.

Output Format
For each test case, print the distinct solutions in lexicographical reverse order, separated by an empty line. If there is no solution for a given test case, print -1.

Constraints
1 <= T <= 10
1 <= N <= 10

Example
Input
3
4
2
1

Output
0100
0001
1000
0010

0010
1000
0001
0100

-1

1

Explanation

Test Case 1:
There are 2 distinct solutions:
Solution-1
0 Q 0 0
0 0 0 Q
Q 0 0 0
0 0 Q 0

Solution-2
0 0 Q 0
Q 0 0 0
0 0 0 Q
0 Q 0 0

Test Case 2:
There are no valid solutions when N = 2.

Test Case 3:
There is only one cell to place queen when N = 1. So, the number of distinct solutions is 1.'''


def check(mat,row,col,n):
    for i in range(row):
        if mat[i][col]==1:
            return False
    for i in range(row):
        for j in range(n):
            if mat[i][j]==1:
                if(i+j)==(row+col) or i-j ==row-col:
                    return False
    return True

def solve(mat,n,row):
    if n==2 or n==3:
        print(-1)
        return
    if row==n:    
        for i in mat:
            for j in i:
                print(j,end="")
            print() 
        print()       
        return
    for j in range(n)    :
        if check(mat,row,j,n) == True:
            mat[row][j]=1
            solve(mat,n,row+1)
            mat[row][j]=0
for i in range(int(input())):
    n=int(input())            
    mat=[[0 for  i in range(n)]for i in range(n)]
    solve(mat,n,0)
