def add(a, b):
    return a + b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a / b

def subtract (a, b):
    return a - b

def power(a, b):

    return a**b

if __name__ == "__main__":
    
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == "+":
        variable_1 = float(input("Enter first value: "))
        variable_2 = float(input("Enter second value: "))
        result = add(variable_1, variable_2)
        print(f"The result is: {result}")

    elif operation == "-":
        variable_1 = float(input("Enter first value: "))
        variable_2 = float(input("Enter second value: "))
        result = subtract(variable_1, variable_2)
        print(f"The result is: {result}")

    elif operation == "*":
        variable_1 = float(input("Enter first value: "))
        variable_2 = float(input("Enter second value: "))
        result = multiply(variable_1, variable_2)
        print(f"The result is: {result}")

    elif operation == "/":
        variable_1 = float(input("Enter first value: "))
        variable_2 = float(input("Enter second value: "))
        result = add(variable_1, variable_2)
        print(f"The result is: {result}")

    elif operation == "^":
        variable_1 = float(input("Enter first value: "))
        variable_2 = float(input("Enter second value: "))
        result = power(variable_1, variable_2)
        print(f"The result is: {result}")

    else:
        print("Operation not supported")