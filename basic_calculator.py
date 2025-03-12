# Step 1: Get user inputs data  
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

# Step 2: Format numbers for display (convert to int if whole number)
display_num1 = int(num1) if num1.is_integer() else num1
display_num2 = int(num2) if num2.is_integer() else num2

# Step 3: Perform the operation and handle division by zero
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    result = num1 / num2


# Step 4: Format the result for display
display_result = int(result) if result.is_integer() else result
