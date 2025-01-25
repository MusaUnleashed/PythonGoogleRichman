player1_number = int(input("Player 1, enter a secret number between 1 and 100: "))
print("\n" * 100)

while True:
    player2_guess = int(input("Player 2, guess the number: "))

    if player2_guess == player1_number:
        print("Correct! You win!")
        break
    elif player2_guess > player1_number:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
