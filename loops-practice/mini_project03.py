# 3. Number Pattern Printer
# Task:
# Ask the user for a number n (e.g. 5), then print the following patterns using loops:
# Pattern 1 (using for loop):
# text1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Pattern 2 (using for loop):
# text*****
# ****
# ***
# **
# *
# You can do both patterns in one program.

while True:
    try:
        n= int(input('Please enter a positive integer:'))
        if n < 0:
           print(f'please enter positive num')
           continue
        else :
            break
    except ValueError:
        print(f'enter value error!')

print(f'First pattern:')
for i in range(1, n+1):
    print(f'The number pattern : {list(range(1, i+1))}')

print(f'---------------------')

print(f'Second pattern:')
for i in range(n, 0, -1):
    print(f'The star pattern : {"*" * i}')
 