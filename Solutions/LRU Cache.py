'''LRU Cache
Design and implement a data structure for the Least Recently Used (LRU) cache. Given a list of page numbers, insert them in a cache of size K in an LRU fashion. This simply means that when the cache is full and a new entry comes, you need to replace the Least Recently Used entry in the cache with the latest entry.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains N and K - the number of pages and the cache size. Second, each includes a list of N page numbers separated by space.

Output Format
For each test case, print the final contents of the cache in an LRU fashion, separated by a newline.

Constraints
1 <= p[i] <= 100000
1 <= T <= 1000

50 points
1 <= N, K <= 100

100 points
1 <= N, K <= 5000

Example
Input
3
5 3
3 8 2 8 1 
8 5
4 7 3 10 7 8 5 3 
10 5
6 5 6 2 3 14 2 1 10 10 

Output
2 8 1 
10 7 8 5 3 
3 14 2 1 10 

Explanation 

Self Explanatory
'''
from collections import OrderedDict
def lru(T,test_cases):
    res=[]
    for i in range(T):
        n,k=test_cases[i][0]
        pages=test_cases[i][1]
        cache=OrderedDict()

        for page in pages:
            if page in cache:
                cache.move_to_end(page)
            else:
                if len(cache)==k:
                    cache.popitem(last=False)
                cache[page]=True
        res.append(' '.join(map(str,cache.keys())))
    return res
T=int(input())
test_cases=[]
for _ in range(T):
    n,k=map(int,input().split())
    pages=list(map(int,input().split()))
    test_cases.append(((n,k),pages))
for res in lru(T,test_cases):
    print(res)
