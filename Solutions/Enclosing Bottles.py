'''Enclosing Bottles
There are N bottles, with respective radius values represented by ar[i]. Once a bottle is enclosed inside another bottle, it ceases to be visible. You have to minimize the number of visible bottles. Following rules are followed to place ith bottle inside jth bottle.ith bottle is not enclosed in any other bottle.jth bottle does not enclose any other bottle.ar[i] < ar[j]
Input Format
First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - denoting the number of bottles and the second line contains N numbers denoting radius values, separated by space.

Output Format
For each test case, print the minimum number of visible bottles, separated by newline.

Constraints
1 <= T <= 100
1 <= N <= 105
1 <= ar[i] <= 109

Input
2
8
1 1 2 3 4 5 5 4
10
1 2 8 9 1 8 9 1 9 7

Output
2
3

Explanation

Test Case 1:
1st bottle can be enclosed in 3rd one (1=>2). Visible bottles are [1, 2, 3, 4, 5, 5, 4].
2nd bottle can be enclosed in 3rd one (2=>3). Visible bottles are [1, 3, 4, 5, 5, 4].
2nd bottle can be enclosed in 3rd one (3=>4). Visible bottles are [1, 4, 5, 5, 4].
2nd bottle can be enclosed in 3rd one (4=>5). Visible bottles are [1, 5, 5, 4].
1st bottle can be enclosed in 4th one (1=>4). Visible bottles are [5, 5, 4].
3rd bottle can be enclosed in 2nd one (4=>5). Visible bottles are [5, 5].

Remaining bottles can no longer be enclosed, hence the number of visible bottles are 2.'''
m=(10**9)+1
for _ in range(int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    hm={}
    for i in  ar:
        if i in hm:
            hm[i]+=1
        else:
            hm[i]=1
    print(max(hm.values()))
