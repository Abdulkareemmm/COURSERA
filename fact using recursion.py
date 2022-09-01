def fact(n):
    if(n==1):
            return n
    else:
            return n*fact(n-1)
n=int(input("enter the number"))
if(n<0):
    print(" for negitive number fact is undefined")
elif(n==0):
        print("the factorial for zero is",1)
else:
    result=fact(n)
    print("the factorial of",n,"is",result)
