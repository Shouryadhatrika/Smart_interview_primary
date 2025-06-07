'''Alice and Bob Coin Game-1 


Alice and Bob are playing a game. The game involves N coins and in each turn, a player may remove at most M coins. In each turn, a player must remove at least 1 coin. The player who takes the last coin wins the game.

Alice and Bob decide to play 3 such games while employing different strategies each time. In the first game, both Alice and Bob play optimally. In the second game, Alice decides to play optimally but Bob decides to employ a greedy strategy, i.e., he always removes the maximum number of coins which may be removed in each turn. In the last game, both the players employ the greedy strategy. Find out who will win each game.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each containing an integer N - the total number of coins, M - the maximum number of coins that may be removed in each turn, and a string S - the name of the player who starts the game, separated by space.

Output Format
For each test case, print the name of the person who wins each of the three games on a newline. Refer to the example output for the format.

Constraints
1 <= T <= 105
1 <= N <= 1018
1 <= M <= N

Example
Input
2
5 3 Bob
10 3 Alice

Output
Test-Case #1:
G1: Bob
G2: Alice
G3: Alice

Test-Case #2:
G1: Alice
G2: Alice
G3: Bob

Explanation

Test-Case 1
In G1 where both employ optimal strategies: Bob will take 1 coin and no matter what Alice plays, Bob will be the one who takes the last coin.
In G2 where Alice employs an optimal strategy and Bob employs a greedy strategy: Bob will take 3 coins and Alice will remove the remaining 2 coins.
In G3 where both employ greedy strategies: Bob will take 3 coins and Alice will remove the remaining 2 coins.
'''
for i in range(int(input())):
    n,m,f=input().strip().split()
    n,m=int(n),int(m)
    s="Bob" if f=="Alice" else"Alice"
    if n%(m+1)==0:
        g1=s
    else:
        g1=f
    if m==1:
        if n%2==0:
            g2=s
        else:
            g2=f
    else:
        if f=="Alice":
            if n==m+1:
                g2=s
            else:
                g2=f
        else:
            if n<=m or n==(m*2)+1:
                g2=f
            else:
                g2=s
    if n%(m*2)<=m and n%(m*2)>0:
        g3=f
    else:
        g3=s
    print("Test-Case #",i+1,":",sep="")
    print("G1:",g1)
    print("G2:",g2)
    print("G3:",g3)
    print()
