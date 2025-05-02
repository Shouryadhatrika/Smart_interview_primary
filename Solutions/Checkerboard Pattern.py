'''Checkerboard Pattern bookmark_borderYou are given an integer N. Print a 2N×2N checkerboard consisting of 2×2 squares alternating '*' and '-', with the top-left cell being '*'. See the following examples for N = 1,2,3 and 4 respectively.
  N = 1           N = 2                      N = 3
              N = 4
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
4
2

OutputCase #1:
**--**--
**--**--
--**--**
--**--**
**--**--
**--**--
--**--**
--**--**
Case #2:
**--
**--
--**
--**
Explanation

Self Explanatory'''

for  i in range(int(input())):
    n=int(input())
    print("Case #",i+1,":",sep="")
    s1="**"
    s2="--"
    c=0
    for i in range(n*2):
        for j in range(n):
            if j%2==0:
                print(s1,end="")
            else:
                print(s2,end="")
        print()
        c+=1
        if c==2:
            c=0
            s1,s2=s2,s1
