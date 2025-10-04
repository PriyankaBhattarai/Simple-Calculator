# Simple Calculator

N1 = float(input("Enter first number: ")) # Input first number as float.
N2 = float(input("Enter second number: ")) # Input second number as float.
op = input("Enter operator (+, -, *, /, %): ") # Input op is (operator).
if op == '+':
    print(f"The sum of this number is: {N1 + N2}") # Perform addition and print the result.
elif op == '-':
    print(f"The subtraction of this number is : {N1 - N2}") # Perform subtraction and print the result.
elif op == '*':
    print(f"The multiplication of this number is: {N1 * N2}") # Perform multiplication and print the result.
elif op == '/':
    if N2 != 0:
        print(f"The division of this number is: {N1 / N2}") # Perform division and print the result.
    else:
        print("Error: Division by zero") # Handle division by zero error.
elif op == '%':
    if N2 != 0:
        print(f"The modulus of this number is: {N1 % N2}") # Perform modulus and print the result.
    else:
        print("Error: Modulus by zero") # Handle Modulus by zero error.
else:
    print(f"It will give an Invalid operator: {op}") # Handle invalid operator error.


