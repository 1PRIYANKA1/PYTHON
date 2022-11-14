#Write a program, which accepts annual basic salary of an employee and calculates and displays the Income tax as per the following rules. 
#Basic: < 1,50,000 Tax = 0, 1,50,000 to 3,00,000 Tax = 20%, > 3,00,000 Tax = 30%
s=int(input("enter the basic salary"))
if s<=150000:
    tax=0
    print("No tax")
    print(tax)
elif s>150000 and s<=300000:
    tax=0
    tax=s*(20/100)
    print("Tax is 20%")
    print(tax)
elif s>300000:
    tax=0
    tax=s*(30/100)
    print("Tax is 30%")
    print(tax)
else:
    print("No tax on basic salary<150000")