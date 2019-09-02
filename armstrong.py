#Armstrong number CHECK
num=int(input("Enter The Number between 100 and 999 "))
rem1=int(num%100)
if rem1==0:
    val1=int(num/100)
    val4=int(val1**3)
    if val4==num:
      print('Number is armstrong number')
    else:
      print('number is not armstrong number')
elif rem1 !=0:
     rem2=int(rem1%10)
     val1=int(num/100)
     val2=int(rem1/10)
     val4=int((val1**3)+(val2**3)+(rem2**3))
     print('val1',val1)
     print('val2',val2)
     print('rem2',rem2)
     print('val4',val4)
     if val4==num:
       print('Number is armstrong number')
     else:
       print('number is not armstrong number')
