n=int(input())
arr=list(map(int,input().strip().split()))
k=[]
sum=0
c=0
for i in range(n):
    if arr[i]!=-1:
        c=1
        for j in range(n):
            if arr[i]==arr[j] and i!=j:
                c=c+1
                arr[j]=-1
        if arr[i]==c:
            k.append(arr[i])
if len(k)==0:
    print(-1)
else:
    
    print(min(k),max(k))