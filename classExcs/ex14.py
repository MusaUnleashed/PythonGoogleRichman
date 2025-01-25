print("Choose a secret number between 1 and 100, but don't tell the computer!")

low = 1
high = 100
guesses = 0

while True:
    guess = (low + high) // 2
    guesses += 1
    print(f"Is your number < {guess}? (y/n)")

    feedback = input().lower()

    if feedback == "y":
        print(f"The computer guessed your number in {guesses} tries!")
        break
    else:
        print(f"Is my guess higher than your number? (y/n)")
        feedback = input().lower()

        if feedback == "y":
            high = guess - 1
        else:
            low = guess + 1
