'''Implement Min Heap 
Implement the Min Heap data structure and perform insert / delMin / getMin operations.

Note: 
 Do not use any inbuilt functions / libraries for the Heap.  Input Format
The first line of input contains T - the number of operations. It's followed by T lines. Each line contains either "insert x" or "delMin" or "getMin".

Output Format
For each "getMin" operation, print the minimum element, separated by a newline. If the heap is empty, print "Empty".

Constraints
1 <= T <= 106
-109 <= x <= 109

Example
Input
10
insert 5
getMin
delMin
getMin
insert -15
insert 10
insert -30
getMin
delMin
getMin

Output
5
Empty
-30
-15

Explanation
Self Explanatory 


class MinHeap:
    def __init__(self):
        self.heap=[]
    def insert (self,x):
        self.heap.append(x)
        self._heapify_up(len(self.heap)-1)
    def getMin(self):
        if not self.heap:
            return"Empty"
        return self.heap[0]
    def delMin(self):
        if not self.heap:
            return 
        last=self.heap.pop()
        if self.heap:
            self.heap[0]=last
            self._heapify_down(0)
    def _heapify_up(self,i):
        while i>0:
            parent=(i-1)//2
            if self.heap[i]<self.heap[parent]:
                self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
                i=parent
            else: 
                break 
    def _heapify_down(self,i):
        size=len(self.heap)
        while True:
            smallest=i
            left=2*i+1
            right=2*i+2
            if left<size and self.heap[left]<self.heap[smallest]:
                smallest=left
            if right<size and self.heap[right]<self.heap[smallest]:
                smallest=right
            if smallest!=i:
                self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
                i=smallest
            else:
                break

T=int(input())
heap=MinHeap()
for _ in range(T):
    cmd=input().strip()
    if cmd.startswith("insert"):
        _,val=cmd.split()
        heap.insert(int(val))
    elif cmd=="delMin":
        heap.delMin()
    elif cmd=="getMin":
        print(heap.getMin())
Self Explanatory
