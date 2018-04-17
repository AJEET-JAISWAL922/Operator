import operator
li = [1,2,3,4,5]
for i in range(0,len(li)):
    print(li[i],end=" ")
print("\r")
print("after set iteam")
operator.setitem(li,3,2);###obj,postion,value
for i in range(0,len(li)):
    print(li[i],end=" ")
print("\r")
print("after delete")
operator.delitem(li,2)
for i in range(0,len(li)):
    print(li[i],end=" ")
print("\r")
print("get value")
print(operator.getitem(li,1))

