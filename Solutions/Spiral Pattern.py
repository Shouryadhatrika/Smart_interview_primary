  '''  Spiral Pattern bookmark_borderPrint the given spiral pattern using '*'. See the example for more details.

Input Format
The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single integer N - the size of the pattern.

Output Format
For each test case, print the test case number as shown, followed by the pattern, separated by a new line.

Constraints
1 <= T <=100
1 <= N <=100

Example
Input
2
5
10

OutputCase #1:
* * * * * 
        * 
* * *   * 
*       * 
* * * * * 
Case #2:
* * * * * * * * * * 
                  * 
* * * * * * * *   * 
*             *   * 
*   * * * *   *   * 
*   *     *   *   * 
*   *         *   * 
*   * * * * * *   * 
*                 * 
* * * * * * * * * * 
Explanation

Self Explanatory '''

for i in range(int(input())):
    n=int(input())
    print("Case #",i+1,":",sep="")
    if (n==2):
        print("* *")
        print("* *")
        continue
    mat=[[' 'for i in range(n)]for i in range(n)]
    top=left=0
    bottom=right=n-1
    while top<=bottom and left<=right:
        for k in range(left-1,right+1):
            mat[top][k]="*"
        top+=2
        for k in range(top-1,bottom+1):
            mat[k][right]="*"
        right-=2
        if top<=bottom:
            for k in range(right+1,left-1,-1):
                mat[bottom][k]="*"
            bottom-=2
        if left<=right:
            for k in range(bottom+1,top-1,-1):
                mat[k][left]="*"
            left+=2
    for i in mat:
        print(*i)
