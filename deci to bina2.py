n=int(input("enter the decimal number"))
list2=[]
while(n!=0):
    rem=n%2
    list2.append(rem)
    n=n//2
    list2.reverse()
print("the equivalent number is")
for i in  list2:
    print(i,end='')
