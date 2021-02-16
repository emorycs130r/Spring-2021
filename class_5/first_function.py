def function(input_1, input_2, input_3, input_4):
 
    result = input_1 * input_2 * input_3 * input_4

    print(f"The four numbers multipled is: {int(result)}")


def multiply_g(pi=3.14, g_value, input_value=9.8):
    return input_value * g_value * pi


if __name__ == "__main__":
    input_1 = float(input("First float: "))
    input_2 = float(input("Second float: "))
    input_3 = int(input("First integer: "))
    input_4 = int(input("Second integer: "))
    
    function(input_1, input_2, input_3, input_4)

