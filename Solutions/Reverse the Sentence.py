'''Reverse the Sentence 
Given a sentence, reverse the entire sentence word-by-word.

Note: 
 Solve using stack or in-place swap. Do not simply scan, split and print in reverse order.  Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each containing a sentence S of space-separated words of lowercase English alphabet. All the words are separated by a single space.

Output Format
For each test case, print the reversed sentence, separated by a newline.

Constraints
1 <= T <= 1000
1 <= len(S) <= 1000

Example
Input
3
hello world
a b c d
data structures and algorithms

Output
world hello
d c b a
algorithms and structures data

Explanation

Self Explanatory'''
def reverse(p1,p2,arr):
    while p1<=p2:
        arr[p1],arr[p2]=arr[p2],arr[p1]
        p1+=1
        p2-=1
    return arr
for _ in range(int(input())):
    n=list(input())
    arr=reverse(0,len(n)-1,n)
    p1=0
    for i in range(len(arr)):
        if arr[i]==" ":
            p2=i-1
            arr=reverse(p1,p2,arr)
            p1=i+1
    arr=reverse(p1,len(arr)-1,arr)
    print("".join(arr))
