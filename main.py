# main.py
from  modules.Mat_utils import add, subtract, multiply, divide 

def calculator():
    print("Welcome to Modular Calculator!")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        operator = input("Choose an operator (+, -, *, /) or 'q' to quit: ").strip()

        if operator.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        try:
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Try again.")
                continue

            print(f"The result is: {result}\n")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()