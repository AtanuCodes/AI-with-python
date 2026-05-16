# prepare order summary with customer name and order details

customer  = ['Atanu', 'Sam', 'Elon']
order = [300, 200, 100]

for name, amount in zip(customer, order):
    print(f'{name} paid {amount}$')
