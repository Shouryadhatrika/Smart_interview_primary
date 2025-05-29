'''Number of Monotonous Substrings 
Given a string S, print the number of monotonous substrings of S. Since the answer may be too large, print answer modulo 1e9 + 7. A string is monotonous if all the characters of the string are the same.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases. The first line of each test case contains an integer N - denoting the size of string.
The second line of each test case contains the string S consisting of lowercase characters.

Output Format
Print the number of monotonous substrings of S.

Constraints
20 points
1 <= N <= 102

30 points
1 <= N <= 103

50 points
1 <= N <= 105

General Constraints
1 <= T <= 100
'a' <= S[i] <= 'z'

Example
Input
2
8
abbcccaa
4
aaaa

Output
13
10

Explanation

Self Explanatory'''
mod=int(1e9+7)
for _ in range(int(input())):
    n=int(input())
    s=input()
    d=0
    c=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            c+=1
        else:
                d=(d+(c*(c+1)//2)%mod)%mod
                c=1
    print((d+(c*(c+1)//2)%mod)%mod)
