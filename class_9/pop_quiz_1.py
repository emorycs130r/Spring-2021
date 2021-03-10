'''
Get a tuple and list as input for a function. Sizes of both must be same. 
Compare the values in the two, and return a third list with highest of two numbers. 

For eg:

tuple_1 = [10, 20, 30, 40]
list_1 = [20, 4, 6, 50]

returned_list = [20, 20, 30, 50]
'''

def compare_values(tuple_1, list_1):

    if len(tuple_1) != len(list_1):
        print("Incorrect length of inputs")
        exit()

    return_list = []

    for i in range(len(tuple_1)):
        # print(f"List value: {l} -- Tuple Value: {t}")
        if list_1[i] < tuple_1[i]:
            list_1[i] = tuple_1[i]
        elif list_1[i] < tuple_1[i]:
            return_list.append(tuple_1[i])
        else:
            return_list.append(tuple_1[i])

    return return_list        


# if __name__ == "__main__":

list_1 = [10, 20, 30, 40]
tuple_1 = (20, 4, 6, 50)
compare_values(list_1, tuple_1)
print(list_1)