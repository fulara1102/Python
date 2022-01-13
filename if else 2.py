#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#ask user for their salary and year of service and print the net bonus amount.
print("Enter salary")
salary = int(input())
print("year of service")
yos = int(input())
if yos > 5:
    print("Bonus",.5*salary)
else:
    print("Have a great days ahead")