#Write a program to check if a year is leap year or not.
#If a year is divisible by 4 then it is leap year but if the year is century year
# like 2000, 1900, 2100 then it must be divisible by 400.
print("Enter the year")
year = int(input())
if year%100 == 0:
    if year% 400== 0:
        print("It is a century year and leap year")
    else:
        print("It is not a century year")
else:
    if year%4 == 0:
        print("It is a leap year")
    else:
        print("Sorry it is not a leap year")