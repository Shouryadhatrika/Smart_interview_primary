
'''Intersection of 2 Line Segments
Given the end points of 2 line segments, check if the line segments intersect.

Input Format
First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains 4 integers Sx, Sy, Ex, Ey - end points of the first line segment and the second line contains the end points of the second line segment.

Output Format
For each test case, print "Yes" if the line segments intersect, print "No" otherwise, separated by newline.

Constraints
1 <= T <= 105
-100 <= Sx, Sy, Ex, Ey <= 100

Example
Input
2
1 1 5 5
1 2 4 3
1 1 5 5
1 2 4 5

Output
Yes
No

Explanation 

Self Explanatory'''
for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    a=(y2-y1)*(x3-x2)-(x2-x1)*(y3-y2)
    b=(y2-y1)*(x4-x2)-(x2-x1)*(y4-y2)
    c=(y4-y3)*(x1-x4)-(x4-x3)*(y1-y4)
    d=(y4-y3)*(x2-x4)-(x4-x3)*(y2-y4)
    Flag="No"
    if a*b<0 and c*d<0:
        Flag="Yes"
    else:
        if a==0 and (min(x1,x2)<=x3<=max(x1,x2)and min (y1,y2)<=y3<=max(y1,y2)):
            Flag="Yes"
        if b==0 and(min(x1,x2)<=x4<=max(x1,x2)and min (y1,y2)<=y4<=max(y1,y2)):
            Flag="Yes"
        if c==0 and (min(x3,x4)<=x1<=max(x3,x4)and min (y3,y4)<=y1<=max(y3,y4)):
            Flag="Yes"
        if d==0 and (min(x3,x4)<=x2<=max(x3,x4)and min (y3,y4)<=y2<=max(y3,y4)):
            Flag="Yes"
    print(Flag)
