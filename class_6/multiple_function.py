import math

def power_2(variable_1):

    return math.pow(variable_1, 2)

# (a + b)^2 = a^2 + b^2 + 2ab

def check_a_plus_b(a, b):

    lhs = power_2(a + b)
    rhs = power_2(a) + power_2(b) + 2 * a * b

    return lhs == rhs

if __name__ == "__main__":
    a = int(input("Enter first_variable: "))
    b = int(input("Enter second variable: "))

    result = check_a_plus_b(a,b)
    if result:
        print("Wow maths is beatiful!")
    else:
        print("Who do they think they are?")
