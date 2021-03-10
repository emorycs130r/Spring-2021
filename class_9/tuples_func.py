
def print_tuple(superman):
    
    print(type(superman))

    for i in superman:
        print(i, end=" ")
    
    superman[1] = 50
    print(superman)
    print("")


def edit_list(list_1):

    list_1[2] = 10


def eg():
    list_eg = (10, 20, 30, 40)
    edit_list(list_eg)
    print(list_eg)


if __name__ == "__main__":
    
    # tuple_ = [10, 20, 30]

    # # tuple_ = "Hello World"
    # print_tuple(tuple_)

    eg()
    