#Accept the time as hour, minute and seconds and check whether the time is valid.
h=int(input("enter hour"))
m=int(input("enter minute"))
s=int(input("enter seconds"))
if (h>=0 and h<24) and (m>=0 and m<60) and (s>=0 and s<60):
    print("valid")
else:
    print("invalid")