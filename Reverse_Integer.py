n=int(input())
k=abs(n)
rev=0
while(k):
    r=k%10
    k=k//10
    rev=rev*10+r
if n>0:
    print(rev)
else:
    print(-rev)