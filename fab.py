def fib():
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter the number of elements"))
if(n<=0):
    print("not possible plese enter positive number")
else:
    for i in range(n):
        print(fib(i))
