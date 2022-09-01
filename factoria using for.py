n=int(input("enter the number"))
fact=1
if(n<0):
    print("for negative number factorial is undefined")
else:
 if(n==0):
     print("the factorial of",n,"is",1)
 else:
     for i in range(1,n+1,1):
         fact=fact*i
     print("the factorial of",n,"is",fact)
