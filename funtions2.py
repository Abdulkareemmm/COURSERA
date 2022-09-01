def buzz(n):
    if(n%7==0 or n%10==7):
        print("given number is buzz number",n)
    else:
        print("given number is not buzz number",n)
n=int(input("enter the a value"))
buzz(n)
