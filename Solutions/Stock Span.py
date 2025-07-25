'''Stock Span 
You are given a series of daily price quotes for a stock and you need to calculate the span of the stock’s price for each day. The span Si of the stock’s price on the current day i is defined as the maximum number of consecutive days just before the current day[including the current day], on which the price of the stock is less than or equal to its price on the current day.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains N - the size of the array. The second line contains N integers - the elements of the array, ith element denotes the stock price on ith day.

Output Format
For each test case, print a space-separated Stock Span Array, separated by a new line.

Constraints
30 points
1 <= T <= 100
1 <= N <= 103

70 points
1 <= T <= 200
1 <= N <= 104

General Constraints
0 <= A[i] <= 104

Example
Input
2
7
100 80 60 70 60 75 85
10
0 7 3 6 6 9 18 0 16 0

Output
1 1 1 2 1 4 6
1 2 1 2 3 6 7 1 2 1

Explanation 

Self Explanatory'''

def calspan(prices,n):
    span=[0]*n
    stack=[]
    for i in range(n):
        while stack and prices[stack[-1]]<=prices[i]:
            stack.pop()
        if not stack:
            span[i]=i+1
        else:
            span[i]=i-stack[-1]
        stack.append(i)
    return span
def main():
    T=int(input())
    for _ in range(T):
        n=int(input())
        prices=list(map(int,input().split()))
        span=calspan(prices,n)
        print(" ".join(map(str,span)))
if __name__=="__main__":
    main()
