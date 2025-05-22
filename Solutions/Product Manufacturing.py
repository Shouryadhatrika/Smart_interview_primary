''' Product Manufacturing
There are M manufacturers and each of them produces a range of products.
M1: [a1, b1]
M2: [a2, b2]
and so on...

Given a product ID, find how many manufacturers produce the given product.

Input Format
The first line of input contains T - the number of test cases. The first line of each test case contains an integer M. The Next M lines contain the ith manufacturer's range of products id's - starting(S) and ending(E) (both inclusive). The next line contains Q - number of queries and the next Q lines contain a single integer denoting the ID of the product.

Output Format
For each test case, print the number of merchants producing the given product for each query, separated by a new line.

Constraints
20 points
1 <= T <= 100
1 <= M, Q <= 1000
1 <= S <= E <= 104
1 <= ID <= 104

30 points
1 <= T <= 100
1 <= M, Q <= 10000
1 <= S <= E <= 104
1 <= ID <= 104

50 points
1 <= T <= 100
1 <= M, Q <= 10000
1 <= S <= E <= 109
1 <= ID <= 109

Example
Input
1
4
1 3
1 6
3 5
5 9
4
3
8
6
10

Output
3
1
2
0

Explanation

Self Explanatory'''

for _ in range(int(input())):
    m=int(input())
    c=[0]*10002
    for _ in range(m):
        s,e=map(int,input().split())
        c[s]+=1
        if e+1<len(c):
            c[e+1]-=1
    for i in range(1,len(c)):
        c[i]=c[i]+c[i-1]
    for _ in range(int(input())):
        n=int(input())
        print(c[n] if n<len(c) else 0)
