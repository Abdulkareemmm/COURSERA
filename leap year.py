n=int(input("enter a number"))
if(n%100==0 and n%400==0):
    print(n,"given year is leap year")
elif(n%100!=0 and n%4==0):
    print(n, "given year is leap year")
else:
        print(n, "given year is non leap year")
