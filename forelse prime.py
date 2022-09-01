n=int(input("enter the n value"))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print(n,"not a prime number")
            break
    else:
        print(n," a prime number")
else:
    print("not a prime number")
