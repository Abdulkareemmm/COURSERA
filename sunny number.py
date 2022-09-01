num=int(input("enter a number"))
x=num+1
flag=0
for i in range(1,x):
 if(i*i==x):
   flag=1
   break
if(flag==1):
    print(num,"is a sunny number")
else:
    print(num,"is not a suny number")
