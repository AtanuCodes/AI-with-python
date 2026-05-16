# Sum & Average Calculator
# Write a program that keeps asking the user to enter numbers.

# Use a while loop
# Stop when the user enters 0
# After stopping, print:
# How many numbers were entered
# The total sum of all numbers
# The average of all numbers

count = 0
total_sum = 0

while True:
    try:
        number = int(input('Enter a number (0 to stop): '))
        if number == 0:
            break
        elif number < 0:
            print(f"Please enter a valid positive number!")
            continue
       
    except ValueError:
        print(f'please enter a valid num!')
        continue


    # Update count and sum with the entered number
    count += 1
    total_sum += number

print(    f'\nTotal count: {count}'
          f'\nTotal sum: {total_sum}'
          f'\nAverage: {total_sum / count if count > 0 else 0}')