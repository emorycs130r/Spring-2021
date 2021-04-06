import csv

def read_csv(file_name):
    # Count the number of lines in csv file

    csv_fd = open(file_name, 'r')
    csv_reader = csv.reader(csv_fd)
    print(csv_reader)
    count = 0
    for row in csv_reader:
        print(row)
        count = count + 1
    
    return count

def convert_str_to_int(file_name):
    csv_fd = open(file_name, 'r')
    csv_reader = csv.reader(csv_fd)

    result_list = []
    for row in csv_reader:  # Iterating over all the rows in csv
        temp_list = [int(x) for x in row] # Converting the string to integer 
        result_list.append(temp_list) # Appending to a new list. 
    
    return result_list # Returns the new list

def get_row_sum(rows):

    # Returns a list with each index having the sum of a particular row. 
    temp_list = []
    for row in rows:
        temp_list.append(sum(row))
    
    return temp_list


if __name__ == "__main__":

    # result = read_csv('sample.csv') 
    # print(f"The number of lines in the file are: {result}")

    result_l = convert_str_to_int('sample.csv')
    sum_of_rows = get_row_sum(result_l)
    print(sum_of_rows)