
def print_matrix(matrix):
    
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


def check_r_c_equality(matrix_1, matrix_2):

    if (len(matrix_1) == len(matrix_2)) and (len(matrix_1[0]) == len(matrix_2[0])):
        return True
    else:
        return False


def adding_matrices(matrix_1, matrix_2):

    result_matrix = []
    
    for i in range(len(matrix_1)):
        temp_row = []
        for j in range(len(matrix_1[0])):
            temp_ = matrix_1[i][j] + matrix_2[i][j]
            temp_row.append(temp_)
        
        result_matrix.append(temp_row)
    
    return result_matrix


'''

Write a function to add 3 matrices.

'''


def add_3_matrices(matrix_1, matrix_2, matrix_3):

    result_matrix = []

    check_1 = check_r_c_equality(matrix_1, matrix_2)
    check_2 = check_r_c_equality(matrix_2, matrix_3)

    if check_1 and check_2:
    
        result_matrix = adding_matrices(matrix_1, matrix_2)
        result_matrix = adding_matrices(result_matrix, matrix_3)
    
    else:
        print("Incompatible matrix sizes")
        exit()

    return result_matrix

if __name__ == "__main__":

    matrix_a = [[1,2,3],
                [4,5,6],
                [7,8,9]
                ]
    
    matrix_b = [[1,3,5],
                [7,9,11],
                [13,15,17],
                [1,2,3]
                ]

    matrix_c = [[2,4,6],
                [8,10,12],
                [14,16,18]
                ]
    
    result = add_3_matrices(matrix_a, matrix_b, matrix_c)
    print_matrix(result)
    # check_ = check_r_c_equality(matrix_a, matrix_b)

    # if check_:
        
    #     print("First Matrix: ")
    #     print_matrix(matrix_a)

    #     print("Second Matrix: ")
    #     print_matrix(matrix_b)

    #     result = adding_matrices(matrix_a, matrix_b)

    #     print("Result Matrix: ")
    #     print_matrix(result)

    # else:
    #     print("Incompatible matrix dimension")