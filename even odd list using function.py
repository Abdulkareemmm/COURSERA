def count(list):
    evenlist=[]
    oddlist=[]
    for i in list:
        if(i%2==0):
            evenlist.append(i)
        else:
             oddlist.append(i)
    return evenlist,oddlist                 
list=[1,2,3,4,5,6,7,8,9,10]
el,ol=count(list)
print("even list",el)
print("odd list",ol)
