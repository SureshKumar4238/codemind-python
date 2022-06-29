n=int(input())
k=[]
while n:
    r=n%10
    n=n//10
    k.append(r)
print(max(k))  