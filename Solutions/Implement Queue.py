'''Implement Queue 
Implement the Queue data structure and perform Enqueue / Dequeue operations.

Note: 
 Do not use any inbuilt functions / libraries for the Queue.  Input Format
The first line of input contains T - number of operations. It is followed by T lines, each line contains either "Enqueue x" or "Dequeue".

Output Format
For each "Dequeue" operation, print the dequeued element, separated by a newline. If the queue is empty, print "Empty".

Constraints
1 <= T <= 10000
-100 <= x <= 100

Example
Input
8
Enqueue 5
Dequeue
Dequeue
Enqueue 10
Enqueue -15
Dequeue
Enqueue -10
Dequeue

Output
5
Empty
10
-15

Explanation

Self Explanatory'''

arr=[0]*10000
f=r=-1
def push(x):
    global f,r
    r=r+1
    arr[r]=x
def pop():
    global f,r
    if f!=r:
        print(arr[f+1])
        f=f+1
    else:
        print("Empty")
for _ in range(int(input())):
    s=input().split()
    if s[0]=="Enqueue":
        push(int(s[1]))
    else:
        pop()
