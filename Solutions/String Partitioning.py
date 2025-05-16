'''String Partitioning 
You are given a string S of length N and you are also given a list L of length K containing substrings of S. Find the total number of ways in which the string S can be partitioned such that each partition contains a string from the list L and the minimum number of partitions that have to be made in S to satisfy that condition.

Input Format
The first line of input contains T - the number of test cases. It's followed by 4T lines, where the first line contains N - the size of the string S. The second line contains the string S. The third line contains K - the length of the list and the fourth line contains K strings each separated by a space.
Note that under the constraints of this problem, it is guaranteed that such an answer always exists.

Output Format
For each test case, print the total number of ways in which the string S can be partitioned such that each partition contains a string from the list L and also print the minimum number of partitions required to satisfy that condition, separated by a space on a new line.

Constraints
30 points
1 <= T <= 10
1 <= N <= 10
'a' <= S[i] <= 'z'
3 <= K <= 100

70 points
1 <= T <= 100
1 <= N <= 30
'a' <= S[i] <= 'z'
3 <= K <= 300

100 points
1 <= T <= 100
1 <= N <= 50
'a' <= S[i] <= 'z'
3 <= K <= 500

Example
Input
2
15
smartinterviews
9
smart inter sm art s mart view views int
10
hackerrank
11
hack r ank h er ra k ckerran a nk ck

Output
6 2
7 3

Explanation

Test-Case 1
There are 6 ways in which the string can be partitioned.
s | mart | inter | view | s
s | mart | inter | views
sm | art | inter | view | s
sm | art | inter | views
smart | inter | view | s
smart | inter | views
The way in which the string can be partitioned with minimum number of partitions here is: smart | inter | views .
The number of partitions here is 2

Test-Case 2
There are7 ways in which the string can be partitioned.
The way in which the string can be partitioned with minimum number of partitions here is: hack | er | r | ank.
The number of partitions here is 3'''


def solv(s,lst,idx,c,mp,par):
    if idx==len(s):
        c[0]+=1
        mp[0]=min(mp[0],par)
        return
    for i in lst:
        n=len(i)
        if idx+n<=len(s) and s[idx:idx+n]==i:
            solv(s,lst,idx+n,c,mp,par+1)
for i in range(int(input())):
    n=int(input())
    s=input()
    k=int(input())
    lst=input().split()
    c=[0]
    mp=[float('inf')]
    solv(s,lst,0,c,mp,0)
    print(c[0],mp[0]-1)
