#Accept the x and y coordinate of a point and find the quadrant in which the point lies. 
x=int(input("enter x coordinate"))
y=int(input("enter y coordinate"))
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print("2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
else:
    print("4th quadrant")