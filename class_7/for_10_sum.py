# Add the first 10 numbers, and the first 10 even numbers using for loops
if __name__ == "__main__":
    sum = 0
    for i in range(0,11):
        sum = sum + i
    print(f"The sum of the first 10 Natural Nos. is {sum}")

    sum = 0
    for i in range(2,21,2):
        sum = sum + i
    print(f"The sum of the first 10 even nos. is {sum}")