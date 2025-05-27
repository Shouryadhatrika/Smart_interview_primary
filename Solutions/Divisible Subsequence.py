'''Divisible Subsequence
Given an array of size N, check if there exists a subsequence of the given array whose sum is divisible by K.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains 2 space-separated integers - N and K. The second line contains the elements of the array.

Output Format
For each test case, print "Yes" if there is a subsequence whose sum is divisible by K, "No" otherwise, separated by a new line.

Constraints
30 points
1 <= T <= 100
1 <= N <= 10
1 <= K <= 100
0 <= arr[i] <= 50

70 points
1 <= T <= 100
1 <= N <= 100
1 <= K <= 103
0 <= arr[i] <= 50

Example
Input
2
5 2
8 1 6 5 3
5 20
8 10 6 5 3

Output
Yes
No

Explanation

Test Case 1
There exists multiple subsequence whose sum is divisible by K=2: [8], [1,5], [8,6,5,3].

Test Case 2
None of the subsequences sum is divisible by K=20.'''

for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    a=set()
    for i in arr:
        b=set()
        m=i%k
        b.add(m)
        for j in a:
            b.add((j+m)%k)
        a.update(b)
    print("Yes"if 0 in a else "No")
