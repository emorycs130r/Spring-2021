def check_largest(a, b, c):

    if a > b:
        if a > c:
            print("a is greatest")
        elif a < c:
            print("c is greatest")
        else:
            print("a & c are greatest")
    elif b > a:
        if b > c:
            print("b is greatest")
        elif b < c:
            print("c is greatest")
        else:
            print("b & c are greatest")
    else:
        if a > c:
            print("a & b are greatest")
        elif c > a:
            print("c is greatest")
        else:
            print("All 3 are equal")
   

def check_largest_modified(a, b, c):

    if a >= b and a >= c:
        print("a is greatest")

    elif b >= a and b >=c:
        print("b is greatest")

    else:
        print("c is largest")

if __name__ == "__main__":

    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    check_largest(a, b, c)
