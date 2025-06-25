'''Clockwise Rotation of Array 
for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    m=m%n
    ar1=arr[:n-m]
    ar2=arr[n-m:]
    print(*(ar2+ar1))
