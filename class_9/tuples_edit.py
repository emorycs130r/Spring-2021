eg_tuple = (10, 40, 50, 100, 200, 300)

print(eg_tuple)
print(type(eg_tuple))

eg_tuple = list(eg_tuple)

print(type(eg_tuple))

eg_tuple[0] = -100

eg_tuple = tuple(eg_tuple)

print(eg_tuple)
