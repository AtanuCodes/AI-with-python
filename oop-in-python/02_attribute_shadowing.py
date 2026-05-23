class Chai:
    temperature = 'Hot'
    taste = 'Good'
    price = 10
cutting = Chai()

print(cutting.temperature)
print(cutting.taste)
cutting.taste = 'Very Good'
print(f'After changin value - ', cutting.taste)

cutting.Newatt = 'New value'
print(cutting.Newatt)

cutting.price = 15
print(cutting.price)

del cutting.price
print(cutting.price) 

# default fallback
