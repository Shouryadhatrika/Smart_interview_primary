'''Sum of XOR of pairs 
You are given an array of integers. Find the sum of XOR of all pairs formed by the elements of the array.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

Output Format
For each test case, print the sum of XOR of all pairs formed by the elements of the array, separated by a new line.

Constraints
20 points
1 <= T <= 100
1 <= N <= 1000
0 <= A[i] <= 105

80 points
1 <= T <= 100
1 <= N <= 105
0 <= A[i] <= 105

Example
Input
3
3
5 12 8
5
4 10 54 11 8
6
15 35 25 10 15 12

Output
52
560
680

Explanation

Test-Case 1
(5 ^ 5) = 0
(5 ^ 12) = 9
(5 ^ 8) = 13
(12 ^ 5) = 9
(12 ^ 12) = 0
(12 ^ 8) = 4
(8 ^ 5) = 13
(8 ^ 12) = 4
(8 ^ 8) = 0

The sum of all the above xor products = 52'''

for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    for i in range(0,31):
        a=0
        for j in range(n):
            if(arr[j]>>i&1)!=1:
                a+=1
        ans=ans+(a*(n-a)*(1<<i))
    print(ans*2)
