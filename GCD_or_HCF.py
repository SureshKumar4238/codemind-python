a,b=map(int,input().split())
if a>b:
    max=a
else:
    max=b
for i in range(max,0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break