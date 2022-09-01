def count(list1):
    even=0
    odd=0
    for i in list1:
        if(i%2==0):
            even=even+1
        else:
            odd=odd+1
    return even,odd    
list1=[1,2,3,4,5,6,7,8,9,10]
e,o=count(list1)
print("the count of even numbers",e)
print("the count of odd numbers",o)


