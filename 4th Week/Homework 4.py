print("Enter a number")
a = int(input())
if ((a%2)==0):
 print("A is divisible by 2")
else:
 print("A is not divisible by 2")

 print("Enter the dragon")
 b = int(input())
if ((a%6)==0):
  print("B is divisible by 6")
else:
 print("B is not divisible by 6")

x = str(input("Enter a number"))
y = str(input("Enter the number you want to search"))
result = x.find(y)
if (result)!=(-1):
 print("Number is present at location:", result)
else:
 print("Number is not present")