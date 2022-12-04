x=int(input("enter array elements= "))
list=[]
maxi=0
for i in range(0,x):
    ele=int(input("enter number= "))
    list.append(ele)
    print(list)
maxi=max(list)
print("largest element is= ",maxi)