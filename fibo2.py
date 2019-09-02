#fibonacci series
a=0
b=1
i=0
c=0
num=int(input("Enter the number"))
print(a,",")
print(b,",")
for i in range(0,num-1):
    c=a+b
    print(c,",")
    a=b
    b=c
    i=i+1
