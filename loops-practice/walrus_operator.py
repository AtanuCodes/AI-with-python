# value = 14
# remainder = value % 5

# if remainder:
#     print(f'Value is not divisible, remainder is {remainder}')

# Walrus operator :=

value = 14

if remainder := value % 5:
     print(f'Value is not divisible, remainder is {remainder}')

# another example

available_sizes = ['small', 'medium', 'large']

if (requested_size := input('Whats your preferable chai cup?').lower()) in available_sizes :
     print(f'Serving {requested_size} Chai')
else:
     print(f'{requested_size} is not availble!')
