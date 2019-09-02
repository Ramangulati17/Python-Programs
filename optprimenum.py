x=int(input("ENTER NUMBER FOR PRIME CHECK "))
p=x
y=int(x/2)
for x in range(2,y+2):
    remainder=p % x
    if remainder is 0:
        print('NUMBER IS NOT PRIME')
        break
    elif remainder!=0 and x==(y+1):
            print('NUMBER IS PRIME')
