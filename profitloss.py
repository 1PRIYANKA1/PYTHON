#Accept the cost price and selling price from the keyboard. Find out if the seller has made a profit or loss and display how much profit or loss has been made.
c=int(input("enter the cost price"))
s=int(input("enter the selling pricce"))
if s>c:
    price=s-c
    print("profit")
    print(price)
elif c>s:
    price=c-s
    print("loss")
    print(price)
else :
    print("no profit no loss")