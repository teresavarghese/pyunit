"""
Calculator Module
"""

def add(number1, number2):
    """
    Returns the sum of number1 and number2
    """
    return number1 + number2

def subtract(number1, number2):
    """
    Returns the difference between number1 and number2
    """
    return number1 - number2

def multiply(number1, number2):
    """
    Returns the product of number1 and number2
    """
    return number1 * number2

def divide(number1, number2):
    """
    Returns the division result of number1 by number2
    """
    if number2 != 0:
        return number1 / number2
    return "Cannot divide by zero"

def main():
    """
    Main function to run the calculator
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
