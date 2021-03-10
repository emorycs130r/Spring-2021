def print_matrix(matrix):
    
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

def add_const_matrix(matrix, constant):
    
    row_num = len(matrix)
    column_num = len(matrix[0])

    for i in range(row_num):
        for j in range(column_num):

            matrix[i][j] = matrix[i][j] * constant
    
    return matrix
            



if __name__ == "__main__":

    matrix_a = [[1,2,3],
                [4,5,6],
                [7,8,9]
                ]
    
    print("Before addition: ")
    print_matrix(matrix_a)

    modified_matrix = add_const_matrix(matrix_a, 5)

    print("After addition:")
    print_matrix(modified_matrix)