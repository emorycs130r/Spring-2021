
def split_csv(file_name):

    ip_fd = open(file_name, 'r')
    values = ip_fd.readlines()
    for val in values:
        if val:
            print(val.split("-"))

    ip_fd.close()


if __name__ == "__main__":
    split_csv('products_hyphen.csv')