n=int(input())
c=0
c2=0
arr=list(map(int,input().strip().split())) 
'''for i in range(0,n):
    if i%2==0 and arr[i]%2==0:
        c1=c2+1'''
for i in range(0,n):
    if i%2!=0 and arr[i]%2==0:
        c2=c2+1
if c2>0:
    print("False")
else:
    print("True")