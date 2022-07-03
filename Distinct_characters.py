n=input()
p=n.lower()
k=[]
t=[]
a='abcdefghijklmnopqrstuvwxyz'
for i in p:
    if p.count(i)==1:
        k.append(i)
for i in a:
    if i in k:
        t.append(i)
m=''.join(t)
print(m)