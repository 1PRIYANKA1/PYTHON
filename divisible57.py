#Write a program to accept a number and check if it is divisible by 5 and 7. 
n=int(input("enter the number"))
if  n%5==0 and n%7==0:
    print("divisible by 5 & 7")
elif n%5==0 and n%7!=0:
    print("divisible by 5")
elif n%5!=0 and n%7==0:
    print("divisibe by 7")
else:
    print("not divisible by 5 & 7")
