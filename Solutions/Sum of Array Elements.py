'''Given an array of integers, find the sum of the elements of the given array.Note: Try to solve this without declaring / storing the array elements.  Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array, and the second line contains the elements of the array.

Output Format
For each test case, print the sum of the elements of the array, separated by a new line.

Constraints
10 points
1 <= N <= 1000
1 <= arr[i] <= 106

40 points
1 <= N <= 1000
1 <= arr[i] <= 1015

General Constraints
1 <= T <= 100

Example
Input
2
3
5 15 3
2
70 100

Output
23
170

Explanation
Self Explanatory.

#CODE:'''


def malli(arr):
    count=0
    for i in arr:
        count+=i
    return count    
t=int(input())        
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(malli(arr))


