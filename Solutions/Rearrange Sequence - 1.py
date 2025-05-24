'''Rearrange Sequence - 1 
You are given an array of size N containing unique integers. Find the size of the largest subarray that can be rearranged to form a contiguous sequence.
A contiguous sequence means that the difference of adjacent elements should be 1.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

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
1 3 2 6 5
9
0 8 6 5 7 10 3 2 1

Output
3
4

Explanation

Test-Case 1
The largest subarray that can be rearranged to form a contiguous sequence is [1, 3, 2] which can be rearranged to form [1, 2, 3].

Test-Case 2
The largest subarray that can be rearranged to form a contiguous sequence is [8, 6, 5, 7] which can be rearranged to form [5, 6, 7, 8].
'''
def ans(arr,n):
    max_len=1
    for i in range(n):
        min_val=arr[i]
        max_val=arr[i]
        seen=set([arr[i]])
        for j in range (i+1,n):
            seen.add(arr[j])
            min_val=min(min_val,arr[j])
            max_val=max(max_val,arr[j])
            crr_len=j-i+1
            if max_val-min_val==crr_len-1 and len(seen)==crr_len:
                max_len=max(max_len,crr_len)
    return max_len
for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        print(ans(arr,n))
