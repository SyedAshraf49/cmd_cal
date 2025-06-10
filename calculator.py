def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"
def power(a, b): return a ** b

while True:
    print("\n--- Simple Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Exit")

    choice = input("Choose an operation: ")

    if choice == '6':
        print("Goodbye!")
        break

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice.")
        continue

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    operations = {'1': add, '2': subtract, '3': multiply, '4': divide, '5': power}
    result = operations[choice](x, y)
    print(f"Result: {result}")
