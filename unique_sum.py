n=int(input())
sum=0
arr=list(map(int,input().strip().split())) #1 2 2 3 3 3 4
for i in range(0,n):
    c=1
    for j in range(0,n):
        if arr[i]!=-1:
            
            if arr[i]==arr[j] and i!=j:
                c=c+1
                arr[i]=-1
            
            
    if c==1:
       sum=sum+arr[i]
print(sum)       
         