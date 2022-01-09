age = int(input())
if 7<age<18:
    print("Not eligible")
elif age == 18:
    print("Make leaner license")
elif 18<age<100:
    print("Eligible")
else:
    print("Invalid input")
