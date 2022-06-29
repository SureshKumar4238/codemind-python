a=int(input())
p=1
sum=0
for i in str(a):
    sum=sum+int(i)**p
    p=p+1
if(a==sum):
    print("True")
else:
    print("False")