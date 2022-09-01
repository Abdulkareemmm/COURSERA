n=int(input("entera number"))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print("not a prime number")
            break
    else:
            print("primr number")
else:            
    print("not a prime number")            
