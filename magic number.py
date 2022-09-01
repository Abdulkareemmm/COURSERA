n=int(input("enter a number"))
x=n
while(x>=10):
    sum=0
    while(x>0):
        rem=x%10
        sum=sum+rem
        x=x//10
    x=sum
if(x==1):
    print(n,"magic number")
else:
    print(n,"not a magic number")
        
        
        
