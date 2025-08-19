#problem 05: Take two numbers and an operator(+,-,*,/)from the user. Perform the operation using conditional statements.

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
op=input("Enter operator (+,-,*,/): ")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("Invalid operator")
