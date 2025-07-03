'''Implement Stack 
Implement the Stack data structure and perform push / pop operations.

Note: 
 Do not use any inbuilt functions / libraries for the Stack.  Input Format
The first line of input contains T - number of operations. It is followed by T lines, each line contains either "push x" or "pop".

Output Format
For each "pop" operation, print the popped element, separated by a newline. If the stack is empty, print "Empty".

Constraints
1 <= T <= 10000
-100 <= x <= 100

Example
Input
8
push 5
pop
pop
push 10
push -15
pop
push -10
pop

Output
5
Empty
-15
-10

Explanation

Self Explanatory

'''

arr=[0]*201
t=-1
def push(x):
    global t
    t=t+1
    arr[t]=x
def pop():
    global t
    if t!=-1:
        print(arr[t])
        t=t-1
    else:
        print("Empty")
for _ in range(int(input())):
    s=input().split()
    if s[0]=="push":
        push(int(s[1]))
    else:
        pop()
