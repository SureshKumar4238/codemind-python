m,n=map(int,input().split())
a=[]
s=0
for i in range(m):
    l=list(map(int,input().split()))
    if len(l)==n:
        a.append(l)
for i in range(m):
    for j in range(n):
        if i==0 or j==0 or i==m-1 or j==n-1:
            s=s+a[i][j]
print(s)            