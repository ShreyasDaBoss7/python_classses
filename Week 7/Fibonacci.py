s = "hello"
print(s.capitalize())
print(s.lower())
print(s.upper())

num_list = (-6, 5, 3, 8, 4, 2, 5, 40)
b = sum(num_list)
print (b)

c = len(num_list)
print (c)

n = input("Enter Number to calculate sum")
n = int (n)
average = 0
sum = 0
for num in range(0,n+1,1):
    sum = sum+num
print("Sum of first", n, "numbers is: ", sum )

a = int(input("Enter the first number of the Fibonacci Series"))
b = int(input("Enter the second number of the Fibonacci Series"))
n = int(input("Enter the number of terms needed"))
print(a, b, end = " ")
while(n-2):
    c = a+b
    a = b
    b = c
    print(c, end = " ")
    n = n-1

