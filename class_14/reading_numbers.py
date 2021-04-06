
def read_numbers(file_name):

    ip_fd = open(file_name, 'r')
    values = ip_fd.readlines()
    return [int(x) for x in values], values

if __name__ == "__main__":

    nos, nos_str = read_numbers('numbers.txt')
    print(type(nos[0]), type(nos_str[0]))