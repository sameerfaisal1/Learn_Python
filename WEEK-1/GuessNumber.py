print("Welcome To Number Guessing Game!")

number = 7
total_Attempts = 5
while True:
    try:
        if(total_Attempts == 0):
            print("All Attempts are used \n \n")
            status = input("Want to Play Again y/n! \n")
            if(status == 'y' or status == 'Y'   ):
                total_Attempts = 5
                continue
            break

        input_number = int(input("Guess a number... "))
    
        if(input_number > number):
            total_Attempts -= 1
            print(f"Attempts Remaining: {total_Attempts}")
            print("Entered number is to high \n")
            continue

        if(input_number < number):
            total_Attempts -= 1
            print(f"Attempts Remaining: {total_Attempts}")
            print("Entered number is to low \n")
            continue

        else:
            total_Attempts -= 1
            print(f"Attempts Remaining: {total_Attempts}")
            print("You guessed the number correctly!\n")
            status = input("Want to Play Again y/n! \n")
            if(status == 'y' or status == 'Y'   ):
                total_Attempts = 5
                continue
            else:
                 break

    except ValueError:
        print("Please enter a valid number \n")
print("Game Ended!\n")

