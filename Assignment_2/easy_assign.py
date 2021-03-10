
# import random

# def check_triangle_sides(a,b,c):
#     if (a+b)>c and (b+c)> a and (a+c) > b :
#         return "Sides are valid"
#     else :
#         return "Sides are not valid"

# def rectangle_calculations(length,width,choice):
#     if choice=='a':
#         area= length*width
#         return f"The area of rectangle is: {area}"
#     elif choice== 'p':
#         perimeter= 2*(length+width)
#         return f"The perimeter of rectangle is {perimeter}"
#     else:
#         return "Invalid choice!"

# def random_number_game(value):
#     ran= int(random.randint(1,100))
#     if ran==value:
#         return True
#     else :
#         return False


# if __name__ == "__main__" :
#     var1= input("Enter 1st side: ")
#     var2 = input("Enter 2nd side: ")
#     var3 = input("Enter 3rd side: ")
#     print(check_triangle_sides(var1,var2,var3))

#     l= float(input("enter length of rectangle: "))
#     w= float(input("enter width of rectangle:  "))
#     c = input("enter the choice: ")
#     print(rectangle_calculations(l,w,c))

#     val= int(input("enter any number: "))
#     print(random_number_game(val))
    


def check_traingle_sides(a,b,c):
    if a + b >= c and a + c >= b and b + c >= a:
        return True
    else:
        return False

if __name__ == "__main__":

    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))

    results = check_traingle_sides(a,b,c)

    if results == True:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")