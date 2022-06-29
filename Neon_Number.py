n=int(input())
k=n*n
s=0
for i in str(k):
    s=s+int(i)
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")