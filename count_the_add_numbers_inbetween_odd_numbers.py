n=int(input())
arr=list(map(int,input().strip().split()))
c=0
od=0
for i in range(n-2):
    for j in range(i,i+3):
        if arr[j]%2!=0:
            od=od+1
    if od==3:
        c=c+1
    od=0  
print(c)