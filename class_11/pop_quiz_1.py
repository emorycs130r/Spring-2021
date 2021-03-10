'''

Create a dictionary from the following list of students with grade: 

bob - A
alice - B+
luke - B
eric - C

Get input of name from user using the "input()" and use it to display grade. If the name isn't present, display "Student not found"


'''
def working_numbers_set(input_list):
    return list(dict.fromkeys(input_list))

if __name__ == "__main__":
    input_list = [2,2,3,5,6,8,7,6,2]
    result = working_numbers_set(input_list)
    print(result)