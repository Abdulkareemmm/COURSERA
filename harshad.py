n=int(input("enter the number"))
x=n
sum=0
while(n!=0):
 rem=n%10
 sum=sum+rem
 n=n//10
if(x%sum==0):
  print("the given number is harshad number")
else:
     print("given number is not a harshad number")
     
