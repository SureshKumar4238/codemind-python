n=int(input())
a=0
b=1
if a==n:
    print(a)
elif b==n:
    print(b)
while True:
    c=a+b
    if c==n:
        print("True")
        break
    elif c>n:
        print("False")
        break
    a,b=b,c