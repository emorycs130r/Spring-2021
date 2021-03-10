array_2d = [[1,2,3], [4,5,6], [7,8,9,15], [10, 11, 12]]

num_rows = len(array_2d)
num_colums = len(array_2d[0])

for i in range(num_rows):
    for j in range(num_colums):
        print(array_2d[i][j], end=" ")
    print()

print("=================")

for row_ in array_2d: # row_ will have each row's content
    # print(row_)
    for elem in row_:
        print(elem, end=" ")
    print()


value = [[]]
