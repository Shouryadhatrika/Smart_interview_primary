'''Balanced Parentheses bookmark_borderWrite a program to generate all possible strings with balanced parentheses having N pairs of curly braces.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each containing a single integer N.

Output Format
For each test case, print each combinational pair of balanced parenthesis of length N in a lexicographical order along with the test case number, separated by a new line.

Constraints
1 <= T <= 12
1 <= N <= 12

Example
Input
2
3
2

OutputTest Case #1:
{{{}}}
{{}{}}
{{}}{}
{}{{}}
{}{}{}
Test Case #2:
{{}}
{}{}

Explanation

Self Explanatory'''

def valid(s,op,cl,n):
    if len(s)==n:
        print(s)
        return
    if op<(n//2):
        valid(s+'{',op+1,cl,n)
    if cl<op:
        valid(s+'}',op,cl+1,n)
for i in range(int(input())):
    n=int(input())
    print("Test Case #",i+1,":",sep="")
    valid("",0,0,n*2)
