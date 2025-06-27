'''Express as a Power b 
Given a number, check if the number can be expressed as pow(a, b) where both a and b should be greater than 1.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each line contains a single integer N.

Output Format
For each test case, print "Yes" if N can be expressed as pow(a, b), and print "No" otherwise, separated by a new line.

Constraints
30 points
1 <= T <= 104
1 <= N <= 106

70 points
1 <= T <= 106
1 <= N <= 108

Example
Input
5
2
16
31
8880
961

Output
No
Yes
No
No
Yes

Explanation

Self Explanatory'''
T=int(input())
for t in range(T):
    n=int(input())
    find=False
    a=2
    while a*a<=n:
        val=a*a
        while val<=n:
            if val==n:
                find=True
                break
            val=val*a
        if find:
            break
        a+=1
    if find:
        print("Yes")
    else:
        print("No")
