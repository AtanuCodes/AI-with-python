# calculate_bills(cups, price_per_cup)
# return total bill
# use this func for multiple orders

def calculte_bills(cups, price_per_cup):
    return cups * price_per_cup

print(f'Total bill for table 1 :', calculte_bills(2,25))
print(f'Total bill for table 2 :', calculte_bills(2,15))
print(f'Total bill for table 3 :', calculte_bills(2,50))