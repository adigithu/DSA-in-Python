age=int(input("Enter a valid age: "))
day=input("Enter the day: ")
price=12 if age>=18 else 8
if day=="Wednesday":
    price=price-2
print(f"Ticket price for you is {price}")