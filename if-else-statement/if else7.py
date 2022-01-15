#Take input of age of 3 people by user and determine oldest and youngest among them.
print("First age")
a1 = input()
print("Second age")
a2 = input()
print("Third age")
a3 = input()
if a1>a2 and a1>a3:
    print("oldest is",a1)
elif a2>a1 and a2>a3:
    print("Oldest is",a2)
elif a3>a1 and a3>a2:
    print("Oldest is",a3)
else:
    print("All are equal")