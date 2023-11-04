def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

is_good = True

while is_good:
    if is_good:
        num1 = float(input("Enter the first number: "))
    else:
        num1 = answer  # Use the previous answer as the new num1

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operation_symbol in operations:
        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    else:
        print("Invalid operation symbol. Please choose +, -, *, or /.")

    if input("Do you want to continue (y/n)? ") != "y":
        is_good = False




