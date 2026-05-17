# add 10% at on evry order and make sure it is consistant
# write add_vat(price, vat_rate)
# compute final price for 3 orders

def add_vat(price, vat_rate):
    return price * (100+vat_rate)/100

orders = [100,200,300]

for price in orders:
    final_price =  add_vat(price, 10)
    print(f'Original price is {price}$ and final price is {final_price}$')