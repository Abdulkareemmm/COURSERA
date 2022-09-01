n=int(input("enter the number"))
count=0
sum=0
x=n
while(n!=0):
 count=count+1
 n=n//10
n=x
while(n!=0):
    rem=n%10
    sum=sum+rem**count
    n=n//10
if(sum==x):
    print("given number is amstong number")
else:
    print("given number is not amstong number")
    
