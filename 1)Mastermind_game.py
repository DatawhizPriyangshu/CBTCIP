
#  Task 1 : MasterMind game  


def get_hints(secret_no, guess_no):

    hints = []
    secret_str = str(secret_no)
    guess_str = str(guess_no)
    
    for i in range(4):

        if guess_str[i] == secret_str[i]:
            hints.append(guess_str[i])
        elif guess_str[i] in secret_str:
            hints.append('*')
        else:
            hints.append('X')
    
    return hints

def get_valid_input(prompt):

    while True:
        user_input = input(prompt)
        if user_input.isdigit() and len(user_input) == 4:
            return int(user_input)
        else:
            print("Please enter a 4-digit number.")

def play_game(set_player, guess_player):

    secret_number = get_valid_input(f"{set_player}, enter a 4-digit secret number: ")
    attempts = 0

    print(f"{set_player} sets a multidigit number: {secret_number}\n")
    
    while True:

        guess_number = get_valid_input(f"{guess_player}, make a guess. The number is of 4 digits: ")
        attempts += 1

        hints = get_hints(secret_number, guess_number)
        
        print(f"{set_player}, Hint: {' '.join(hints)}")
        print(f"attempt: {attempts}")

        if guess_number == secret_number:
            print(f"{guess_player} guessed it correct in {attempts} attempt(s).")
            break

    return attempts


def main():

    print("---------------------------------------------------------")
    print("Welcome to Mastermind!. Here are the rules : ")
    print("Player 1 sets a 4-digit secert number. Player 2 tries to guess  and vice versa")
    print("The player who guess in less attempts wins the game and crowned Mastermind")
    print("If a digit matches and is in the correct position, it is displayed.")
    print("If a digit is correct but in the wrong position, it is displayed with an '*' ")
    print("If a digit is not in the number, it is displayed as 'X'.")
    print("Let's begin the game !")
    print("---------------------------------------------------------\n")

    player2_attempts = play_game("Player 1", "Player 2")

    print("\n---------------------------------------------------------\n")
    
    player1_attempts = play_game("Player 2", "Player 1")

    if player1_attempts < player2_attempts:
        print("Player 1 is crowned Mastermind!")
    elif player1_attempts > player2_attempts:
        print("Player 2 is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
