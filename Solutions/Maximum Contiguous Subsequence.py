'''Maximum Contiguous Subsequence 
Given an array, find the length of the longest subsequence whose elements can be re-arranged in a strictly increasing contiguous order. The difference between 2 adjacent elements in the subsequence, after re-arrangement, should be exactly 1.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - size of the array. The next line contains N integers - the elements of the array.

Output Format
For each test case, print the length of the longest subsequence, separated by a new line.

Constraints
1 <= T <= 1000
1 <= N <= 10000
-100000 <= ar[i] <= 100000

Example
Input
3
8
21 -22 -22 5 -31 -24 5 -23
10
18 -33 31 33 30 -14 32 30 16 17
6
6 3 8 5 2 5

Output
3
4
2

Explanation

Test Case-1:
Subsequence is: -22, -24, -23.

Test Case-2: 
Subsequence is: 31, 33, 30, 32.

Test Case-3: 
Subsequence is: 6, 5 or 3, 2.
'''
def findlongestConseqSubSeq(arr,n):
    s=dict()
    ans=0
    for i in arr:
        s[i]=0
    for i in range(n):
        if (arr[i]-1)not in s.keys():
            j=arr[i]
            while(j in s.keys()):
                j+=1
            ans=max(ans,j-arr[i])
    return ans
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(findlongestConseqSubSeq(arr,n))
