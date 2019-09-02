x=1
remainder=0
x=int(input("ENTER NUMBER FOR PRIME CHECK "))
p=x
while x>2:
    x=x-1
    remainder=p % x
    if remainder is 0:
        print('NUMBER IS NOT PRIME')
        break
    elif remainder!=0 and x==2:
        print('NUMBER IS PRIME')
