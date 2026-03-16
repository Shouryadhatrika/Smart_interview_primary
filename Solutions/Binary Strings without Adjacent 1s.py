'''Binary Strings without Adjacent 1s 
Find the number of binary strings of length N, such that there are no adjacent 1s in that string.

Input Format
The first line of input contains T - number of test cases. It is followed by T lines, each line contains N - length of the binary string.

Output Format
For each test case, print the number of binary strings of length N, separated by new line. Since the answer can be very large, print answer % 1000000007 [1e9+7].

Constraints
1 <= T <= 105
1 <= N <= 105

Example
Input
5
3
11
7
5
500

Output
5
233
34
13
73724597

Explanation

Example 1:
You can construct the following binary strings of length 3 with no adjacent 1s:
000, 001, 010, 100, 101'''



def getAll(n):
    res=[0,2,3]
    for i in range(3,n+1):
        res.append((res[i-1]+res [i-2])%1000000007)
    return res
res=getAll(10**5)
for _ in range(int(input())):
    print(res[int(input())])
