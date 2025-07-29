def calc():
    operation = input("Enter your operation (+, -, *, /) : ")
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    if operation == "+":
        print("Addition is :", num1 + num2)
    elif operation == "-":
        print("Subtraction is :", num1 - num2)
    elif operation == "*":
        print("Multiplication is :", num1 * num2)
    elif operation == "/":
        print("Division is :", num1 / num2)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calc()
