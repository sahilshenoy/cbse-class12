# Check if anyear is a leap year or not

year = int(input("Enter the year to check: "))
if((year%4==0) and (year%100!=0) or (year%400==0)):
    print(year,"is a Leap year.")
else:
    print(year,"is NOT a Leap year.")    