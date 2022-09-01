list1=[1,2,34,56,78,90]
key=int(input("enter the number serch"))
for i in list1:
    if(i==key):
        print("element is found")
        break
else:
    print("element is not found")
