import random

def create_list(n):

    # n = 10
    list_ = []
    for i in range(n):
        list_.append(random.randint(1, 1000))
    
    return list_


def print_list(list_):
    print(f"The list is: {list_}")
    print("The list is: ", end=" ")
    for i in list_:
        print(i, end="->")
    print("")


def find_product(list_):
    
    # Product of the numbers in the list. 
    product = 1
    for i in list_:
        product = product * i

    return product

if __name__ == "__main__":

    eg_list = create_list(10)
    print_list(eg_list)

    result = find_product(eg_list)
    print(f'The product is {result}.')

