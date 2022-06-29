n=int(input())#
q=[]
for i in str(n):
    q.append(int(i))
for i in range(len(q)):
    if(q[i]==6):
        q[i]=9
        break
for i in range(len(q)):
    print(q[i],end="")