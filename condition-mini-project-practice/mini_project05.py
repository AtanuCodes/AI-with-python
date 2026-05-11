# traditional tea way
# tea_amount = int(input("What is your order amount?"))
# if tea_amount >= 300:
#     print(f"Your delivery is free! Total amount is ${tea_amount}.")
# elif tea_amount < 300:
#     print(f"Your delivery charge is $30, total amount is ${tea_amount + 30}.")

# using ternery operator

tea_amount = int(input("What is your order amount?$"))
delivery_charge = 0 if tea_amount >= 300 else 30
total_amount = tea_amount + delivery_charge
print(f"Your delivery charge is ${delivery_charge}, total amount is ${total_amount}.")