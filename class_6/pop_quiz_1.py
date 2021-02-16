'''

You're on a spaceship, and all of a sudden you start hearing a buzzing sound. You figure it is because
of the CPU, and now need to write a script to check it. 

Step 1: Write a function to check CPU Utilisation if above 90. If yes, return True, else return False. 
Step 2: Get input from a user, in float. 
Step 3: Call the function with the user input, and store result in variable. 
Step 4: If result is true, print, "All good". Otherwise, print "Houston, we have a problem"


'''

def check_cpu(curr_util):
    
    if float(curr_util) > 90:
        # result = 'All good.'
        return True

    else:
        # result = 'Houston, we have a problem.'
        return False


if __name__ == "__main__":
    var_1 = input('What is the current utilisation value? ')
    result = check_cpu(var_1)
    if result:
        print("All good!")
    else:
        print("Houston, we have a problem.")
    
