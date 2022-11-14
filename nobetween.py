#Write a program to accept three numbers and check whether the first is between the other two numbers. Ex: Input 20 10 30. Output: 20 is between 10 and 30
x=int(input("enter the 1st number"))
y=int(input("enter the 2nd number"))
z=int(input("enter the 3rd number"))
if x>y and x<z:
    print("True,the first number is between the other two number");
else:
    print("False")