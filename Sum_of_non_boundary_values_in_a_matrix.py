m,n=map(int,input().split())
k=[]
s=0
for i in range(m):
    l=list(map(int,input().split()))
    if len(l)==n:
        k.append(l)
for i in range(1,m-1):
    for j in range(1,n-1):
        s=s+k[i][j]
print(s)        