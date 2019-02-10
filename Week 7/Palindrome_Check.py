def reverse(s):
 if len(s) == 0:
  return s
 else:
  return reverse(s[1:]) + s[0]

s = str(input("Enter a word "))

print("The original string  is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")

rs=(reverse(s))
print("i am here ",rs)
if(s==rs):
 print(s," is a palindrome")
else:
 print(s," is not a palindrome")