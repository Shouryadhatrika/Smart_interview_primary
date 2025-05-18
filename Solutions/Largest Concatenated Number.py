'''Largest Concatenated Number 
Given an array of integers, find the largest number that can be constructed by concatenating all the elements of the given array.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the size of the array and the second line contains N integers - the elements of the array.

Output Format
For each test case, print the largest number that can be constructed by concatenating all the elements of the given array, separated by a new line.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 1000

Example
Input
3
8
49 73 58 30 72 44 78 23
4
69 9 57 60
2
40 4

Output
7873725849443023
9696057
440

Explanation

Self Explanatory'''
def compare(x,y):
    if x+y>y+x:
        return True
    return False
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if not compare(arr[j],arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=list(map(str,arr))
    arr=bubblesort(arr)
    result="".join(arr)
    if result[0]=="0":
        print("0")
    else:
        print(result)
