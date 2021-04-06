'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
'''

reader = open('dog_breeds.txt', 'r')

print(reader)
contents = reader.readlines()
for line in contents:
    print(line, type(line))

reader.close()