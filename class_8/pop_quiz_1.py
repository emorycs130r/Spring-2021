# Write a function that takes a list of integers as an input, and creates a new list with all the numbers divisible by 6. 

def check_divisible_by_6(eg_list):

    new_list = []
    for value in eg_list:
        print(value)
        if value % 6 == 0:
            new_list.append(value)

    return new_list

if __name__ == "__main__":

    list_ = [5, 6, 7, 10, 18, 78]
    new_ = check_divisible_by_6(list_)
    print(new_) 