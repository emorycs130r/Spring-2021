class ComplexNumber():

    def __init__(self, r=0, i=0):
        
        # real and imaginary are called attributes of a class
        self.real = r
        self.imaginary = i


def add_two_complex_nos(c_1, c_2):

    c_3 = ComplexNumber()

    c_3.real = c_1.real + c_2.real
    c_3.imaginary = c_1.imaginary + c_2.imaginary

    return c_3
    


if __name__ == "__main__":


    c_n = ComplexNumber(4, 5) # 4 + 5i
    print(c_n.real, c_n.imaginary)

    # 10 + 20i
    c_2 = ComplexNumber(10, 20)
    print(c_2.real, c_2.imaginary)

    result = add_two_complex_nos(c_n, c_2)
    print(f"The result is {result.real} + {result.imaginary}i")