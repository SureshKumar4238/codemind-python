a=int(input())
s=0
p=1
for i in str(a):
    s=s+int(i)
    p=p*int(i)
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")