'''

Step 1: Write 2 functions that converts celsius to farenheit, celsius to kelvin. 
Step 2: Get an input from user for the celsius value, and f/k for the value to convert it to. 
Step 3: Based on the input call the right function. 

'''

def c_to_f(temp):
    return (9/5) * temp + 32

def c_to_k(temp):
    return temp + 273.15

if __name__ == "__main__":
    function = input("Which conversion? (F or K) ")
    temp = float(input("Enter a temperature in Celsius: "))

    if function == "F" or function == "f":
        print(c_to_f(temp))
    elif function == "K" or function == "k":
        print(c_to_k(temp))
    else:
        print("Invalid conversion")