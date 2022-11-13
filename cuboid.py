#Accept three dimensions length (l), breadth(b) and height(h) of a cuboid and print surface area and volume. 
l=float(input("enter length"));
b=float(input("enter breadth"));
h=float(input("enter height"));
SA=2*(l*b+l*h+b*h)
V=l*b*h
print(SA);
print(V);