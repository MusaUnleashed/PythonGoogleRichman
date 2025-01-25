total_sum = 0

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break  # Exit the loop if input is empty
    try:
        number = float(user_input)
        total_sum += number  # Add the number to the total sum
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print(f"The sum of all entered numbers is: {total_sum}")
