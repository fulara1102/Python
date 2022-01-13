"""
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
"""
print("Enter quantity")
q = int(input())
if q>1000 or q ==1000:
    print("Discount is",.10*q*100)
    print("Total bill is",q*100-.10*100*q)
else:
    print("Total bill is ",q*100)