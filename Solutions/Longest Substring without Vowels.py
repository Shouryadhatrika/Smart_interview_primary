'''Longest Substring without Vowels 
Given a string S consisting of only lowercase characters, find the length of the longest substring that does not contain any vowel.

Input Format
First line of input contains T - number of test cases. Its followed by T lines, each line contains a string of size N, containing only lowercase english alphabets.

Output Format
For each test case, print the length of the largest substring that does not contain any vowel, separated by newline.

Constraints
1 <= T <= 100
1 <= N <= 104

Example
Input
3
smartinterviews
algorithms
searching

Output
2
4
3

Explanation

Test Case 1:
We have multiple substrings of length 2 which doesn't contain any vowels: "sm", "rt", "nt", "rv", "ws"

Test Case 2:
We have a substring of length 4 which doesn't contain any vowels: "thms"

Test Case 3:
We have a substring of length 3 which doesn't contain any vowels: "rch"'''
for _ in range(int(input())):
    s=input()
    m=0
    vs="aeiou"
    c=0
    for i in s:
        if i in vs:
            c=0
        else:
            c+=1
            m=max(m,c)
    print(m)
