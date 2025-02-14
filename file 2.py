# Get input for two numbers
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

# Get input for operation
operation = input("Enter operation (add/sub/mul/div): ").lower()

# Perform the operation
if operation == "add":
    result = a + b
    print(f"Result: {result}")
elif operation == "sub":
    result = a - b
    print(f"Result: {result}")
elif operation == "mul":
    result = a * b
    print(f"Result: {result}")
elif operation == "div":
    if b != 0:
        result = a / b
        print(f"Result: {result}")
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")
