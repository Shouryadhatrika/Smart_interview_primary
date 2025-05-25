'''Rearrange Sequence - 2.
You are given an array of size N containing integers which may not be unique. Find the size of the largest subarray that can be rearranged to form a strictly contiguous sequence.

Input Format
The first line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

Output Format
For each test case, print the size of the largest subarray that can be rearranged to form a contiguous sequence, on a new line.

Constraints
30 points
1 <= T <= 100
4 <= N <= 100

70 points
1 <= T <= 100
4 <= N <= 1000

General Constraints
0 <= A[i] <= 105

Example
Input
2
5
4 3 3 1 1
9
8 8 6 7 3 5 7 1 1

Output
2
3

Explanation

Test-Case 1
The largest subarray which can be rearranged to form a contiguous sequence here, is {4, 3} which can be rearranged to form {3, 4}.

Test-Case 2
The largest subarray which can be rearranged to form a contiguous sequence here, is {8, 6, 7} which can be rearranged to form {6, 7, 8}.'''

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    max_len=0
    for i in range(n):
        seen=set()
        min_val=max_val=arr[i]
        for j in range(i,n):
            if arr[j] in seen:
                break 
            seen.add(arr[j])
            min_val=min(min_val,arr[j])
            max_val=max(max_val,arr[j])
            if max_val-min_val==j-i:
                max_len=max(max_len,j-i+1)
    print(max_len)
