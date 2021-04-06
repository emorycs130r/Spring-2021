import random

def create_file():

    op_fd = open('file_1.txt', 'w')
    op_fd.write("Sixth World\n")
    op_fd.write("Seventh Line\n")
    op_fd.write("Eigth Line\n")
    op_fd.write("Ninth Line\n")
    op_fd.write("Tenth Line\n")

    op_fd.close()

def create_numbers_file(file_name):

    op_fd = open(file_name, 'w')
    for i in range(100):
        op_fd.write(str(random.randint(1,100)))
        op_fd.write('\n')


def create_csv(file_name):

    file_fd = open(file_name, 'w')

    for i in range(500):
        val_1 = random.randint(1, 100)
        val_2 = random.randint(1, 1000)
        val_3 = random.randint(1, 340)
        write_string = f"{val_1}-{val_2}-{val_3}\n"
        file_fd.write(write_string)

    file_fd.close()
    
if __name__ == "__main__":
    # create_file()
    # create_numbers_file('numbers.txt')
    create_csv('products_hyphen.csv')