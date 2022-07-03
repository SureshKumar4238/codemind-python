n=int(input())
arr=list(map(int,input().strip().split()))
c=0
ec=0
for i in range(n-2):
    for j in range(i,i+3):
        if arr[j]%2==0:
            ec=ec+1
    if ec==3:
        c=c+1
    ec=0  
print(c)