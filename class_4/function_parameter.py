def second_function(parameter_1):

    print(f"Value & Type of parameter 1 is: {parameter_1} {type(parameter_1)}")
    if parameter_1 == 10:
        print("Correct value")

second_function(10) # --> 10 is called passing a value to the function .
second_function("Hello World") # --> "Hello World"
second_function(89.7777)