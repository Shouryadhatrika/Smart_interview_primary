'''  Print Hollow Diamond Pattern bookmark_borderPrint a hollow diamond pattern using '*'. See examples for more details.

Input Format
The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single odd integer N - the size of the diamond.

Output Format
For each test case, print the test case number as shown, followed by the diamond pattern, separated by a new line.

Constraints
1 <= T <= 100
3 <= N <= 201

Example
Input4
3
7
5
15

OutputCase #1:
 *
* *
 *
Case #2:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
Case #3:
  *
 * *
*   *
 * *
  *
Case #4:
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
*             *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *
Explanation

Self Explanatory   '''


for p in range(int(input())):
    n=int(input())
    x=n//2

    print("Case #{}:".format(p+1))

    for i in range(n//2+1):
        if i==0:
            print(' '*x+'*')
        else:
            print(' '*(x-i)+'*'+' '*(2*i-1)+'*')    
    for i in range(n//2-1,-1,-1):
        if i ==0:
            print(' '*x+'*')
        else:
            print(' '*(x-i)+'*'+' '*(2*i-1)+'*')    
