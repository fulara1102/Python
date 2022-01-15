"""A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade."""
print("Enter name")
name = input()
print("Enter total number")
grade = int(input())
if grade < 25:
    print("Grade = F")
elif 25 > grade > 45:
    print("Grade = E")
elif 45 > grade > 50:
    print("Grade = D")
elif 50 > grade > 60:
    print("Grade = C")
elif 60 > grade > 80:
    print("Grade = B")
elif 80>grade>=100:
    print("Grade = A")
else:
    print("Invalid input!")