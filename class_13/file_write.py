# writer = open('write_file.txt', 'a')
# var_1 = "Line 3 is this\n"
# var_2 = "Line 4 is this\n"
# writer.write(var_1)
# writer.write(var_2)
# writer.close()


writer = open('bulk_write.txt', 'w')
lines = ['Hello World\n', 'Line 2\n', str(25), '\nThis is great\n']
writer.writelines(lines)