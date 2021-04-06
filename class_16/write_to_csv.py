'''

Write a function that takes in a file name, and threshold value. 
It stores the numbers greater than threshold value from each row into a new file. 

'''
import csv

def get_values_greater(file_name, threshold):
    

    csv_fd = open(file_name, 'r')
    csv_reader = csv.reader(csv_fd)
    int_row_list = []
    for row in csv_reader:
        temp_row = [int(r) for r in row if int(r) > threshold]
        int_row_list.append(temp_row)
    
    print(int_row_list)

    csv_w_fd = open('threshold.csv', 'w')
    csv_writer = csv.writer(csv_w_fd)
    csv_writer.writerows(int_row_list)

    csv_fd.close()
    csv_w_fd.close()

'''

Get mean, median and mode for each row, and write it into a new file. 


'''

import statistics

def calc_three_values(file_name):
    csv_fd = open(file_name, 'r')
    csv_reader = csv.reader(csv_fd)
    int_row_list = []
    for row in csv_reader:
        temp_row = [int(r) for r in row]
        mean = statistics.mean(temp_row)
        median = statistics.median(temp_row)
        mode = statistics.mode(temp_row)
        int_row_list.append([mean, median, mode])
    print(int_row_list)


if __name__ == "__main__":
    # get_values_greater('sample.csv', 20)
    calc_three_values('sample.csv')