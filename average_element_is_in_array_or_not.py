n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(n):
    s=s+a[i]
m=s//n    
for i in range(n):
    if a[i]==m:
        print("True")
        break
else:
    print("False")