'''Sum of Pairs 
Given an array of integers and a number K, check if there exist a pair of indices i,j s.t. a[i] + a[j] = K and i!=j.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, first line of each test case contains N - the size of the array and K, and the next line contains N space separated integers - the elements of the array.

Output Format
For each test case, print "True" if such a pair exists, "False" otherwise, separated by newline.

Constraints
30 points
1 <= T <= 100
2 <= N <= 1000

70 points
1 <= T <= 300
2 <= N <= 10000

General Constraints
-108 <= K <= 108
-108 <= ar[i] <= 108

Example
Input
3
5 -15
-30 15 20 10 -10
2 20
10 10
4 7
-4 0 10 -7

Output
True
True
False

Explanation

Self Explanatory'''
def MergeSort(arr,low,high):
    if(low>=high):
        return
    mid=(low+high)//2
    MergeSort(arr,low,mid)
    MergeSort(arr,mid+1,high)    
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
    while (p1<=mid):
            temp.append(arr[p1])
            p1+=1
    while (p2<=high):
            temp.append(arr[p2])
            p2+=1
    for i in range (len(temp)):
        arr[low+i]=temp[i]
    return    
for _ in range(int(input())):        
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        MergeSort(arr,0,n-1)
        p1=0
        p2=n-1
        flag=False
        while(p1<p2):
            s=arr[p1]+arr[p2]
            if s==k:
                flag=True
                break
            elif s>k:
                p2-=1
            else:
                p1+=1
        print("True" if flag else "False")
