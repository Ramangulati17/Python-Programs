x=int(input("ENTER NUMBER FOR ODD EVEN CHECK "))
remainder=x % 2
if remainder is 0:
    print('NUMBER IS EVEN')
elif remainder!=0:
    print('NUMBER IS ODD')
