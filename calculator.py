def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    """Main calculator function"""
    print("=" * 40)
    print("          Simple Calculator")
    print("=" * 40)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"\n{num1} × {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
            
            except ValueError:
                print("\nInvalid input! Please enter numeric values.")
        else:
            print("\nInvalid choice! Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    calculator()
