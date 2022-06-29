def prime(n):
    if n==1:
        return False
    else:
        
        for i in range(2,int(n*0.5)+1):
            if n%i==0:
                return False
        else:
            return True
n=int(input())
c=0
c2=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i)!=True:
            #print(i)
            c=c+1
print(c)        