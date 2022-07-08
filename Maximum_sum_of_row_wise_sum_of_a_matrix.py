m,n=map(int,input().split())
a=[]
s=0
max=0
for i in range(m):
    l=list(map(int,input().split()))
    if len(l)==n:
        a.append(l)
for i in range(m):
    for j in range(n):
        s=s+a[i][j]
    if max<s:
        max=s
    s=0
print(max)    
        