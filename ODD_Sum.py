n=int(input())
a=list(map(int,input().split()))
os=0
for i in range(n):
    if a[i]%2!=0:
        os=os+a[i]
print(os)        