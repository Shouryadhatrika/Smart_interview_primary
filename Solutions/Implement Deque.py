'''Implement Deque 
Implement the DEQUE data structure and perform push / pop operations.

Note: 
 Do not use any inbuilt functions / libraries for the DEQUE.  Input
The first line of input contains T - number of operations. It's followed by T lines, each line contains either "push_front x" or "push_back x" or "pop_front" or "pop_back".

Output
For each of the "pop_front" and "pop_back" operations, print the popped element, separated by a new line. If the deque is empty, print "Empty".

Constraints
1 <= T <= 10000
-100 <= x <= 100

Example
Input
10
push_back 5
pop_front
pop_front
push_back 10
push_front -15
pop_back
push_back -10
push_back 20
pop_front
pop_front

Output
5
Empty
10
-15
-10

Explanation 

Initially, an empty deque is created.

push_back 5: Deque becomes [5].
pop_front: The element 5 is popped from the front, so the deque becomes empty, print 5.
pop_front: Deque is already empty, print "Empty".
push_back 10: Deque becomes [10].
push_front -15: Deque becomes [-15, 10].
pop_back: The element 10 is popped from the back, so the deque becomes [-15], print 10.
push_back -10: Deque becomes [-15, -10].
push_back 20: Deque becomes [-15, -10, 20].
pop_front: The element -15 is popped from the front, so the deque becomes [-10, 20], print -15.
pop_front: The element -10 is popped from the front, so the deque becomes [20], print -10.'''

from collections import deque
q=deque()
for _ in range(int(input())):
    s=list(map(str,input().split()))
    if s[0]=='push_front':
        q.appendleft(int(s[1]))
    elif s[0]=='pop_front':
        if len(q)==0:
            print("Empty")
        else:
            print(q.popleft())
    elif s[0]=='push_back':
        q.append(int(s[1]))
    else:
        if len(q)==0:
            print("Empty")
        else:
            print(q.pop())
