'''
* Create a function, that takes 2 file names as input, and copies contents from one file to another. 
'''

def copy_files(ip_file, op_file):
    
    ip_fd = open(ip_file, 'r')
    op_fd = open(op_file, 'a')

    ip_lines = ip_fd.readlines()
    ip_fd.close()
    op_fd.writelines(ip_lines)
    op_fd.close()


if __name__ == "__main__":
    copy_files('file_1.txt', 'file_1_copy.txt')

