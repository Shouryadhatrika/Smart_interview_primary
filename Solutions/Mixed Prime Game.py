'''Mixed Prime Game
Two people are playing a game of numbers! The rules of the game are:The game is played on a given number N.The players take turns one by one. During each move, the current player can subtract a number p from N, where p is a prime number such that p<=N.The game ends when a player cannot make a move. The first player to have no available move loses the game.Given the value of N, determine whether the person who wins the game is the first or second person to move. Assume first player always plays greedily and second player always plays optimally.

Input Format
The first line of input contains T - number of test cases. Its followed by T lines, each line contains a single integer N.

Output Format
For each test case, print the name of the winner, separated by newline.

Constraints
 30 points 
 1 <= T <= 100 
 1 <= N <= 100

 70 points 
 1 <= T <= 104
 1 <= N <= 104

Example
Input
 4
 10
 5
 3
 25

Output
 Second
 First
 First
 Second

Explanation

Self Explanatory
'''
n=10**4+1
primes=[0,0]+[1]*(n-2)
for i in range(1,int(n**0.5)+1):
    if primes[i]:
        for j in range(i*i,n,i):
            primes[j]=0
game1=[0]*n
game2=[0]*n
prime=[i for i in range(1,n) if primes[i]]
for i in range(2,n):
    if primes[i]:
        cp=i
        game1[i]=1
    elif game2[i-cp]==0:
        game1[i]=1
        
    if primes[i]:
        game2[i]=1
        continue
    idx=0
    while idx<len(prime) and prime[idx]<i:
        if game1[i-prime[idx]]==0:
            game2[i]=1
            break
        idx+=1
for _ in range(int(input())):
    n=int(input())
    if game1[n]:
        print("First")
    else:
        print("Second")
