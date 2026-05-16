# 1. Multiplication Table Generator
# Task:
# Ask the user to enter a positive integer (example: 7).
# Then use a for loop to print the multiplication table from 1 to 12:
# text7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 12 = 84
# Bonus:

# Add input validation (if user enters negative or not a number, ask again)
# Let the user also choose how many rows they want (instead of fixed 12)

while True:
    try:
        number = int(input('Enter a positive integer: '))
        if number <= 0:
            print(f"Please enter a valid positive number!")
            continue
        break
    except ValueError:
        print(f'please enter a valid num!')

while True:
    try:
        rows = int(input('How many rows you want?'))
        if rows <= 0:
            print(f"Please enter a valid positive number!")
            continue
        break
    except ValueError:
        print(f'please enter a Positive row num!')

for multiplyer in range(1, rows + 1):
    product = number * multiplyer
    print(f'{number} * {multiplyer} = {product}')
    

        