# Simple Calculator

def calculator():
    print("Simple Calculator")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("\nOperations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    operation = input("\nChoose operation (1/2/3/4): ")
    
    if operation == '1':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nError: Cannot divide by zero!")
    else:
        print("\nInvalid operation!")

if __name__ == "__main__":
    calculator()
