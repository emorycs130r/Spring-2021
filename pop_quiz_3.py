# x^3 + log(y)
import math

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

result = math.log(y, 10) + math.pow(x,3)

print(f"The result is {result}")