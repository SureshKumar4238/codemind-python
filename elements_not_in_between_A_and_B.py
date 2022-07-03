n=int(input())
arr=list(map(int,input().strip().split()))
a,b=map(int,input().split())
c=0
for i in range(0,n):
    if arr[i]<a or arr[i]>b:
        c=c+1
        print(arr[i],end=" ")
if c==0:
    print(-1)