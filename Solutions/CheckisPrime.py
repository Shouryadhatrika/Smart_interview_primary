'''Check isPrime
Given a number N, find out whether the number is a prime number or not.

Input Format
First line of input contains T - the number of test cases. It is followed by T lines, each line contains a single integer N.

Output Format
For each test case, on a new line, print "Yes" if the number is prime or "No" otherwise.

Constraints
30 points
0 <= N <= 109

70 points
0 <= N <= 1018

General Constraints
1 <= T <= 104

Example
Input
3
3
11
15

Output
Yes
Yes
No

Explanation

Self Explanatory'''

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    if is_prime(int(input())):
        print("Yes")
    else:
        print("No")
