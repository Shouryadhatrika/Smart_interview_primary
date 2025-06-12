'''Game of Letters 
Santa and Banta are playing a game of letters.

The rules are as follows:
1. Initially they have a string consisting of lowercase English alphabets only.
2. Each of them takes a turn.
3. In each turn, a player removes some alphabets from the string (at least one). All the alphabets removed by a player in a turn must be the same. To understand it better, say a player in his turn removes 3 characters. Now all the 3 removed characters must be the same, so all 3 must be either 'a' or 'b' or 'c' or...
4. The player who is unable to make a move loses the game.

You are given the string. Assume Santa always plays the first move, you have to print the name of the winner. Assume both players play optimally.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each line contains a single string of lower-case English alphabets.

Output Format
For each test case, print the name of the winner, separated by a new line.

Constraints
1 <= T <= 1000
1 <= len(S) <= 104
'a' <= S[i] <= 'z'

Example
Input
3
aaa
abab
abacd

Output
Santa
Banta
Santa

Explanation

Self Explanatory'''
t=int(input())
for _ in range(t):
    s=input().strip()
    c=[0]*26
    for ch in s:
        c[ord(ch)-ord('a')]+=1
    xor_sum=0
    for cnt in c:
        xor_sum^=cnt
    if xor_sum==0:
        print("Banta")
    else:
        print("Santa")
