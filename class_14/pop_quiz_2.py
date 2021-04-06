'''

Write a function with input file, output file, and a value. Copy all the values
less than the value into the output file.  

'''


def get_numbers_lower(input_list, value):

    temp_list = []

    for val in input_list:
        if int(val) < value:
            temp_list.append(val)
    
    return temp_list

def copy_file_lower(file_1, file_2, value):

    ip_fd = open(file_1, 'r')
    op_fd = open(file_2, 'w')

    ip_lines = ip_fd.readlines()
    
    lower_values = get_numbers_lower(ip_lines, value)

    op_fd.writelines(lower_values)
    # for line in ip_lines:
    #     if int(line) < value:
    #         string = f"{line}"
    #         op_fd.write(string)
    
    ip_fd.close()
    op_fd.close()


if __name__ == "__main__":
    copy_file_lower('numbers.txt', 'numbers_2_copy.txt', 50)