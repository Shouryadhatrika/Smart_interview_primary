''' Protective Villagers 
In a remote village, there is a new long marketplace with N stalls, all lined up along a straight path at positions x1, x2, x3,..., xN. A group of villagers, represented by C individuals, are highly protective of their personal space and tend to get into disputes when placed too close to one another. To maintain peace, the village leader wants to allocate the villagers to these stalls in a way that maximizes the minimum distance between any two of them.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains 2 space-separated integers - N and C. The second contains N integers, where ith integer denotes xi, the location of the ith stall.

Output Format
For each test case, print the largest minimum distance possible, separated by a new line.

Constraints
50 points
2 <= N <= 20
2 <= C <= N

100 points
2 <= N <= 104
2 <= C <= N

General Constraints
1 <= T <= 100
0 <= xi <= 106

Example
Input
1
5 3
1 2 9 8 4

Output
3

Explanation

Example 1:
The villagers should be placed at 1,4,9, which makes the minimum distance between them as 3. Any other combination will give a smaller minimum distance.
'''
def is_possible(stalls,n,c,dist):
    count=1
    last_pos=stalls[0]
    for i in range(1,n):
        if stalls[i]-last_pos>=dist:
            count+=1
            last_pos=stalls[i]
        if count>=c:
            return True
    return False
def max_min_distance(stalls,n,c):
    stalls.sort()
    low=1
    high=stalls[-1]-stalls[0]
    result=0
    while low<=high:
        mid=(low+high)//2
        if is_possible(stalls,n,c,mid):
            result=mid
            low=mid+1
        else:
            high=mid-1
    return result
T=int(input())
for _ in range(T):
    n,c=map(int,input().split())
    stalls=list(map(int,input().split()))
    print(max_min_distance(stalls,n,c))
