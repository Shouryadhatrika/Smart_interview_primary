'''Number of Valid Subarrays

You are given an array containing only 0s and 1s. You have to find the number of subarrays which has equal number of 0s and 1s.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines - the first line contains N - the size of the array. The second line contains the elements of the array.

Output Format
For each test case, output the number of subarrays having equal number of 0s and 1s, separated by a newline.

Constraints
10 points
1 <= T <= 100
1 <= N <= 100

20 points
1 <= T <= 100
1 <= N <= 1000

70 points
1 <= T <= 100
1 <= N <= 50000

Example
Input
3
4
1 0 1 0
10
1 0 1 0 0 1 0 0 1 1
4
1 1 1 1

Output
4
14
0

Explanation

Self Explanatory
'''


T=int(input())
for _ in range(T):
    n=int(input())
    ar=list(map(int,input().split()))
    for i in range(n):
        if ar[i]==0:
            ar[i]=-1
    p_sum=0
    count_map={0:1}
    count=0
    for num in ar:
        p_sum+=num
        if p_sum in count_map:
            count+=count_map[p_sum]
            count_map[p_sum]+=1
        else:
            count_map[p_sum]=1
    print(count)
