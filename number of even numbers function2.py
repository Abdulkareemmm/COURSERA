def count(my_list):
    even=0
    odd=0
    for i in my_list:
        if(i%2==0):
            even=even+1
        else:
            odd=odd+1
    return odd,even
my_list=[1,2,3,4,5,6,7]
o,e=count(my_list)
print("the count of even numbers is",e)
print("the count of odd numbers is",o)
