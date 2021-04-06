import csv
import random

def create_csv(file_name):

    csv_fd = open(file_name, 'w')
    csv_write = csv.writer(csv_fd)
    for i in range(100):
        csv_list = [random.randint(1,100) for i in range(5)]
        '''
        csv_list = []
        for i in range(5):
            csv_list.append(random.randint(1,100))
        '''
        # csv_write.writerow(csv_list)
        csv_write.writerow(csv_list)
    csv_fd.close()

if __name__ == "__main__":

    create_csv('example.csv')