
def print_matrix(array_2d):
    for row_ in array_2d: # row_ will have each row's content
    # print(row_)
        for elem in row_:
            print(elem, end=" ")
        print()

def create_square_matrix(size_):
    
    matrix = []
    for i in range(size_):
        temp_row = []
        for j in range(size_):
            temp_row.append(0)
        matrix.append(temp_row)
    
    return matrix


def create_identity_matrix(size_):
    
    matrix = []
    for i in range(size_):
        temp_row = []
        for j in range(size_):
            if i == j:
                temp_row.append(1)
            else:
                temp_row.append(0)
        matrix.append(temp_row)
    
    return matrix

'''
Write a function to create a matrix with different row and column size. 
'''

def create_matrix(row_size, column_size):

    matrix = []

    for i in range(row_size):
        temp_row = []
        for j in range(column_size):
            temp_row.append(0)
        matrix.append(temp_row)
    
    return matrix

if __name__ == "__main__":
    
    # mat = create_square_matrix(5)
    # print(mat)

    # matx_ = create_matrix(3, 4)
    # print(matx_)

    id_mat = create_identity_matrix(5)
    print_matrix(id_mat)