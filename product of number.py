n=int(input("enter the number"))
product=1
while(n!=0):
    rem=n%10
    product=product*rem
    n=n//10
print("the product of thr given number is",n,product)    
    
