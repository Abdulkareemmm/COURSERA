n=input("enter the binary values")
list1=list(n)
list1.reverse()
sum=0
for i in range(len(list1)):
    sum=sum+int(list[i])*2**i
    print("the euivalent decimal number is",sum)
    
