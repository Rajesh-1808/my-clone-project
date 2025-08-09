# calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
    print(f"The result is: {add(a, b)}")
elif choice == '2':
    print(f"The result is: {subtract(a, b)}")
elif choice == '3':
    print(f"The result is: {multiply(a, b)}")
elif choice == '4':
    print(f"The result is: {divide(a, b)}")
else:
    print("Invalid input.")