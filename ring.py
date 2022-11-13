#Accept inner and outer radius of a ring and print the perimeter and area of the ring (Hint: perimeter = 2 π (a+b) , area = π (a2-b2) ) 
a=float(input("enter inner radius"));
print(a);
b=float(input("enter outer radius"));
print(b);
perimeter=2*3.14*(a+b)
area=3.14*((a*a)-(b*b))
print(perimeter);
print(area);