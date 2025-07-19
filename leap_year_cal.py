year = float(input("Enter the Year:"))

if year%4==0 and year % 100 !=0:
    print("The given year is a leap year")

elif  year% 400 ==0:
    print("The given year is a leap year")
else:
    print("given year is not a leap year or is invalid")




