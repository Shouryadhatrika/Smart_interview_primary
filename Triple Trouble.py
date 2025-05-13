'''
Triple Trouble 
Given an array of size 3X+1, where every element occurs three times, except one element, which occurs only once. Find the element that occurs only once.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array (of the form 3X + 1) and second line contains the elements of the array.

Output Format
For each test case, print the number which occurs only once, separated by new line.

Constraints
30 points
1 <= T <= 100
1 <= N <= 103
1 <= A[i] <= 105

70 points
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 109

Example
Input
2
10
5 7 8 7 7 9 5 9 5 9
7
10 20 20 30 20 30 30

Output
8
10

Explanation

Self Explanatory'''
def mergesort(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)

    left=arr[low:mid+1]
    right=arr[mid+1:high+1]

    i=j=0
    k=low
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        i+=1
        k+=1    

def fun():
    T=int(input())    
    for _ in range(T):
     n=int(input())
     arr=list(map(int,input().split()))
     mergesort(arr)
     print("sorted array",arr)
fun()     
