#Accept three sides of triangle as input, and print whether the triangle is valid or not. 
s1=float(input("enter the 1st side"))
s2=float(input("enter the 2nd side"))
s3=float(input("enter the 3rd side"))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    print ("tirangle is valid")
else:
    print("triangle is not valid")