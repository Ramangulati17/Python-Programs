#fibonacci series
a=0
b=0
i=0
num=int(input("Enter the number"))
for i in range(0,num):
    c=a+b
    print(c,",")
    a=b
    b=c
    if b==0:
        b=b+1
    i=i+1
