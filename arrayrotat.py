arr1=int(input("enter the range= "))
list=[]
for i in range(0,arr1):
    ele=int(input("enter the elements"))
    list.append(ele)
    print(list)

x=int(input("enter the number to be rotated"))
for i in range(0,x):
    el=list.pop(0);
    list.append(el)

print(list)