ch=str(input("enter a string"))
if ch.isupper():
    a=str.lower(ch)
    print(a)
elif ch.islower():
    a=str.upper(ch)
    print(a)
else:
    print("special character")

