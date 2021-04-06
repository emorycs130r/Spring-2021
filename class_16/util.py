import csv
import random

def read_csv():

    csv_fd = open('zillow.csv', 'r')
    csv_reader = csv.reader(csv_fd)
    for row in csv_reader:
        print(row)
    
    csv_fd.close()
    csv_fd = open('zillow.csv', 'r')
    complete_values = csv.DictReader(csv_fd)

    for row in complete_values:
        print(row)

def create_csv():

    csv_fd = open('sample.csv', 'w')
    csv_write = csv.writer(csv_fd)
    for i in range(100):
        csv_list = [random.randint(1,100) for i in range(5)]
        csv_write.writerow(csv_list)
    csv_fd.close()

if __name__ == "__main__":
    # read_csv()
    create_csv()