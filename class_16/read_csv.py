import csv

def read_csv(file_name):
    
    csv_fd = open(file_name, 'r')
    csv_reader = csv.DictReader(csv_fd)
    
    temp_list = set()
    for row in csv_reader:
        # row['block'] = int(row['block']) # --> row[0] == int(row[0])
        # row['timestamp'] = int(row['timestamp'])
        temp_list.add(row['block'])
        # print(row)
    
    return len(temp_list)


def split_read_requests(file_name):
    csv_fd = open(file_name, 'r')
    csv_reader = csv.DictReader(csv_fd)

    read_list = []
    for row in csv_reader:
        if row['read_write'] == 'r':
            read_list.append(row)
    
    print(read_list)
    csv_fd.close()
    csv1_fd = open('read_values.csv', 'w')
    keys = list(read_list[0].keys()) # --> To get the headers from the csv file.
    csv_writer = csv.DictWriter(csv1_fd, fieldnames=keys)
    csv_writer.writeheader()
    csv_writer.writerows(read_list)



# Write a function to get a count of the number of unique blocks in the file. 


# Write a function to move all the rows which happened after a particular timestamp
def move_rows(file_name, timestamp):
    csv_fd = open(file_name, 'r')
    csv_reader = csv.DictReader(csv_fd)

    read_list = []
    for row in csv_reader:
        if int(row['timestamp']) > int(timestamp):
            read_list.append(row)
    
    print(read_list)
    csv_fd.close()
    csv1_fd = open('new_rows.csv', 'w')
    keys = list(read_list[0].keys()) # --> To get the headers from the csv file.
    csv_writer = csv.DictWriter(csv1_fd, fieldnames=keys)
    csv_writer.writeheader()
    csv_writer.writerows(read_list)


if __name__ == "__main__":
    

    # result = read_csv('values.csv')
    # print(f"The number of unique blocks are {result}")

    # split_read_requests('values.csv')
    move_rows('values.csv', '1858836242064')