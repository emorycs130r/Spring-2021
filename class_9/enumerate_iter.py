

def enumerate_(list_1):
    
    for idx, value in enumerate(list_1):
        print(f" Iteration: {idx}, {value}")


def return_multiple():
    
    str_ = "Hello World"
    int_ = 90
    list_ = [10, 30, 40]
    return str_, int_, list_


if __name__ == "__main__":
    
    # list_ = [20, 30, 40, 50, 60, 70, 80]
    # enumerate_(list_)

    returned_values_1, returned_values_2 = return_multiple()
    print(returned_values_1, returned_values_2, returned_values_3)