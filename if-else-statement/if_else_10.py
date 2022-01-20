"""Ask user to enter age, sex ( M or F ), marital status ( Y or N )
and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR"."""
print("Enter your age")
age = int(input())
print("Enter your sex(M or F)")
sex = input()
#print("Enter marital status(Y or N)")
#marital = input()
if sex == "F" or 20 > age > 40:
    print("she will work only in urban areas.")
elif sex == "M" or 20 > age > 40:
    print("He may work in anywhere")
elif sex == "M" or 40 > age > 60:
    print("he will  work in uaban areas only ")
else:
    print("ERROR!!")