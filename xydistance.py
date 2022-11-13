#Accept the x and y coordinates of two points and compute the distance between the two points.
import math
x1=int(input("enter the value of x1="))
x2=int(input("enter the value of x2="))
y1=int(input("enter the value of y1="))
y2=int(input("enter the value of y2="))

d=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
print(d);