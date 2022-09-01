n=int(input("enter the n value"))
reverse=0
x=n
while(n!=0):
 rem=n%10
 reverse=reverse*10+rem
 n=n//10
print("reverse of the given number is",reverse)
if(reverse==x):
    print("given number is palindrome")
else:
    print("given number is not palindrome")
