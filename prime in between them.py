start=int(input("enter the starting value"))
end=int(input("enter the ending value"))
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print("prime number is",i)

            
