row=int(input("enter the number of rows"))
a=74
for i in range(row):
    for j in range(i+1):
        print(chr(a),end=" ")
        a=a+1
    print()
   
