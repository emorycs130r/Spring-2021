import random

def check_input(player_1):

    '''
     0 -> r
     1 -> p
     2 -> s
    
    '''
    value = random.randint(0,3)


    if player_1 == 'r':
        
        if value == 0:
            return None
        elif value == 1:
            return False
        else:
            return True
     
    elif player_1 == 'p':
        if value == 1:
            return None
        elif value == 0:
            return True
        else:
            return False
    
    elif player_1 == 's':
        if value == 2:
            return None
        elif value == 0:
            return False
        else:
            return True
    
    else:
        return "Wrong Input"

if __name__ == "__main__":

    
    player_1_score = 0
    computer_score = 0
    while True:
        
        player_1 = input("Enter your choice: (r/s/p) ")
        result = check_input(player_1)
        
        if result == True:
            print("You won")
            player_1_score = player_1_score + 1
        elif result == False:
            print("You lost")
            computer_score = computer_score + 1
        elif result == None:
            print("Tie")
        else:
            print("Wrong Input")
        

        if player_1_score == 5:
            print("Player 1 won")
            break
        
        if computer_score == 5:
            print("Computer won")
            break