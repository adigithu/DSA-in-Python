year=int(input("Enter a year: "))
if year%400 or (year%4 == 0 and year%100!=0) ==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")