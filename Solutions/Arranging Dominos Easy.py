'''Arranging Dominos Easy 
You are given a floor of size 5xN. You have tiles of 2 different sizes: 5 x 1 and 1 x 5. You have to do the flooring using these tiles in the following way:Floor space should be completely covered by tiles.You cannot break tiles, i.e, you have to use a tile entirely or not at all.Any tile should not extend beyond the floor space.Tiles should be placed parallel to the floor boundaries.Your task is to find the number of ways in which you can lay the tiles on the floor.

Input Format
The first line of input contains T - number of test cases. It is followed by T lines, each line contains N - the length of the floor. The width of the floor is fixed to be 5.

Output Format
For each test case, print the number of ways in which you can lay the tiles on the floor, separated by new line. Since the output can be very large, print result % 1000000007 [1e9+7].

Constraints
30 points
1 <= T <= 100
1 <= N <= 20

70 points
1 <= T <= 105
1 <= N <= 105

Example
Input
2
3
7

Output
1
4

Explanation

Test Case 1:
The only way possible is to place 3 tiles vertically.

Test Case 2:
We can tile the floor in the following ways:
*Place 7 tiles vertically 
*Place 1 tile vertically, 5 tiles horizontally and 1 tile vertically
*Place 5 tiles horizontally and 2 tiles vertically
*Place 2 tiles vertically and 5 tiles horizontally'''



mod=int(1e9+7)
lmt=int(10**5)+1
dp=[0]*(lmt)
dp[0]=dp[1]=dp[2]=dp[3]=dp[4]=1
for i in range(1,lmt):
    dp[i]=(dp[i-5]+dp[i-1])%mod
for _ in range(int(input())):
    n=int(input())
    print(dp[n])

