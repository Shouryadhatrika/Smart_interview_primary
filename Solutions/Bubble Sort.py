'''Implement Bubble Sort and print the total number of swaps involved to sort the array.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the size of the array. The next line contains N integers - the elements of the array.

Output Format
For each test case, print the total number of swaps, separated by a new line.

Constraints
1 <= T <= 100
1 <= N <= 100
-1000 <= ar[i] <= 1000

Example
Input
4
8
176 -272 -272 -45 269 -327 -945 176
2
-274 161
7
274 204 -161 481 -606 -767 -351
2
154 -109

Output
15
0
16
1

Explanation

Self Explanatory'''
def bubblesort(blist):
    cmpcount,swapcount=0,0
    for j in range(len(blist)):
        for i in range(1,len(blist)-j):
             cmpcount+=1
             if blist[i-1]>blist[i]:
                swapcount+=1
                blist[i-1],blist[i]=blist[i],blist[i-1]
    return cmpcount,swapcount
t=int(input())
results=[]     

for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    cmpcount,swapcount=bubblesort(arr)
    results.append(swapcount)
for res in results:
    print(res)   
