#Write a program to check whether given character is a digit or a character in lowercase or uppercase alphabet. 
ch=input("enter a character")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    print("the charactter",ch,"is an alphabet")
elif ch>='0' and ch<='9':
    print("the charactter",ch,"is a digit")
else:
    print("special character")
