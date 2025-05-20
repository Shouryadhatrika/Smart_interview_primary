'''Triplet with Sum K 
You are given an integer array and a positive integer K. You have to tell if there exists i,j,k in the given array such that ar[i]+ar[j]+ar[k]=K, i≠j≠k.

Input Format
The first line of input contains T - the number of test cases. Its followed by 2T lines, the first line contains N and K - the size of the array and the number K. The second line contains the elements of the array.

Output Format
For each test case, print "true" if the arrays contains such elements, "false" otherwise, separated by new line.

Constraints
30 points
1 <= T <= 100
3 <= N <= 100

70 points
1 <= T <= 100
3 <= N <= 1000

General Constraints
-105 <= A[i] <= 105
0 <= K <= 105

Example
Input
3
5 60
1 20 40 100 80
12 54
12 45 52 65 21 645 234 -100 14 575 -80 112
3 15
5 5 5

Output
false
true
true

Explanation

Self Explanatory'''
def mergesort(arr,low,high):
    if(low>=high):
        return
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)    
    merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    p1=low
    p2=mid+1
    temp=[]

    while(p1<=mid and p2<=high):
        if(arr[p1]<arr[p2]):
            temp.append(arr[p1])
            p1+=1
        else:
            temp.append(arr[p2])
            p2+=1
    while p1<=mid:
            temp.append(arr[p1])
            p1+=1
    while p2<=high:
            temp.append(arr[p2])
            p2+=1
    for i in range (len(temp)):
        arr[low+i]=temp[i]
for _ in range(int(input())):        
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        mergesort(arr,0,n-1)
        flag=False
        for i in range(n):
            c=arr[i]
            new=k-c
            p1=i+1
            p2=n-1
            while(p1<p2):
                s=arr[p1]+arr[p2]
                if s==new:
                 flag=True
                 break
                elif s>new:
                     p2-=1
                else:
                 p1+=1
            if flag:
                break
        print("true" if flag else"false")
