fruits = ['Apple', 'Strawberry', 'Orange']

# Index = Position - 1

# print(fruits[3])

print(type(fruits))

vegetables = []
print(f"Before adding value: {vegetables}")
vegetables.append('Brocolli')

print(f"After adding value: {vegetables}")
# print(vegetables)

fruits.append('Kiwi')

print(f"Fruits are: {fruits}")

fruits.insert(2, 'Raspberry')

print(f"Updated fruit list: {fruits}")

fruits.remove('Apple')

print(f"Updated fruit list 2: {fruits}")