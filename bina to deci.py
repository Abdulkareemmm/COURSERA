n=input("enter the binary number")
list1=list(n)
list1.reverse()
sum=0
for i in range(len(list1)):
    sum=sum+int(list1[i])*2**i
print(sum,"decimal number is")
