def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
n=int(input())            
if prime(n):
    k=str(n)
    k=k[ : : -1]
    if prime(int(k)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print('not prime')