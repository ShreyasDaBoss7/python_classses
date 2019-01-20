x = str(input("Enter a number"))
y = str(input("Enter the number you want to search"))
result = x.find(y)
if (result)!=(-1):
 print("Number is present at location:", result)
else:
 print("Number is not present")