num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 + num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("Error invalid operation", operation)

print(result)