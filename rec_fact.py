def factorial(x):
    if x==1:
      return 1
    else:
      return(x*factorial(x-1))
#This the example of recursive function where fuction is called by itself
#number entered by user
x=int(input("Enter the number for factorial "))
print("The Factorial of", x ,"is",factorial(x))
