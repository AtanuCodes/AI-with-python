# Write a program that asks the user to enter a number (integer).
# Then print:

# Whether the number is Positive, Negative, or Zero
# Whether it is Even or Odd
# Bonus: If the number is positive and even, also print "This is a nice even number!"
# Handle invalid input gracefully (show a message if not a number)

user_input = input("Please enter an integer: ")

if not user_input.isdigit():
    print("Invalid input. Please enter a valid integer.")
else:
    user_input = int(user_input)
    if user_input > 0:
        print("The number is positive.")
    elif user_input < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

if user_input > 0 and user_input % 2 == 0:
    print("This is a nice even number!")
