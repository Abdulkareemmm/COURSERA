n=int(input("enter the value"))
x=n
sum=0
while(n!=0):
          rem=n%10
          sum=sum+rem
          n=n//10
print("the su of individual digits",x,sum)
