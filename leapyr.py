#Accept any year as input through the keyboard. Write a program to check whether the year is a leap year or not.
y=int(input("enter a year"))
if y%4==0 and y%100!=0 or y%400==0:
    print("leap year")
else:
    print("not a leap year")