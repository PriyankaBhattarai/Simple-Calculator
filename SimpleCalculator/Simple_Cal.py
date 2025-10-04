# Simple Calculator

N1 = float(input("Enter first number: ")) # Input first number as float.
N2 = float(input("Enter second number: ")) # Input second number as float.
op = input("Enter operator (+, -, *, /, %): ") # Input op is (operator).
if op == '+':
    print(N1 + N2) # Perform addition and print the result.
elif op == '-':
    print(N1 - N2) # Perform subtraction and print the result.
elif op == '*':
    print(N1 * N2) # Perform multiplication and print the result.
elif op == '/':
    if N2 != 0:
        print(N1 / N2) # Perform division and print the result.
    else:
        print("Error: Division by zero") # Handle division by zero error.
elif op == '%':
    if N2 != 0:
        print(N1 % N2) # Perform modulus and print the result.
    else:
        print("Error: Modulus by zero") # Handle division by zero error.
else:
    print("Invalid operator")   


